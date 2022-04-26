terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0.0"
    }
  }
}
provider "kubernetes" {
  config_path    = "~/.kube/config"
  //config_context = "my-context"
}
resource "kubernetes_namespace" "LiVE_namespace" {
  metadata {
    name = "live"
  }
}
resource "kubernetes_deployment" "proxy" {
  metadata {
    name = "proxy"
    labels = {
      pod = "proxy"
    }
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        pod = "proxy"
      }
    }

    template {
      metadata {
        labels = {
          pod = "proxy"
       }
      }
      spec {
        container {
          image = var.proxy_image
          name = "proxy"
          port {
            container_port = 5000
          }
        }
      }
    } 
  }
}
resource "kubernetes_service" "proxy" {
  metadata {
    name = "proxy"
  }
  spec {
    selector = {
      pod = kubernetes_deployment.proxy.metadata[0].labels.pod
    }
    port {
      port = 5000
    }
    type = "LoadBalancer"
  }
}