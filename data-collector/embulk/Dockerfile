FROM reflet/docker-embulk

RUN embulk gem install embulk-input-randomj embulk-output-command embulk-formatter-fast_jsonl embulk-filter-column

COPY . .
