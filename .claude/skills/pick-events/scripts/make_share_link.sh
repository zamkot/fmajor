#!/usr/bin/env bash
# Usage: make_share_link.sh [--label <text>] <event_id> [event_id ...]
# Prints a share link with exactly those event ids starred.
set -euo pipefail

LABEL=""
if [[ "${1:-}" == "--label" ]]; then
  LABEL="$2"
  shift 2
fi

PAGES_URL="https://zamkot.github.io/fmajor/"
ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
IDS="$(IFS=,; echo "$*")"

# Extract the share-payload encoder straight from build_html.py instead of
# re-implementing it, so this can't drift if the encoding ever changes.
{
  sed -n '/const BASE62_CHARS/,/^function decodeSharePayload/p' "$ROOT/build_html.py" | sed '$d'
  cat <<EOF
const payload = encodeSharePayload([${IDS}], [], []);
const url = new URL('${PAGES_URL}schedule.html');
url.searchParams.set('share', payload);
$([[ -n "$LABEL" ]] && echo "url.searchParams.set('by', $(node -e "console.log(JSON.stringify(process.argv[1]))" "$LABEL"));")
console.log(url.toString());
EOF
} | node -
