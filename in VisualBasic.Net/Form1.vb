Public Class Form1
    Dim b(16) As System.Windows.Forms.Button
    Dim timer As New Timer

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        b(0) = button1
        b(1) = Button2
        b(2) = Button3
        b(3) = Button4
        b(4) = Button5
        b(5) = Button6
        b(6) = Button7
        b(7) = Button8
        b(8) = Button9
        b(9) = Button10
        b(10) = Button11
        b(11) = Button12
        b(12) = Button13
        b(13) = Button14
        b(14) = Button15
        b(15) = Button16

        Dim x As Integer
        Dim myVal(15) As Integer
        myVal = randomizeIt()
        For x = 0 To 15
            b(x).Text = myVal(x)
            If (x = 15) Then b(x).Text = ""
            AddHandler b(x).Click, AddressOf clickHandler
        Next
        Timer1.Enabled = True
    End Sub

    Private Sub clickHandler(ByVal sender As Object, ByVal e As System.EventArgs)
        Dim x, index As Integer
        Dim leftEdge As Boolean
        Dim rightEdge As Boolean

        leftEdge = False
        rightEdge = False
        For x = 0 To 15
            If (sender.Equals(b(x))) Then
                index = x
                Exit For
            End If
        Next

        If (((index + 1) Mod 4) = 0) Then
            leftEdge = True
        ElseIf (((index + 1) Mod 4) = 1) Then
            rightEdge = True
        End If

        If (index + 4 <= 15 AndAlso b(index + 4).Text = "") Then
            swap(index + 4, index)
        ElseIf (index - 4 >= 0 AndAlso b(index - 4).Text = "") Then
            swap(index - 4, index)
        ElseIf (index + 1 <= 15 AndAlso (b(index + 1).Text = "" And Not (leftEdge))) Then
            swap(index + 1, index)
        ElseIf (index - 1 >= 0 AndAlso (b(index - 1).Text = "" And Not (rightEdge))) Then
            swap(index - 1, index)
        End If

    End Sub

    Private Sub swap(ByVal index1 As Integer, ByVal index2 As Integer)
        Dim temp As String
        temp = b(index1).Text
        b(index1).Text = b(index2).Text
        b(index2).Text = temp
    End Sub

    Private Function randomizeIt() As Integer()
        Dim myVal(15) As Integer
        Dim a, x As Integer
        Dim hasPrev As Boolean
        Dim RandomNumber As System.Random
        RandomNumber = New Random(System.DateTime.Now.Millisecond)

        For x = 0 To 15
            a = RandomNumber.Next(1, 15)

            Do
                For y = 0 To x - 1
                    hasPrev = False
                    If (a = myVal(y)) Then
                        hasPrev = True
                        Exit For
                    End If
                Next

                If (hasPrev) Then
                    If (a <= 14) Then
                        a += 1
                    Else
                        a = 1
                    End If
                Else
                    myVal(x) = a
                    Exit Do
                End If

            Loop While (x <= 14)
        Next

        Return myVal
    End Function

    Private Sub Button17_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button17.Click
        randomizeMe()
    End Sub

    Private Sub randomizeMe()
        Dim x As Integer
        Dim myVal(15) As Integer
        myVal = randomizeIt()
        For x = 0 To 14
            b(x).Text = myVal(x)
        Next
        b(x).Text = ""
        Timer1.Enabled = True
    End Sub

    Private Sub Timer1_Tick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Timer1.Tick
        Dim x As Integer, isComplete As Boolean

        isComplete = True
        For x = 0 To 14
            If (b(x).Text <> (x + 1).ToString) Then
                isComplete = False
                Exit For
            End If
        Next

        If (isComplete) Then
            Timer1.Enabled = False
            MsgBox("you completed")
            randomizeMe()
            Exit Sub
        End If

        isComplete = True
        For x = 1 To 15
            If (b(x).Text <> x.ToString) Then
                isComplete = False
                Exit For
            End If
        Next

        If (isComplete) Then
            Timer1.Enabled = False
            MsgBox("you completed")
            randomizeMe()
            Exit Sub
        End If
    End Sub

    Private Sub Button18_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button18.Click
        Dim c(15) As Integer
        Dim what, d(15), requiredPos, count As Integer

        If (b(15).Text <> "") Then
            MsgBox("this button must be the first step after randomization")
            Exit Sub
        End If


        For x = 1 To 15
            d(x) = b(x - 1).Text
        Next

        what = 1
        Do
            For x = 1 To 15
                If (d(x) = what) Then
                    requiredPos = x
                    Exit For
                End If
            Next

            count = 0
            For x = 1 To 15
                If (x = what) Then
                    c(x) = what
                    count = count + 1
                ElseIf (x <= requiredPos) Then
                    c(x) = d(x - count)
                Else
                    c(x) = d(x)
                End If
            Next

            If ((requiredPos Mod 2) <> (what Mod 2)) Then
                swap1(c(14), c(15))
            End If

            For x = 1 To 15
                d(x) = c(x)
            Next

            what = what + 1
        Loop While (what <= 13)

        If (d(14) = 14 And d(15) = 15) Then
            MsgBox("Make with a bottom gap", vbInformation, "Cheat")
        Else
            MsgBox("Make with a top gap", vbInformation, "Cheat")
        End If
    End Sub

    Private Sub swap1(ByRef a As Object, ByRef b As Object)
        Dim temp As Integer
        temp = a
        a = b
        b = temp
    End Sub

    Private Sub Form1_Resize(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Resize

        If (b(15) Is Nothing) Then Exit Sub

        Dim requiredDistance, requiredHeight, placeTop As Long
        Dim requiredWidth, requiredXDistance, placeLeft As Long
        Dim xWidth, yWidth As Long

        requiredHeight = Me.Height / 2
        requiredDistance = (Button17.Top + Button17.Height - b(0).Top) / 2

        requiredWidth = Me.Width / 2
        requiredXDistance = (Button4.Left + Button4.Width - button1.Left) / 2

        placeLeft = requiredWidth - requiredXDistance - 5
        placeTop = requiredHeight - requiredDistance - 20

        xWidth = b(1).Left - b(0).Left
        yWidth = b(4).Top - b(0).Top

        For x = 0 To 15
            b(x).Top = placeTop + Int(x / 4) * yWidth
            b(x).Left = placeLeft + Int(x Mod 4) * xWidth
        Next

        Button17.Top = placeTop + 4 * yWidth
        Button17.Left = placeLeft + 3 * xWidth

        Button18.Top = placeTop + 4 * yWidth
        Button18.Left = placeLeft + 2 * xWidth

    End Sub
End Class
