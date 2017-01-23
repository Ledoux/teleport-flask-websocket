if [[ ! $(heroku apps:info -a $[run.subDomain]) ]]; then
  git init
  heroku create --app $[run.subDomain] --buildpack heroku/python --remote $[type.name]
  heroku config:set --app $[run.subDomain] TYPE=$[type.name]
else
  if [[ ! -d ".git" ]]; then
    git init
    heroku git:remote --app $[run.subDomain] --remote $[type.name]
  else
    echo ".git has been already initiated"
    if [[ "$(git remote | grep $[type.name])" == "$[type.name]" ]]; then
      echo "remote has been already set"
    else
      heroku git:remote --app $[run.subDomain] --remote $[type.name]
    fi
  fi
  echo "$[run.subDomain] has been already created"
  echo "Do you wish to delete this app (y/n)?"
  read answer
  if echo "$answer" | grep -iq "^y"; then
    heroku apps:destroy $[run.subDomain] --confirm $[run.subDomain];
    git init
    heroku create --app $[run.subDomain] --buildpack heroku/python --remote $[type.name];
    heroku config:set --app $[run.subDomain] TYPE=$[type.name];
  else
    echo No
  fi
fi
