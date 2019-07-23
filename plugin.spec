config:
   plugin_type: other
   entry_point: main.yml
subparsers:
    # the actual name of the plugin
    simple-plugin:
        description: Browbeat Infrared plugin
        include_groups: ["Ansible options", "Common options"]
        groups:
            - title: Browbeat
              options:
                  rally:
                      type: Bool
                      help: Run Rally
                      default: foo
