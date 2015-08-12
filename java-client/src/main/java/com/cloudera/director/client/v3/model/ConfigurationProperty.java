// Licensed to Cloudera, Inc. under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  Cloudera, Inc. licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Note: This file is auto generated. Do not edit manually.

package com.cloudera.director.client.v3.model;

import java.util.ArrayList;
import java.util.List;

public class ConfigurationProperty {
  /* Configuration property key */
  private String configKey;
  /* The default value for this property */
  private String defaultValue;
  /* Description of the configuration property */
  private String description;
  /* The character to use to separate lists */
  private String listSeparator;
  /* Configuration property name */
  private String name;
  /* The placeholder value to use if the value is unset */
  private String placeholder;
  /* Whether this property is required */
  private Boolean required;
  /* Whether this property is sensitive */
  private Boolean sensitive;
  /* This property's type */
  private String type;
  /* A list of all valid values for this property */
  private List<ConfigurationPropertyValue> validValues;
  /* The widget used to display this property */
  private String widget;
  public interface Type {
    String BOOLEAN = "BOOLEAN";
    String INTEGER = "INTEGER";
    String DOUBLE = "DOUBLE";
    String STRING = "STRING";
  }
  public interface Widget {
    String RADIO = "RADIO";
    String CHECKBOX = "CHECKBOX";
    String TEXT = "TEXT";
    String PASSWORD = "PASSWORD";
    String NUMBER = "NUMBER";
    String TEXTAREA = "TEXTAREA";
    String FILE = "FILE";
    String LIST = "LIST";
    String OPENLIST = "OPENLIST";
    String MULTI = "MULTI";
    String OPENMULTI = "OPENMULTI";
  }
  public ConfigurationProperty() { }

  private ConfigurationProperty(String configKey, String defaultValue, String description, String listSeparator, String name, String placeholder, Boolean required, Boolean sensitive, String type, List<ConfigurationPropertyValue> validValues, String widget) {
    this.configKey = configKey;
    this.defaultValue = defaultValue;
    this.description = description;
    this.listSeparator = listSeparator;
    this.name = name;
    this.placeholder = placeholder;
    this.required = required;
    this.sensitive = sensitive;
    this.type = type;
    this.validValues = validValues;
    this.widget = widget;
  }

  private ConfigurationProperty(ConfigurationPropertyBuilder builder) {
    this.configKey = builder.configKey;
    this.defaultValue = builder.defaultValue;
    this.description = builder.description;
    this.listSeparator = builder.listSeparator;
    this.name = builder.name;
    this.placeholder = builder.placeholder;
    this.required = builder.required;
    this.sensitive = builder.sensitive;
    this.type = builder.type;
    this.validValues = builder.validValues;
    this.widget = builder.widget;
  }

  public static ConfigurationPropertyBuilder builder() {
    return new ConfigurationPropertyBuilder();
  }

  public static class ConfigurationPropertyBuilder {
    private String configKey = null;
    private String defaultValue = null;
    private String description = null;
    private String listSeparator = null;
    private String name = null;
    private String placeholder = null;
    private Boolean required = null;
    private Boolean sensitive = null;
    private String type = null;
    private List<ConfigurationPropertyValue> validValues = new ArrayList<ConfigurationPropertyValue>();
    private String widget = null;

    public ConfigurationPropertyBuilder configKey(String configKey) {
      this.configKey = configKey;
      return this;
    }

    public ConfigurationPropertyBuilder defaultValue(String defaultValue) {
      this.defaultValue = defaultValue;
      return this;
    }

    public ConfigurationPropertyBuilder description(String description) {
      this.description = description;
      return this;
    }

    public ConfigurationPropertyBuilder listSeparator(String listSeparator) {
      this.listSeparator = listSeparator;
      return this;
    }

    public ConfigurationPropertyBuilder name(String name) {
      this.name = name;
      return this;
    }

    public ConfigurationPropertyBuilder placeholder(String placeholder) {
      this.placeholder = placeholder;
      return this;
    }

    public ConfigurationPropertyBuilder required(Boolean required) {
      this.required = required;
      return this;
    }

    public ConfigurationPropertyBuilder sensitive(Boolean sensitive) {
      this.sensitive = sensitive;
      return this;
    }

    public ConfigurationPropertyBuilder type(String type) {
      this.type = type;
      return this;
    }

    public ConfigurationPropertyBuilder validValues(List<ConfigurationPropertyValue> validValues) {
      this.validValues = validValues;
      return this;
    }

    public ConfigurationPropertyBuilder widget(String widget) {
      this.widget = widget;
      return this;
    }

    public ConfigurationProperty build() {
      return new ConfigurationProperty(this);
    }
  }

  public ConfigurationPropertyBuilder toBuilder() {
    return builder()
      .configKey(configKey)
      .defaultValue(defaultValue)
      .description(description)
      .listSeparator(listSeparator)
      .name(name)
      .placeholder(placeholder)
      .required(required)
      .sensitive(sensitive)
      .type(type)
      .validValues(validValues)
      .widget(widget)
      ;
  }
  public String getConfigKey() {
    return configKey;
  }
  public void setConfigKey(String configKey) {
    this.configKey = configKey;
  }

  public String getDefaultValue() {
    return defaultValue;
  }
  public void setDefaultValue(String defaultValue) {
    this.defaultValue = defaultValue;
  }

  public String getDescription() {
    return description;
  }
  public void setDescription(String description) {
    this.description = description;
  }

  public String getListSeparator() {
    return listSeparator;
  }
  public void setListSeparator(String listSeparator) {
    this.listSeparator = listSeparator;
  }

  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }

  public String getPlaceholder() {
    return placeholder;
  }
  public void setPlaceholder(String placeholder) {
    this.placeholder = placeholder;
  }

  public Boolean getRequired() {
    return required;
  }
  public void setRequired(Boolean required) {
    this.required = required;
  }

  public Boolean getSensitive() {
    return sensitive;
  }
  public void setSensitive(Boolean sensitive) {
    this.sensitive = sensitive;
  }

  public String getType() {
    return type;
  }
  public void setType(String type) {
    this.type = type;
  }

  public List<ConfigurationPropertyValue> getValidValues() {
    return validValues;
  }
  public void setValidValues(List<ConfigurationPropertyValue> validValues) {
    this.validValues = validValues;
  }

  public String getWidget() {
    return widget;
  }
  public void setWidget(String widget) {
    this.widget = widget;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    String newLine = System.getProperty("line.separator");
    sb.append("class ConfigurationProperty {" + newLine);
    sb.append("  configKey: ").append(configKey).append(newLine);
    sb.append("  defaultValue: ").append(defaultValue).append(newLine);
    sb.append("  description: ").append(description).append(newLine);
    sb.append("  listSeparator: ").append(listSeparator).append(newLine);
    sb.append("  name: ").append(name).append(newLine);
    sb.append("  placeholder: ").append(placeholder).append(newLine);
    sb.append("  required: ").append(required).append(newLine);
    sb.append("  sensitive: ").append(sensitive).append(newLine);
    sb.append("  type: ").append(type).append(newLine);
    sb.append("  validValues: ").append(validValues).append(newLine);
    sb.append("  widget: ").append(widget).append(newLine);
    sb.append("}" + newLine);
    return sb.toString();
  }
}

