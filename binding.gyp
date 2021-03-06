{
  "targets": [
    {
      "target_name": "tree_sitter_jacy_binding",
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "src"
      ],
      "sources": [
        "src/parser.c",
        "bindings/node/binding.cc"
      ],
      "cflags_c": [
        "-std=c99",
      ],
      "variables": {
        "node_module_version": 80
      }
    }
  ]
}
