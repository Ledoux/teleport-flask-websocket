if [[ ! -d ".git" ]]; then
  git init
else
  echo ".git has been already initiated"
fi
if [[ ! $(heroku apps:info -a $[run.subDomain]) ]]; then
  heroku create --app $[run.subDomain] --buildpack heroku/python --remote $[type.name]
  heroku config:set --app $[run.subDomain] TYPE=$[type.name]
else
  echo "$[run.subDomain] has been already created"
  echo "Do you wish to delete this app (y/n)?"
  read answer
  if echo "$answer" | grep -iq "^y" ;then
    heroku apps:destroy $[run.subDomain] --confirm $[run.subDomain];
    heroku create --app $[run.subDomain] --buildpack heroku/python --remote $[type.name];
    heroku config:set --app $[run.subDomain] TYPE=$[type.name];
  else
    echo No
  fi
fi
