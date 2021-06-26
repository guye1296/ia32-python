# ia32-python

Python definitions to the x86-64 architecture.

Based on [ia32-doc](https://github.com/wbenny/ia32-doc)

__NOTE__: This is still a work in progress


# Install

```bash
python -m pip install ia32-python
```

# Usage
```python
# ia32_python.intel_manual contains SDM definitions
from ia32_python.intel_manual.control_registers import Cr0

# Create a new cr0 instance
# Can pass either `int` or `bytes`
cr0 = Cr0(0x80000007)
# Show flags
cr0.flags()
# will return 'PE,MP,EM,PG'

# Bit-level slicing is available
hex(cr0[0:32])

# Assignment is also supported.
cr0[0:8] = 0

# Can set individual flags
cr0.PE = True

# Byte serialization is available
cr0.bytes
# will output b'\x01\x00\x00\x80\x00\x00\x00\x00'

# Bit fields can be easily printed!
print(cr0)
# will print
# [PE (0:1)] 0x1
# [MP (1:2)] 0x0
# [EM (2:3)] 0x0
# [TS (3:4)] 0x0
# [ET (4:5)] 0x0
# [NE (5:6)] 0x0
# [WP (16:17)] 0x0
# [AM (18:19)] 0x0
# [NW (29:30)] 0x0
# [CD (30:31)] 0x0
# [PG (31:32)] 0x1


# More complex structs are also supported
from ia32_python.intel_manual.cpuid import CpuidEax01
cpuid = CpuidEax01(0)
# Assignment can be performed to each member
cpuid.CPUID_EAX = 0x1234
# Or to individual bits
cpuid.CPUID_EAX.EXTENDED_FAMILY_ID = 0x40
# Each member contains the width in bits
cpuid.CPUID_EAX.EXTENDED_FAMILY_ID.width
# will output 8

# And the offset in bits
cpuid.CPUID_EAX.EXTENDED_FAMILY_ID.offset
# will output 20

# Like bitfields, structs can be serialized
cpuid.bytes
# will output b'4\x12\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Documentation is provided from the SDM
help(cr0.PG)


# Enums are supported
from ia32_python.intel_manual.vmx.ept.ept_entry_count import InveptType
InveptType.fields
# will output [INVEPT_SINGLE_CONTEXT (0x1), INVEPT_ALL_CONTEXT (0x2)]

# Invalid types will raise a `ValueError`
t = InveptType(3)
```
