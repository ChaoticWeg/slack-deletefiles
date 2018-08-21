#!/usr/bin/env bash

## slack file deletion

# get this dir and pushd into it
this_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
pushd "${this_dir}" >/dev/null 2>&1

logdir="${this_dir}/logs"
mkdir -p "${logdir}"

logfile="${this_dir}/logs/$(date +"%Y%m%d_%H%M%S.log")"
pyfile="${this_dir}/main.py"

/usr/bin/python -m pipenv run python "${pyfile}" >"${logfile}" 2>&1
py_ok=$?


## post results to discord webhook

pushd "${this_dir}/discord.sh" >/dev/null 2>&1

embed_color=
case "${py_ok}" in
    0) embed_color="0x0fba00";;
    *) embed_color="0xba0000";;
esac

# log contents: escape newlines and strip control characters
log_contents="$(cat -v "${logfile}" | sed ':a;N;$!ba;s/\n/\\n/g' | tr -d '\000-\037')"
embed_desc="${log_contents}\n\nCC: <@149987025573904385>"

# post log output and logfile
bash discord.sh \
    --username "slack-deletefiles" \
    --title "File Deletion" \
    --color "${embed_color}" \
    --description "${embed_desc}" \
    --timestamp

bash discord.sh \
    --file "${logfile}" \
    --text "Full log file attached: $(basename "${logfile}")"

popd >/dev/null 2>&1
popd >/dev/null 2>&1

exit $py_ok

