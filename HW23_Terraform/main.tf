locals {
  resource_prefix = "${var.my_name}-${random_string.random.result}"
}

terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 3.36.0"
    }
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_subscription" "current" {
  subscription_id = "1c7667de-3367-49d7-8883-06f316cda9b1"
}

resource "random_string" "random" {
  length = 8
  special = false
  lower = true
  upper = false
}

resource "azurerm_resource_group" "example" {
  name     = "${local.resource_prefix}-rg"
  location = "West Europe"
}

resource "azurerm_storage_account" "example" {
  name                = "${local.resource_prefix}sa"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  account_tier        = "Standard"
  account_replication_type = "GRS"

  tags = {
    environment = "staging"
  }
}
