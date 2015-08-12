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

package com.cloudera.director.client.latest.model;

import java.util.HashMap;
import java.util.Map;

public class DeploymentTemplate {
  /* Optional configurations for Cloudera Manager and its management services */
  private Map<String,Map<String,String>> configs;
  /* Whether to enable Cloudera Enterprise Trial */
  private Boolean enableEnterpriseTrial;
  /* External database template definitions */
  private Map<String,ExternalDatabaseTemplate> externalDatabaseTemplates;
  /* External database definitions */
  private Map<String,ExternalDatabase> externalDatabases;
  /* Hostname for existing Cloudera Manager installation */
  private String hostname;
  /* Password for Kerberos administrative principal used by Cloudera Manager [redacted on read] */
  private String krbAdminPassword;
  /* Username for Kerberos administrative principal used by Cloudera Manager */
  private String krbAdminUsername;
  /* License for Cloudera Manager [redacted on read] */
  private String license;
  /* Instance definition for a Cloudera Manager instance created from scratch */
  private VirtualInstance managerVirtualInstance;
  /* Deployment name */
  private String name;
  /* Web UI and API password [redacted on read] */
  private String password;
  /* Port for existing Cloudera Manager installation */
  private Integer port;
  /* Custom Cloudera Manager repository URL */
  private String repository;
  /* Custom Cloudera Manager public GPG key */
  private String repositoryKeyUrl;
  /* Whether to install unlimited strength JCE policy files */
  private Boolean unlimitedJce;
  /* Web UI and API username */
  private String username;
  public DeploymentTemplate() { }

  private DeploymentTemplate(Map<String,Map<String,String>> configs, Boolean enableEnterpriseTrial, Map<String,ExternalDatabaseTemplate> externalDatabaseTemplates, Map<String,ExternalDatabase> externalDatabases, String hostname, String krbAdminPassword, String krbAdminUsername, String license, VirtualInstance managerVirtualInstance, String name, String password, Integer port, String repository, String repositoryKeyUrl, Boolean unlimitedJce, String username) {
    this.configs = configs;
    this.enableEnterpriseTrial = enableEnterpriseTrial;
    this.externalDatabaseTemplates = externalDatabaseTemplates;
    this.externalDatabases = externalDatabases;
    this.hostname = hostname;
    this.krbAdminPassword = krbAdminPassword;
    this.krbAdminUsername = krbAdminUsername;
    this.license = license;
    this.managerVirtualInstance = managerVirtualInstance;
    this.name = name;
    this.password = password;
    this.port = port;
    this.repository = repository;
    this.repositoryKeyUrl = repositoryKeyUrl;
    this.unlimitedJce = unlimitedJce;
    this.username = username;
  }

  private DeploymentTemplate(DeploymentTemplateBuilder builder) {
    this.configs = builder.configs;
    this.enableEnterpriseTrial = builder.enableEnterpriseTrial;
    this.externalDatabaseTemplates = builder.externalDatabaseTemplates;
    this.externalDatabases = builder.externalDatabases;
    this.hostname = builder.hostname;
    this.krbAdminPassword = builder.krbAdminPassword;
    this.krbAdminUsername = builder.krbAdminUsername;
    this.license = builder.license;
    this.managerVirtualInstance = builder.managerVirtualInstance;
    this.name = builder.name;
    this.password = builder.password;
    this.port = builder.port;
    this.repository = builder.repository;
    this.repositoryKeyUrl = builder.repositoryKeyUrl;
    this.unlimitedJce = builder.unlimitedJce;
    this.username = builder.username;
  }

  public static DeploymentTemplateBuilder builder() {
    return new DeploymentTemplateBuilder();
  }

  public static class DeploymentTemplateBuilder {
    private Map<String,Map<String,String>> configs = new HashMap<String,Map<String,String>>();
    private Boolean enableEnterpriseTrial = null;
    private Map<String,ExternalDatabaseTemplate> externalDatabaseTemplates = new HashMap<String,ExternalDatabaseTemplate>();
    private Map<String,ExternalDatabase> externalDatabases = new HashMap<String,ExternalDatabase>();
    private String hostname = null;
    private String krbAdminPassword = null;
    private String krbAdminUsername = null;
    private String license = null;
    private VirtualInstance managerVirtualInstance = null;
    private String name = null;
    private String password = null;
    private Integer port = null;
    private String repository = null;
    private String repositoryKeyUrl = null;
    private Boolean unlimitedJce = null;
    private String username = null;

    public DeploymentTemplateBuilder configs(Map<String,Map<String,String>> configs) {
      this.configs = configs;
      return this;
    }

    public DeploymentTemplateBuilder enableEnterpriseTrial(Boolean enableEnterpriseTrial) {
      this.enableEnterpriseTrial = enableEnterpriseTrial;
      return this;
    }

    public DeploymentTemplateBuilder externalDatabaseTemplates(Map<String,ExternalDatabaseTemplate> externalDatabaseTemplates) {
      this.externalDatabaseTemplates = externalDatabaseTemplates;
      return this;
    }

    public DeploymentTemplateBuilder externalDatabases(Map<String,ExternalDatabase> externalDatabases) {
      this.externalDatabases = externalDatabases;
      return this;
    }

    public DeploymentTemplateBuilder hostname(String hostname) {
      this.hostname = hostname;
      return this;
    }

    public DeploymentTemplateBuilder krbAdminPassword(String krbAdminPassword) {
      this.krbAdminPassword = krbAdminPassword;
      return this;
    }

    public DeploymentTemplateBuilder krbAdminUsername(String krbAdminUsername) {
      this.krbAdminUsername = krbAdminUsername;
      return this;
    }

    public DeploymentTemplateBuilder license(String license) {
      this.license = license;
      return this;
    }

    public DeploymentTemplateBuilder managerVirtualInstance(VirtualInstance managerVirtualInstance) {
      this.managerVirtualInstance = managerVirtualInstance;
      return this;
    }

    public DeploymentTemplateBuilder name(String name) {
      this.name = name;
      return this;
    }

    public DeploymentTemplateBuilder password(String password) {
      this.password = password;
      return this;
    }

    public DeploymentTemplateBuilder port(Integer port) {
      this.port = port;
      return this;
    }

    public DeploymentTemplateBuilder repository(String repository) {
      this.repository = repository;
      return this;
    }

    public DeploymentTemplateBuilder repositoryKeyUrl(String repositoryKeyUrl) {
      this.repositoryKeyUrl = repositoryKeyUrl;
      return this;
    }

    public DeploymentTemplateBuilder unlimitedJce(Boolean unlimitedJce) {
      this.unlimitedJce = unlimitedJce;
      return this;
    }

    public DeploymentTemplateBuilder username(String username) {
      this.username = username;
      return this;
    }

    public DeploymentTemplate build() {
      return new DeploymentTemplate(this);
    }
  }

  public DeploymentTemplateBuilder toBuilder() {
    return builder()
      .configs(configs)
      .enableEnterpriseTrial(enableEnterpriseTrial)
      .externalDatabaseTemplates(externalDatabaseTemplates)
      .externalDatabases(externalDatabases)
      .hostname(hostname)
      .krbAdminPassword(krbAdminPassword)
      .krbAdminUsername(krbAdminUsername)
      .license(license)
      .managerVirtualInstance(managerVirtualInstance)
      .name(name)
      .password(password)
      .port(port)
      .repository(repository)
      .repositoryKeyUrl(repositoryKeyUrl)
      .unlimitedJce(unlimitedJce)
      .username(username)
      ;
  }
  public Map<String,Map<String,String>> getConfigs() {
    return configs;
  }
  public void setConfigs(Map<String,Map<String,String>> configs) {
    this.configs = configs;
  }

  public Boolean getEnableEnterpriseTrial() {
    return enableEnterpriseTrial;
  }
  public void setEnableEnterpriseTrial(Boolean enableEnterpriseTrial) {
    this.enableEnterpriseTrial = enableEnterpriseTrial;
  }

  public Map<String,ExternalDatabaseTemplate> getExternalDatabaseTemplates() {
    return externalDatabaseTemplates;
  }
  public void setExternalDatabaseTemplates(Map<String,ExternalDatabaseTemplate> externalDatabaseTemplates) {
    this.externalDatabaseTemplates = externalDatabaseTemplates;
  }

  public Map<String,ExternalDatabase> getExternalDatabases() {
    return externalDatabases;
  }
  public void setExternalDatabases(Map<String,ExternalDatabase> externalDatabases) {
    this.externalDatabases = externalDatabases;
  }

  public String getHostname() {
    return hostname;
  }
  public void setHostname(String hostname) {
    this.hostname = hostname;
  }

  public String getKrbAdminPassword() {
    return krbAdminPassword;
  }
  public void setKrbAdminPassword(String krbAdminPassword) {
    this.krbAdminPassword = krbAdminPassword;
  }

  public String getKrbAdminUsername() {
    return krbAdminUsername;
  }
  public void setKrbAdminUsername(String krbAdminUsername) {
    this.krbAdminUsername = krbAdminUsername;
  }

  public String getLicense() {
    return license;
  }
  public void setLicense(String license) {
    this.license = license;
  }

  public VirtualInstance getManagerVirtualInstance() {
    return managerVirtualInstance;
  }
  public void setManagerVirtualInstance(VirtualInstance managerVirtualInstance) {
    this.managerVirtualInstance = managerVirtualInstance;
  }

  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }

  public String getPassword() {
    return password;
  }
  public void setPassword(String password) {
    this.password = password;
  }

  public Integer getPort() {
    return port;
  }
  public void setPort(Integer port) {
    this.port = port;
  }

  public String getRepository() {
    return repository;
  }
  public void setRepository(String repository) {
    this.repository = repository;
  }

  public String getRepositoryKeyUrl() {
    return repositoryKeyUrl;
  }
  public void setRepositoryKeyUrl(String repositoryKeyUrl) {
    this.repositoryKeyUrl = repositoryKeyUrl;
  }

  public Boolean getUnlimitedJce() {
    return unlimitedJce;
  }
  public void setUnlimitedJce(Boolean unlimitedJce) {
    this.unlimitedJce = unlimitedJce;
  }

  public String getUsername() {
    return username;
  }
  public void setUsername(String username) {
    this.username = username;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    String newLine = System.getProperty("line.separator");
    sb.append("class DeploymentTemplate {" + newLine);
    sb.append("  configs: ").append(configs).append(newLine);
    sb.append("  enableEnterpriseTrial: ").append(enableEnterpriseTrial).append(newLine);
    sb.append("  externalDatabaseTemplates: ").append(externalDatabaseTemplates).append(newLine);
    sb.append("  externalDatabases: ").append(externalDatabases).append(newLine);
    sb.append("  hostname: ").append(hostname).append(newLine);
    sb.append("  krbAdminPassword: ").append("REDACTED").append(newLine);
    sb.append("  krbAdminUsername: ").append(krbAdminUsername).append(newLine);
    sb.append("  license: ").append("REDACTED").append(newLine);
    sb.append("  managerVirtualInstance: ").append(managerVirtualInstance).append(newLine);
    sb.append("  name: ").append(name).append(newLine);
    sb.append("  password: ").append("REDACTED").append(newLine);
    sb.append("  port: ").append(port).append(newLine);
    sb.append("  repository: ").append(repository).append(newLine);
    sb.append("  repositoryKeyUrl: ").append(repositoryKeyUrl).append(newLine);
    sb.append("  unlimitedJce: ").append(unlimitedJce).append(newLine);
    sb.append("  username: ").append(username).append(newLine);
    sb.append("}" + newLine);
    return sb.toString();
  }
}

