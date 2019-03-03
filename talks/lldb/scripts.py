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