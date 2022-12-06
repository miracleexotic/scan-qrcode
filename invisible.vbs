Dim Args()
ReDim Args(WScript.Arguments.Count - 1)

For i = 0 To WScript.Arguments.Count - 1
   Args(i) = """" & WScript.Arguments(i) & """"
Next

CreateObject("WScript.Shell").Run Join(Args), 0, False