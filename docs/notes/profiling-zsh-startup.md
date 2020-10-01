# zsh 使用问题 + 分析 zsh 启动项

## Issues

When install oh-my-zsh directly in macOS Catalina, I find a warning in zsh:
https://github.com/ohmyzsh/ohmyzsh/issues/6939

And I fix this warning by run this command in the prompt:

```bash
compaudit | xargs chmod g-w,o-w
```

But I don't known why this problem appear.
上述命令似乎是更改了 zsh 对文件夹的权限，嘛没找到文档有空再找。

## Profiling zsh startup

zsh 的启动速度和 fish，bash 相比应该是最慢的，但 zsh 有历史命令补全和语法高亮等功能相比 bash 更加方便，而 fish 虽然内置功能很全但部分语法和 bash 不兼容，用来用去还是得用 zsh，但是 zsh 的启动总是随着装的环境变量越多而越慢，动辄 0.5S 以上的启动速度实在是忍受不了，需要优化一下。

a measurement of the total time it takes to launch zsh, run

```bash
time zsh -i -c echo
```

And there are several ways to anaylse zsh startup time.

This article is personally most recommend. The author write a simple script to analyse the result of zsh init log to find the command which use the longest time.
https://esham.io/2018/02/zsh-profiling

This article specific a simple way to identify the zsh inti command time usage.
https://stevenvanbael.com/profiling-zsh-startup

This article use a GUI tool to see the zsh init command time usage, but the GUI tool is a littel bit hard to use.
https://best33.com/283.moe

This article use a command to see the verbose log of zsh launch time:
https://carlosbecker.com/posts/speeding-up-zsh
and the command to find out where the slowness is:

```bash
zsh -i -c -x exit
```

Use zinit instead of oh-my-zsh:
https://tech.viewv.top/2020/07/03/zsh加速.html

## Resons to slow zsh

1. nvm, pyenv, conda, etc.
2. brew auto update, brew --prefix, some lib add to path
3. zsh plugins

找到问题了，卸载了 nvm，需要其他版本的 node 用 docker 开一个；使用 pipenv 代替 pyenv。

```bash
# some method to optimize brew
# show installed package with depends
brew deps --installed --tree

# brew can use brew rmtree to remove formulae with all depends
brew rmtree <formulae>
```

## Test Result

```bash
# measure zsh startup time without config profile
time zsh --no-rcs -i -c exit
zsh --no-rcs -i -c exit  0.00s user 0.00s system 77% cpu 0.008 total

time zsh -i -c exit
zsh -i -c exit  0.09s user 0.06s system 86% cpu 0.181 total

 \time zsh -i -c exit
        0.15 real         0.08 user         0.05 sys

# test for multiple times
for i in $(seq 1 10); do /usr/bin/time zsh -i -c exit; done
        0.14 real         0.08 user         0.05 sys
        0.13 real         0.08 user         0.05 sys
        0.12 real         0.07 user         0.04 sys
        0.13 real         0.08 user         0.04 sys
        0.13 real         0.08 user         0.05 sys
        0.14 real         0.08 user         0.05 sys
        0.12 real         0.07 user         0.04 sys
        0.13 real         0.07 user         0.04 sys
        0.13 real         0.08 user         0.05 sys
        0.13 real         0.07 user         0.04 sys
```

The Output with different configs:

```bash
# Measuring initial startup time
time zsh -i -c exit
zsh -i -c exit  0.13s user 0.12s system 96% cpu 0.262 total

# Use oh-my-zsh avit theme:
zsh -i -c exit  0.09s user 0.05s system 94% cpu 0.147 total

# Use pure promot theme:
zsh -i -c exit  0.09s user 0.06s system 95% cpu 0.162 total

# Use oh-my-zsh with pure promot theme:
zsh -i -c exit  0.09s user 0.06s system 95% cpu 0.155 total
```
