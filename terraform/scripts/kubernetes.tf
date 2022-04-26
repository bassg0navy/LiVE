resource "kubernetes_namespace" "LiVE_namespace" {
  metadata {
    name = "LiVE"
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