# lambda-cloudwatch-alarm-to-slack

## required
- ansible >= 2.2.0.0

## deploy
```bash
$ ansible-playbook deploy.yml --ask-vault-pass
```

```
# with AWS Config environment variable
$ AWS_PROFILE=kikusu AWS_DEFAULT_REGION=us-west-2 ansible-playbook deploy.yml
```
