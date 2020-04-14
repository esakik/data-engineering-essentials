# Embulk
>Ref: https://naokirin.hatenablog.com/entry/2018/12/31/162548

## Getting Started
```bash
$ docker image build -t esakik/embulk .
$ docker container run -d --name embulk -v $(pwd)/output/output.txt:/output/output.txt esakik/embulk
```

## Execute
```bash
root@xxxx:~# embulk run config/embulk.yaml
```

## Cleanup
```bash
$ docker stop embulk
$ docker rm embulk
```
