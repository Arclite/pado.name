# Dynamic Debugging with LLDB
- Show setting breakpoints with the debugger and printing different values on already-existing variables
- Show setting conditions on breakpoints
	- `cell.accessoryView is UISwitch`
	- `ex (cell.accessoryView as? UISwitch)?.onTintColor = .red`
- Show visual debugger, demo looking at different parts of the app.
- Show that you can see values of views, but not edit them.
- Demonstrate editing views in the app the “old fashioned” way
	- `expr -l Swift -- unsafeBitCast(0x8deadbeef, to: Type.self)`
- Demonstrate command aliases
	- `command alias uikit --l import UIKit`
- Show adding aliases to `~/.lldbinit` for use each time.
- Show creating a breakpoint to automatically run this alias each app launch.
- Demonstrate that you can create your own scripts with Python.
- Show creating the `cast` command.

```python
import lldb
import shlex

def Let(debugger, command, result, internal_dict):
  target = debugger.GetSelectedTarget()
  process = target.GetProcess()
  thread = process.GetSelectedThread() 
  currentFrame = thread.GetSelectedFrame()

  identifier, pointer, castType = shlex.split(command)
  expression = "let {0} = unsafeBitCast({1}, to: {2}.self)".format(identifier, pointer, castType)

  expressionOptions = lldb.SBExpressionOptions()
  expressionOptions.SetLanguage(lldb.eLanguageTypeSwift)

  castObject = currentFrame.EvaluateExpression(expression, expressionOptions)

  result.AppendMessage(castObject.GetObjectDescription())

def __lldb_init_module(debugger, internal_dict):
  debugger.HandleCommand("command script add -f " + __name__ + "." + ".Let let"
```

## Useful Links
[https://developer.apple.com/wwdc18/412](https://developer.apple.com/wwdc18/412)
[https://lldb.llvm.org/python\_reference/index.html](https://lldb.llvm.org/python_reference/index.html)
[https://github.com/facebook/chisel](https://github.com/facebook/chisel)
[https://www.objc.io/issues/19-debugging/lldb-debugging/](https://www.objc.io/issues/19-debugging/lldb-debugging/)