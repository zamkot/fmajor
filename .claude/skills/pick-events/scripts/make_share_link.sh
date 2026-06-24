#!/usr/bin/env bash
# Usage: make_share_link.sh <event_id> [event_id ...]
# Prints a share link with exactly those event ids starred.
set -euo pipefail

PAGES_URL="https://zamkot.github.io/fmajor/"
ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
IDS="$(IFS=,; echo "$*")"

TMP="$(mktemp -t fmajor_encode).js"
trap 'rm -f "$TMP"' EXIT

# Extract the share-payload encoder straight from build_html.py instead of
# re-implementing it, so this can't drift if the encoding ever changes.
sed -n '/const BASE62_CHARS/,/^function decodeSharePayload/p' "$ROOT/build_html.py" | sed '$d' > "$TMP"
echo "console.log('${PAGES_URL}schedule.html?share=' + encodeSharePayload([${IDS}], [], []));" >> "$TMP"

node "$TMP"
