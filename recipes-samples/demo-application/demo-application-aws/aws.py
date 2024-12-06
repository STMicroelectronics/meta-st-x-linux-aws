#!/usr/bin/python3
#
# Author: STMicroelectronics.
#
# Copyright (c) 2024 STMicroelectronics. All rights reserved.
#
# This software component is licensed by ST under BSD 3-Clause license,
# the "License"; You may not use this file except in compliance with the
# License. You may obtain a copy of the License at:
#
# http://www.opensource.org/licenses/BSD-3-Clause

import os
import threading
import subprocess
from subprocess import PIPE, Popen
from time import time
from time import sleep
import yaml
import gi
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Pango

gi.require_version('Gtk', '3.0')

# -------------------------------------------------------------------
# -------------------------------------------------------------------
ICON_SIZE_1080 = 260
ICON_SIZE_720 = 160
ICON_SIZE_480 = 160
ICON_SIZE_272 = 48

# return format:
# [ icon_size, font_size ]
SIZES_ID_ICON_SIZE = 0
SIZES_ID_FONT_SIZE = 1
def get_sizes_from_screen_size(width, height):
    minsize =  min(width, height)
    icon_size = None
    font_size = None
    if minsize == 720:
        icon_size = ICON_SIZE_720
        font_size = 25
    elif minsize == 480:
        icon_size = ICON_SIZE_480
        font_size = 20
    elif minsize == 272:
        icon_size = ICON_SIZE_272
        font_size = 10
    elif minsize == 600:
        icon_size = ICON_SIZE_720
        font_size = 15
    elif minsize >= 1080:
        icon_size = ICON_SIZE_1080
        font_size = 32
    return [icon_size, font_size]

def get_icon_size_from_screen_size(width, height):
    minsize =  min(width, height)
    if minsize == 720:
        return ICON_SIZE_720
    elif minsize == 480:
        return ICON_SIZE_480
    elif minsize == 272:
        return ICON_SIZE_272
    elif minsize == 600:
        return ICON_SIZE_1080
    elif minsize >= 1080:
        return ICON_SIZE_1080

class GreengrassCLI(object):
    _instance = None
    _is_running = False
    _runner = ""
    _sub_file = "/tmp/subscribe.txt"
    _mqtt_sub_msg = ""

    _RUNNER_LIST_COMPONENT = "Components"
    _RUNNER_PUBLISH = "MQTT Pub"
    _RUNNER_SUBSCRIBE = "MQTT Sub"

    _BASH_COMMAND_NOT_FOUND = ": command not found"
    _CLI_NOT_FOUND_STR = "/!\\ greengrass-cli not found"
    _CLI_ERROR_STR = "/!\\ greengrass-cli error"
    _CLI_ALREADY_RUNNING_STR = "/!\\ greengrass-cli already running by "
    
    _CLI_PATH="/opt/greengrass/v2/bin/greengrass-cli"

    def __new__(cls):
        if cls._instance is None:
            print('Creating the GreengrassCLI singleton')
            cls._instance = super(GreengrassCLI, cls).__new__(cls)
            cls._is_running = False
        return cls._instance

    def list_components(self):
        component_list = ""
        if self._is_running is False:
            self._is_running = True
            self._runner = self._RUNNER_LIST_COMPONENT

            command = f'sudo {self._CLI_PATH} component list'
            proc = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
            stdout, stderr = proc.communicate()
            if proc.returncode != 0:
                if self._BASH_COMMAND_NOT_FOUND in stderr.decode():
                    component_list=self._CLI_NOT_FOUND_STR
                else:
                    component_list=self._CLI_ERROR_STR
            else:
                component_list = stdout.decode()

            self._is_running = False
        else:
            component_list=self._CLI_ALREADY_RUNNING_STR + self._runner
        return component_list

    def mqtt_publish(self, topic, message):
        publish_response=""
        if self._is_running is False:
            self._is_running = True
            self._runner = self._RUNNER_PUBLISH

            command = f"sudo {self._CLI_PATH} pubsub pub -t \"{topic}\" -m \"{message}\""
            proc = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
            stdout, stderr = proc.communicate()
            if proc.returncode != 0:
                if self._BASH_COMMAND_NOT_FOUND in stderr.decode():
                    publish_response=self._CLI_NOT_FOUND_STR
                else:
                    publish_response=self._CLI_ERROR_STR
            else:
                publish_response="Published"

            self._is_running = False
        else:
            publish_response=self._CLI_ALREADY_RUNNING_STR + self._runner

        return publish_response

    def mqtt_subscribe_start_async(self, topic):
        if self._is_running is False:
            self._is_running = True
            self._runner = self._RUNNER_SUBSCRIBE
            self._mqtt_sub_msg = ""

            os.popen(f"echo \"\" > {self._sub_file}")
            subscribe_mqtt_command = f"sudo {self._CLI_PATH} pubsub sub -t \"{topic}\" > {self._sub_file} 2<&1"
            os.popen(subscribe_mqtt_command)

            sleep(0.2)

        else:
            self._mqtt_sub_msg = self._CLI_ALREADY_RUNNING_STR + self._runner
            
    def mqtt_subscribe_get_msg(self):
        if self.mqtt_subscribe_is_running() is True:
            msg = os.popen(f"cat {self._sub_file}").read()
            if self._BASH_COMMAND_NOT_FOUND in msg:
                self.mqtt_subscribe_stop()
                return self._CLI_NOT_FOUND_STR
            else:
                self._mqtt_sub_msg = msg

        return self._mqtt_sub_msg

    def mqtt_subscribe_stop(self):
        if self.mqtt_subscribe_is_running() is True:
            self._is_running = False
        self._mqtt_sub_msg = ""
        os.popen('sudo /usr/bin/pkill -f ".*cli.CLI pubsub sub.*"')
        os.popen(f"rm {self._sub_file}")

    def mqtt_subscribe_is_running(self):
        if self._is_running is True and self._runner == self._RUNNER_SUBSCRIBE:
            return True
        return False


class LabelConfigName(Gtk.Label):
    def __init__(self, name):
        Gtk.Label.__init__(self)
        self.set_xalign (0.0)
        self.set_text(name + ":")


class LabelConfigValue(Gtk.Label):
    def __init__(self):
        Gtk.Label.__init__(self)
        self.set_max_width_chars(20)
        self.set_hexpand(True)
        self.set_ellipsize(Pango.EllipsizeMode.MIDDLE)
        self.set_line_wrap(True) 
        self.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)
        self.set_xalign (0.0)

class ConfigPage(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self, homogeneous=False, spacing=0)
        self.set_border_width(5)

        # Display configuration grid

        self.info_grid = Gtk.Grid()
        self.info_grid.set_column_spacing(2)
        self.info_grid.set_row_spacing(2)

        # Thing Name
        self.label_thing_name = LabelConfigName("Thing Name")
        self.label_effective_thing_name = LabelConfigValue()
        self.info_grid.attach(self.label_thing_name, 0, 1, 1, 1)
        self.info_grid.attach_next_to(self.label_effective_thing_name, self.label_thing_name, Gtk.PositionType.RIGHT, 1, 1)

        # Region
        self.label_region = LabelConfigName("Region")
        self.label_effective_region = LabelConfigValue()
        self._insert_config_to_grid(self.label_region, self.label_effective_region, self.label_thing_name)

        # Role Alias
        self.label_role_alias = LabelConfigName("Role Alias")
        self.label_effective_role_alias = LabelConfigValue()
        self._insert_config_to_grid(self.label_role_alias, self.label_effective_role_alias, self.label_region)

        # Cred Endpoint
        self.label_cred_endpoint = LabelConfigName("Cred Endpoint")
        self.label_effective_cred_endpoint = LabelConfigValue()
        self._insert_config_to_grid(self.label_cred_endpoint, self.label_effective_cred_endpoint, self.label_role_alias)

        # Data Endpoint
        self.label_data_endpoint = LabelConfigName("Data Endpoint")
        self.label_effective_data_endpoint = LabelConfigValue()
        self._insert_config_to_grid(self.label_data_endpoint, self.label_effective_data_endpoint, self.label_cred_endpoint)

        # Certificate
        self.label_certificate = LabelConfigName("Certificate")
        self.label_effective_certificate = LabelConfigValue()
        self._insert_config_to_grid(self.label_certificate, self.label_effective_certificate, self.label_data_endpoint)

        # Key
        self.label_key = LabelConfigName("Private Key")
        self.label_effective_key = LabelConfigValue()
        self._insert_config_to_grid(self.label_key, self.label_effective_key, self.label_certificate)
        
        # Pkcs11 lib path
        self.label_pkcs11_lib = LabelConfigName("Pkcs11 lib path")
        self.label_effective_pkcs11_lib = LabelConfigValue()
        self._insert_config_to_grid(self.label_pkcs11_lib, self.label_effective_pkcs11_lib, self.label_key)

        # Pkcs11 slot
        self.label_pkcs11_slot = LabelConfigName("Pkcs11 slot")
        self.label_effective_pkcs11_slot = LabelConfigValue()
        self._insert_config_to_grid(self.label_pkcs11_slot, self.label_effective_pkcs11_slot, self.label_pkcs11_lib)

        # Pkcs11 userpin
        self.label_pkcs11_userpin = LabelConfigName("Pkcs11 user pin")
        self.label_effective_pkcs11_userpin = LabelConfigValue()
        self._insert_config_to_grid(self.label_pkcs11_userpin, self.label_effective_pkcs11_userpin, self.label_pkcs11_slot)

        # Put info grid into scrolled window

        self.scrolled_config = Gtk.ScrolledWindow()
        self.scrolled_config.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_config.set_vexpand(True)
        
        self.scrolled_config.add(self.info_grid)

        # Add read button

        self.button_read = Gtk.Button.new_with_label("Read")
        self.button_read.connect("clicked", self._on_read_clicked)

        # Add config page grid

        self.config_grid = Gtk.Grid()
        self.config_grid.set_column_spacing(2)
        self.config_grid.set_row_spacing(2)

        self.config_grid.attach(self.scrolled_config, 0, 1, 2, 1)
        self.config_grid.attach(self.button_read,  0, 2, 1, 1)

        self.add(self.config_grid)

        self.refresh()
    
    def _insert_config_to_grid(self, configName, configValue, upperConfigName):
        self.info_grid.attach_next_to(configName, upperConfigName, Gtk.PositionType.BOTTOM, 1, 1)
        self.info_grid.attach_next_to(configValue, configName, Gtk.PositionType.RIGHT, 1, 1)

    def _convert_yaml_none_to_str(self, data):
        if isinstance(data, list):
            data[:] = [self._convert_yaml_none_to_str(i) for i in data]
        elif isinstance(data, dict):
            for k, v in data.items():
                data[k] = self._convert_yaml_none_to_str(v)
        return 'None' if data is None else data

    def _on_read_clicked(self, button):
        print('"Read" button was clicked')
        self.refresh()

    def refresh(self):
        # Open effective configuration file
        command = 'sudo cat /opt/greengrass/v2/config/effectiveConfig.yaml'
        ret = subprocess.run(command, shell=True, capture_output=True)
        if ret.returncode == 0:
            self.config = yaml.safe_load(ret.stdout.decode('utf-8'))
            self._convert_yaml_none_to_str(self.config)

            # Display effective configuration
            self.label_effective_thing_name.set_text(self.config['system']['thingName'])
            self.label_effective_region.set_text(self.config['services']['aws.greengrass.Nucleus']['configuration']['awsRegion'])
            self.label_effective_role_alias.set_text(self.config['services']['aws.greengrass.Nucleus']['configuration']['iotRoleAlias'])
            self.label_effective_data_endpoint.set_text(self.config['services']['aws.greengrass.Nucleus']['configuration']['iotDataEndpoint'])
            self.label_effective_cred_endpoint.set_text(self.config['services']['aws.greengrass.Nucleus']['configuration']['iotCredEndpoint'])
            self.label_effective_certificate.set_text(self.config['system']['certificateFilePath'])
            self.label_effective_key.set_text(self.config['system']['privateKeyPath'])
            self.label_effective_pkcs11_slot.set_text(str(self.config['services']['aws.greengrass.crypto.Pkcs11Provider']['configuration']['slot']))
            self.label_effective_pkcs11_userpin.set_text(str(self.config['services']['aws.greengrass.crypto.Pkcs11Provider']['configuration']['userPin']))
            self.label_effective_pkcs11_lib.set_text(self.config['services']['aws.greengrass.crypto.Pkcs11Provider']['configuration']['library'])
        else:
            self.label_effective_thing_name.set_text("No effective config")
            self.label_effective_region.set_text("No effective config")
            self.label_effective_role_alias.set_text("No effective config")
            self.label_effective_data_endpoint.set_text("No effective config")
            self.label_effective_cred_endpoint.set_text("No effective config")
            self.label_effective_certificate.set_text("No effective config")
            self.label_effective_key.set_text("No effective config")
            self.label_effective_pkcs11_slot.set_text("No effective config")
            self.label_effective_pkcs11_userpin.set_text("No effective config")
            self.label_effective_pkcs11_lib.set_text("No effective config")
            
class NetworkPage(Gtk.VBox):
    def __init__(self):
        Gtk.VBox.__init__(self, homogeneous=False, spacing=0)
        self.set_border_width(5)

        self.scrolled_network = Gtk.ScrolledWindow()
        self.scrolled_network.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_network.set_vexpand(True)

        self.button_refresh_ip = Gtk.Button.new_with_label("Refresh")
        self.button_refresh_ip.connect("clicked", self._on_refresh_button_clicked)

        self.network_info_grid = Gtk.Grid()
        self.network_info_grid.set_column_spacing(2)
        self.network_info_grid.set_row_spacing(2)

        self.network_interfaces = []
        network_interface_names = self._get_network_interface_names("end") + self._get_network_interface_names("wlan")

        position_in_grid = 1
        for network_interface_name in network_interface_names:
            label = Gtk.Label()
            label.set_max_width_chars(20)
            label.set_xalign (0.0)
            label.set_hexpand(True)
            label.set_line_wrap(True)
            self.network_interfaces.append((network_interface_name, label))
            self.network_info_grid.attach(label, 0, position_in_grid, 1, 1)
            position_in_grid = position_in_grid + 1

        self.scrolled_network.add(self.network_info_grid)

        self.network_grid = Gtk.Grid()
        self.network_grid.set_column_spacing(2)
        self.network_grid.set_row_spacing(2)

        self.network_grid.attach(self.scrolled_network, 0, 1, 2, 1)
        self.network_grid.attach(self.button_refresh_ip,  0, 2, 1, 1)

        self.add(self.network_grid)

        self.refresh()

    def _get_network_interface_names(self, name):
        network_interface = []
        command = f'ip a | grep -o {name}[0-9]'
        ret = subprocess.run(command, shell=True, capture_output=True)
        if ret.returncode == 0:
            network_interface = list(dict.fromkeys(ret.stdout.decode('utf-8').splitlines()))
        return network_interface

    def _on_refresh_button_clicked(self, button):
        print('"Refresh ip" button was clicked')
        self.refresh()

    def refresh(self):
        for network_interface in self.network_interfaces:
            name, label = network_interface

            ip = os.popen(f"ip -4 addr show {name} | grep -oP '(?<=inet\s)\d+(\.\d+){{3}}'").read().strip()
            label.set_text(f"{name}: " + ip)

class ComponentPage(Gtk.VBox):
    def __exit__(self, exc_type, exc_value, traceback):
        if self.thread_components.is_alive():
            self._stop_list_component()
            self.thread_components.join()

    def __init__(self):
        Gtk.VBox.__init__(self, homogeneous=False, spacing=0)
        self.set_border_width(5)

        self.component_grid = Gtk.Grid()
        self.component_grid.set_column_spacing(2)
        self.component_grid.set_row_spacing(2)

        self.scrolled_components = Gtk.ScrolledWindow()
        self.scrolled_components.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        self.label_component_list = Gtk.Label()
        self.label_component_list.set_max_width_chars(20)
        self.label_component_list.set_hexpand(True)
        self.label_component_list.set_ellipsize(Pango.EllipsizeMode.MIDDLE)
        self.label_component_list.set_line_wrap(True)
        self.label_component_list.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)
        self.label_component_list.set_xalign (0.0)
        self.label_component_list.set_xalign (0.0)
        self.scrolled_components.set_vexpand(True)
        self.scrolled_components.add(self.label_component_list)

        self.button_get_components = Gtk.Button.new_with_label("Refresh")
        self.button_get_components.connect("clicked", self._on_get_components_clicked)

        self.component_grid.attach(self.scrolled_components, 0, 1, 2, 1)
        self.component_grid.attach(self.button_get_components,  0, 2, 1, 1)

        self.add(self.component_grid)

        # Start in a thread the command to get the green grass components
        self.thread_components = threading.Thread(target=self._get_component_threaded)
        self.thread_components.start()

    def _get_component_threaded(self):
        print('greengrass-cli component list')
        self.label_component_list.set_text("Getting components...")

        gg_cli = GreengrassCLI()

        component_list = gg_cli.list_components()
        self.label_component_list.set_text(component_list)
    
    def _on_get_components_clicked(self, button):
        print('"Refresh components" button was clicked')
        if not self.thread_components.is_alive():
            self.thread_components = threading.Thread(target=self._get_component_threaded)
            self.thread_components.start()

    def _stop_list_component(self):
        os.popen('sudo /usr/bin/pkill -f ".*cli.CLI component list.*"')

class MqttSubPage(Gtk.VBox):
    def __exit__(self, exc_type, exc_value, traceback):
        if self.thread_mqtt_publish.is_alive():
            self._stop_mqtt_pub()
            self.thread_mqtt_publish.join()
        
    def __init__(self):
        Gtk.VBox.__init__(self, homogeneous=False, spacing=0)
        self.set_border_width(5)

        self.button_mqtt_subscribe = Gtk.Button.new_with_label("Subscribe")
        self.button_mqtt_subscribe.connect("clicked", self._on_mqtt_subscribe_clicked)

        self.label_mqtt_subscribe_topic = Gtk.Label("Topic: ")
        self.label_mqtt_subscribe_topic.set_xalign (0.0)
        self.entry_mqtt_subscribe_topic = Gtk.Entry()
        self.entry_mqtt_subscribe_topic.set_text("+/hello/world")
        self.scrolled_subscribe_mqtt = Gtk.ScrolledWindow()
        self.scrolled_subscribe_mqtt.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_subscribe_mqtt.set_vexpand(True)
        self.subscribe_msg_mqtt_label = Gtk.Label("")
        self.subscribe_msg_mqtt_label.set_max_width_chars(20)
        self.subscribe_msg_mqtt_label.set_hexpand(True)
        self.subscribe_msg_mqtt_label.set_ellipsize(Pango.EllipsizeMode.MIDDLE)
        self.subscribe_msg_mqtt_label.set_line_wrap(True)
        self.subscribe_msg_mqtt_label.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)
        self.subscribe_msg_mqtt_label.set_xalign (0.0)
        self.subscribe_msg_mqtt_label.set_xalign (0.0)
        self.scrolled_subscribe_mqtt.add(self.subscribe_msg_mqtt_label)

        self.label_mqtt_sub_state = Gtk.Label("")
        self.label_mqtt_sub_state.set_xalign (0.0)
        self.scrolled_mqtt_sub_state = Gtk.ScrolledWindow()
        self.scrolled_mqtt_sub_state.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_mqtt_sub_state.set_vexpand(True)
        self.scrolled_mqtt_sub_state.add(self.label_mqtt_sub_state)


        self.mqtt_sub_grid = Gtk.Grid()
        self.mqtt_sub_grid.set_column_spacing(2)
        self.mqtt_sub_grid.set_row_spacing(2)

        self.mqtt_sub_grid.attach(self.label_mqtt_subscribe_topic, 0, 1, 1, 1)
        self.mqtt_sub_grid.attach(self.entry_mqtt_subscribe_topic, 1, 1, 1, 1)
        self.mqtt_sub_grid.attach(self.scrolled_mqtt_sub_state, 0, 2, 2, 1)
        self.mqtt_sub_grid.attach(self.button_mqtt_subscribe, 0, 3, 2, 1)
        self.mqtt_sub_grid.attach(self.scrolled_subscribe_mqtt, 2, 1, 1, 3)

        self.thread_mqtt_subscribe = threading.Thread(target=self._subscribe_mqtt_threaded)
        self.subscribe_mqtt_flag = False

        self.add(self.mqtt_sub_grid)

    def _on_mqtt_subscribe_clicked(self, button):
        print('"Subscribe mqtt" button was clicked')

        if not self.thread_mqtt_subscribe.is_alive():
            self.button_mqtt_subscribe.set_label("Unsubscribe")
            self.label_mqtt_sub_state.set_text("Subscribing...")
            self.subscribe_msg_mqtt_label.set_text("")

            self.thread_mqtt_subscribe = threading.Thread(target=self._subscribe_mqtt_threaded)
            self.thread_mqtt_subscribe.start()
        else:
            self.button_mqtt_subscribe.set_label("Subscribe")
            self.label_mqtt_sub_state.set_text("")
            self.subscribe_msg_mqtt_label.set_text("")
            self.subscribe_mqtt_flag = False
            self.thread_mqtt_subscribe.join()

    def _subscribe_mqtt_threaded(self):
        self.subscribe_mqtt_flag = True

        gg_cli = GreengrassCLI()
        gg_cli.mqtt_subscribe_start_async(self.entry_mqtt_subscribe_topic.get_text())
        
        msg = gg_cli.mqtt_subscribe_get_msg()
        self.subscribe_msg_mqtt_label.set_text(msg)

        last_msg = ""
        last_scrolled_pos = None

        while gg_cli.mqtt_subscribe_is_running() is True and self.subscribe_mqtt_flag is True:
            msg = gg_cli.mqtt_subscribe_get_msg()
            if msg != last_msg:
                self.label_mqtt_sub_state.set_text("Subscribed")
                last_msg = msg
                self.subscribe_msg_mqtt_label.set_text(msg)
            adj = self.scrolled_subscribe_mqtt.get_vadjustment()
            new_scrolled_pos = adj.get_upper() - adj.get_page_size()
            if new_scrolled_pos is not None and new_scrolled_pos != last_scrolled_pos:
                last_scrolled_pos = new_scrolled_pos
                adj.set_value( new_scrolled_pos )
            sleep(1)

        gg_cli.mqtt_subscribe_stop()
        self.label_mqtt_sub_state.set_text("")
        self.button_mqtt_subscribe.set_label("Subscribe")


class MqttPubPage(Gtk.VBox):
    def __exit__(self, exc_type, exc_value, traceback):
        if self.thread_mqtt_subscribe.is_alive():
            self.subscribe_mqtt_flag = False
            self.thread_mqtt_subscribe.join()
        
    def __init__(self):
        Gtk.VBox.__init__(self, homogeneous=False, spacing=0)
        self.set_border_width(5)

        self.button_mqtt_publish = Gtk.Button.new_with_label("Publish")
        self.button_mqtt_publish.connect("clicked", self._on_mqtt_publish_clicked)

        self.label_mqtt_pub_topic = Gtk.Label("Topic: ")
        self.label_mqtt_pub_topic.set_xalign (0.0)
        self.entry_mqtt_pub_topic = Gtk.Entry()
        self.entry_mqtt_pub_topic.set_text("from_core/hello/world")
        self.label_mqtt_pub_message = Gtk.Label("Message: ")
        self.label_mqtt_pub_message.set_xalign (0.0)
        self.entry_mqtt_pub_message = Gtk.Entry()
        self.entry_mqtt_pub_message.set_text("HelloWorld from x-linux-aws")
        self.label_mqtt_pub_state = Gtk.Label("")
        self.label_mqtt_pub_state.set_xalign (0.0)
        self.scrolled_mqtt_pub = Gtk.ScrolledWindow()
        self.scrolled_mqtt_pub.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_mqtt_pub.set_vexpand(True)
        self.scrolled_mqtt_pub.add(self.label_mqtt_pub_state)

        self.mqtt_pub_grid = Gtk.Grid()
        self.mqtt_pub_grid.set_column_spacing(2)
        self.mqtt_pub_grid.set_row_spacing(2)

        self.mqtt_pub_grid.attach(self.label_mqtt_pub_topic, 0, 1, 1, 1)
        self.mqtt_pub_grid.attach(self.entry_mqtt_pub_topic, 1, 1, 1, 1)
        self.mqtt_pub_grid.attach(self.label_mqtt_pub_message, 0, 2, 1, 1)
        self.mqtt_pub_grid.attach(self.entry_mqtt_pub_message, 1, 2, 1, 1)
        self.mqtt_pub_grid.attach(self.scrolled_mqtt_pub, 0, 3, 2, 1)
        self.mqtt_pub_grid.attach(self.button_mqtt_publish, 0, 4, 2, 1)

        self.add(self.mqtt_pub_grid)

        self.thread_mqtt_publish = threading.Thread(target=self._publish_mqtt_threaded)

    def _on_mqtt_publish_clicked(self, button):
        print('"Publish mqtt" button was clicked')
        if not self.thread_mqtt_publish.is_alive():
            self.thread_mqtt_publish = threading.Thread(target=self._publish_mqtt_threaded)
            self.thread_mqtt_publish.start()

    def _stop_mqtt_pub(self):
        os.popen('sudo /usr/bin/pkill -f ".*cli.CLI pubsub pub.*"')

    def _publish_mqtt_threaded(self):
        self.label_mqtt_pub_state.set_text("Publishing...")
        gg_cli = GreengrassCLI()

        publish_return = gg_cli.mqtt_publish(self.entry_mqtt_pub_topic.get_text(), self.entry_mqtt_pub_message.get_text())
        self.label_mqtt_pub_state.set_text(publish_return)

class AwsGreengrass(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "AWS", parent, 0, title="Simple Notebook Example")

        self.maximize()
        try:
            display = Gdk.Display.get_default()
            monitor = display.get_primary_monitor()
            geometry = monitor.get_geometry()
            scale_factor = monitor.get_scale_factor()
            self.screen_width = scale_factor * geometry.width
            self.screen_height = scale_factor * geometry.height
        except:
            self.screen_width = self.get_screen().get_width()
            self.screen_height = self.get_screen().get_height()

        self.icon_size = get_icon_size_from_screen_size(self.screen_width, self.screen_height)
        sizes = get_sizes_from_screen_size(self.screen_width, self.screen_height)
        self.font_size = sizes[SIZES_ID_FONT_SIZE]

        self.set_decorated(False)
        rgba = Gdk.RGBA(0.31, 0.32, 0.31, 0.8)
        self.override_background_color(0,rgba)

        mainvbox = self.get_content_area()

        # Enable double click to close page

        self.previous_click_time=0
        self.connect("button-release-event", self.on_page_press_event)

        # Create Notebook with tabs

        self.notebook = Gtk.Notebook()

        self.page_network = NetworkPage()
        self.page_config = ConfigPage()
        self.page_components = ComponentPage()
        self.page_mqtt_pub = MqttPubPage()
        self.page_mqtt_sub = MqttSubPage()

        self.notebook.append_page(self.page_config, Gtk.Label(label="Settings"))
        self.notebook.append_page(self.page_components, Gtk.Label(label="Components"))
        self.notebook.append_page(self.page_network, Gtk.Label(label="LAN"))
        self.notebook.append_page(self.page_mqtt_pub, Gtk.Label(label="MQTT Pub"))
        self.notebook.append_page(self.page_mqtt_sub, Gtk.Label(label="MQTT Sub"))

        # Display title

        self.title = Gtk.Label()
        self.title.set_markup(f"<span font='{self.font_size + 5}' color='#FFFFFFFF'><b>AWS Greengrass</b></span>")

        # Create main grid

        self.main_grid = Gtk.Grid()
        self.main_grid.attach(self.title,  0, 1, 1, 1)
        self.main_grid.attach(self.notebook,  0, 2, 1, 1)

        mainvbox.pack_start(self.main_grid, False, True, 3)
        self.show_all()

    def on_page_press_event(self, widget, event):
        self.click_time = time()
        #print(self.click_time - self.previous_click_time)
        # TODO : a fake click is observed, workaround hereafter
        if (self.click_time - self.previous_click_time) < 0.01:
            self.previous_click_time = self.click_time
        elif (self.click_time - self.previous_click_time) < 0.3:
            print ("double click : exit")
            self.destroy()
        else:
            #print ("simple click")
            self.previous_click_time = self.click_time

def create_subdialogwindow(parent):
    _window = AwsGreengrass(parent)
    _window.show_all()
    response = _window.run()
    _window.destroy()
