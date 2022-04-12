from ctypes import cdll

lib = cdll.LoadLibrary("target/release/datadude.dll")

print("python: starting ...")

lib.process()

print("python: done!")

