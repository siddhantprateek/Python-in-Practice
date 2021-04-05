
def subseq(unproc, proc=[], index=0):
    
    if len(unproc) == index:
        print(proc)
        return

    ch = unproc[index]

    proc.append(ch)
    subseq(unproc, proc, index+1)
    proc.pop()

    subseq(unproc, proc, index+1)

subseq("abc")

# # def subseq(unproc, proc="", index=0):

#     if len(unproc) == index:
#         print(proc)
#         return

#     ch = unproc[index]
#     subseq(unproc, proc + ch, index+1)
#     subseq(unproc, proc, index+1)

def subseqDont(unproc, proc=""):

    if unproc == "":
        print(proc)
        return

    ch = unproc[0]
    subseqDont(unproc[1:], proc + ch)
    subseqDont(unproc[1:], proc)

subseqDont("abc")