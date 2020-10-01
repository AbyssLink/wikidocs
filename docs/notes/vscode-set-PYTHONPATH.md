# 在 VS Code 中设置多个 PYTHONPATH

## 介绍

PYTHONPATH 的作用官网介绍：

> In VS Code, PYTHONPATH affects debugging, linting, IntelliSense, testing, and any other operation that depends on Python resolving modules.

可见若 PYTHONPATH 未准确设置的话，会影响 VS Code 的智能提示和代码风格检查、单元测试等，如对导入模块的解析

## 步骤

### 新方案

**（2019.11.21 更新）**
微软官网给出了更好的解决方案：[How to resolve custom imports](https://github.com/microsoft/python-language-server/blob/master/TROUBLESHOOTING.md#common-questions-and-issues)
需要解析多级目录下的自定义模块，只需设置 `python.autoComplete.extraPaths` 属性，在 `.vscode/settings.json` 中添加需要解析的目录 `./src` ：

```json
{
  "python.autoComplete.extraPaths": ["./src"]
}
```

相比原方案的优势在：不需要额外的配置文件，更改后也无需重启 VS Code

### 原方案

给定以下示例目录结构：

```shell
workspaceRootFolder
  .vscode
  |...OtherFolders
  |codeFolder
      |-__init__.py
      |...OtherLibFiles
```

进入工作区文件夹创建一个 .env 文件，在此空 .env 文件中添加一行：

```json
# 用您的文件夹名称替换codeFolder
PYTHONPATH = codeFolder
```

将 python.envFile 设置添加到 settings.json 中:

```json
"python.envFile": "${workspaceFolder}/.env"
```

然后重启 VS Code，完成解析

如果 PYTHONPATH 中希望添加多个路径怎么办呢？官网的介绍如下：

> The value of PYTHONPATH can contain multiple locations separated by os.pathsep: a semicolon (;) on Windows and a colon (:) on Linux/macOS.

由此知只需修改 .env 文件，多个需要添加到 PYTHONPATH 的文件夹间用 os.pathsep 分隔，示例：

```json
# Windows
PYTHONPATH = codeFolder1 ; codeFolder2
# Linux/macOS
PYTHONPATH = codeFolder1 : codeFolder2
```

## 体会

许多配置细节可以在官方文档和 GitHub issues 找到答案

## 参考

[https://github.com/Microsoft/...](https://github.com/Microsoft/vscode-python/issues/3840#issuecomment-463789294)
[https://code.visualstudio.com...](https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file)
