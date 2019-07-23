config:
   plugin_type: test
   entry_point: main.yml
subparsers:
    # the actual name of the plugin
    browbeat:
        description: Browbeat Infrared plugin
        include_groups: ["Ansible options", "Common options"]
        groups:
            - title: Browbeat
              options:
                  install:
                    type: Bool
                    help: |
                      Runs the browbeat installer
                    default: False
                  config:
                    type: FileValue
                    help: |
                      The browbeat configuration to execute
                  monitor:
                    type: Bool
                    help: |
                       Setup collectd to monitor
                    default: False
                  visualize:
                    type: Bool
                    help: |
                       Visualize system metrics through grafana dashboards
                    default: False
