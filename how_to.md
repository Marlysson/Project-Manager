# Como sincronizar o seu Fork com o repo principal

* Adicione um remote que aponte para o repositório de origem com o comando:

```
git remote add upstream https://github.com/Marlysson/Project-Manager.git
```
* Agora você vai ter um remote chamado `origin` e o recém adicionado `upstream`. Para conferir digite

```
git remote -v
```

* Com o comando a seguir baixe as alterações do remote `upstream`.

```
git fetch upstream
```

* Vá para a branch `master`.

```
git checkout master
```

* Faça o merge da branch `master` com `upstream` no seu repositório local.

```
git merge upstream/master
```

* Envie suas alterações para o seu repositório.

```
git push
```

A partir daí continue suas alterações. Não se esqueça de enviar um Pull Request no final.