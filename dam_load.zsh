#!/usr/bin/env zsh

# Load aliases from the dam data.json file in the alfred_cli.dam package.
# Usage: source this file in your shell (e.g. `source /path/to/dam_load.zsh`).

dam_load_aliases() {
  local entries

  entries=$(python3 - << 'PY'
import json
from importlib.resources import files

data_path = files("alfred_cli.dam") / "data.json"
with data_path.open() as f:
    data = json.load(f)

for key, value in data.items():
    # Print key and value separated by a tab so zsh can parse it easily
    print(f"{key}\t{value}")
PY
  )

  local key path
  while IFS=$'\t' read -r key path; do
    [[ -z "$key" ]] && continue
    # Create an alias that cds into the stored path
    alias "__$key"="cd $path"
    export "$key"="$path"
  done <<< "$entries"
}

dam_load_aliases
unset -f dam_load_aliases


