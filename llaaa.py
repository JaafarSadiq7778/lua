import sys
import marshal

if sys.version[:3] == '3.9':
    exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s=,\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x05)\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xcd%\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x95"\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s]\x1f\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s%\x1c\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xed\x18\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xb5\x15\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00@\x00\x00\x00s\x80\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x03Z\x03e\x06j\x07d\x04d\x05\x85\x02\x19\x00e\x02e\x03\xa0\x04d\x06\xa1\x01\x83\x01k\x02rZe\x08e\x03\xa0\x04d\x07\xa1\x01\x83\x01\x01\x00n"e\te\ne\x03\xa0\x04d\x08\xa1\x01\x83\x01e\x06j\x07\xa0\x0bd\t\xa1\x01d\x02\x19\x00\x16\x00\x83\x01\x01\x00d\x04S\x00)\nF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N\xe9\x03\x00\x00\x00sy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe93\x00\x00\x00\xe9.\x00\x00\x00\xe99\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s}\x12\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00@\x00\x00\x00s\x94\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z\x05d\x02d\x04l\x06Z\x06d\x02d\x04l\x07Z\x07d\x02d\x04l\x08Z\x08d\x02d\x04l\tZ\td\x02d\x04l\nZ\nd\x02d\x04l\x0bZ\x0bd\x02d\x04l\x0cZ\x0cd\x02d\x05l\x0cm\rZ\r\x01\x00d\x06Z\x0ed\x07Z\x0fd\x08Z\x10d\tZ\x11d\nZ\x12d\x0bZ\x13d\x0cZ\x14d\rZ\x15d\x0ed\x0f\x84\x00Z\x16e\x16\x83\x00\x01\x00d\x04S\x00)\x10F\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9@\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00\xe9_\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9a\x00\x00\x00\xe9m\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00N)\x01\xda\x13generate_user_agentz\x07\x1b[1;91mz\x07\x1b[1;90mz\x07\x1b[1;97mz\x07\x1b[1;92mz\x07\x1b[1;93mz\x07\x1b[1;94mz\x07\x1b[1;95mz\x07\x1b[1;96mc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00\x0b\x00\x00\x00C\x00\x00\x00s\x9a\x02\x00\x00t\x00d\x01\x83\x01\x01\x00t\x01t\x02d\x02\x17\x00t\x03\x17\x00d\x03\x17\x00t\x02\x17\x00d\x04\x17\x00t\x03\x17\x00d\x05\x17\x00t\x04\x17\x00t\x05t\x06\xa0\x07d\x06\xa1\x01\x83\x01\x17\x00t\x02\x17\x00\x83\x01}\x00t\x01t\x02d\x02\x17\x00t\x03\x17\x00d\x03\x17\x00t\x02\x17\x00d\x04\x17\x00t\x03\x17\x00t\x05t\x06\xa0\x07d\x07\xa1\x01\x83\x01\x17\x00t\x04\x17\x00t\x05t\x06\xa0\x07d\x06\xa1\x01\x83\x01\x17\x00t\x02\x17\x00\x83\x01}\x01t\x01t\x02d\x02\x17\x00t\x03\x17\x00d\x03\x17\x00t\x02\x17\x00d\x04\x17\x00t\x03\x17\x00t\x05t\x06\xa0\x07d\x08\xa1\x01\x83\x01\x17\x00t\x04\x17\x00t\x05t\x06\xa0\x07d\x06\xa1\x01\x83\x01\x17\x00t\x02\x17\x00\x83\x01}\x02t\x08t\t|\x02d\t\x83\x02\xa0\n\xa1\x00\xa0\x0b\xa1\x00\x83\x01}\x03t\x00|\x03\x83\x01\x01\x00t\x00d\x01\x83\x01\x01\x00t\t|\x02d\t\x83\x02}\x04d\n}\x05|\x04\xa0\x0c\xa1\x00\xa0\rd\x0b\xa1\x01d\n\x19\x00}\x06|\x05|\x03k\x02\x90\x01r$d\n}\x05t\x0e\x83\x00\x01\x00d\x0c|\x06\x9b\x00d\r\x9d\x03}\x07t\x05t\x06\xa0\x07d\x0e\xa1\x01\x83\x01\xa0\x0f|\x06\xa1\x01}\x08t\x10\xa0\x11|\x08\xa1\x01}\tt\x12\xa0\x13t\x05t\x06\xa0\x07d\x0f\xa1\x01\x83\x01\xa1\x01}\n|\n\xa0\x14|\tj\x15\xa1\x01}\x0bt\x10\xa0\x11|\x07\xa1\x01j\x15}\x0c|\x0c}\r|\r\xa0\rt\x05t\x06\xa0\x07d\x10\xa1\x01\x83\x01\xa1\x01d\x11\x19\x00}\x0e|\x0e\xa0\rd\x12\xa1\x01d\n\x19\x00}\x0f|\x0bd\n\x19\x00}\x10t\x16|\x10\x83\x01d\x13k\x05\x90\x02rd|\x05d\x11\x17\x00}\x05t\x00t\x02d\x14|\x05\x9b\x00d\x15|\x06\x9b\x00d\x16|\x10\x9b\x00\x9d\x06\x17\x00\x83\x01\x01\x00d\x17t\x17|\x06\x83\x01\x17\x00d\x18\x17\x00t\x17|\x10\x83\x01\x17\x00d\x19\x17\x00}\x11t\x10\xa0\x11t\x05t\x06\xa0\x07d\x1a\xa1\x01\x83\x01t\x17|\x00\x83\x01\x17\x00t\x05t\x06\xa0\x07d\x1b\xa1\x01\x83\x01\x17\x00t\x17|\x01\x83\x01\x17\x00t\x05t\x06\xa0\x07d\x1c\xa1\x01\x83\x01\x17\x00t\x17|\x11\x83\x01\x17\x00\xa1\x01\x01\x00t\tt\x05t\x06\xa0\x07d\x1d\xa1\x01\x83\x01d\x1e\x83\x02\xa0\x18|\x06d\x0b\x17\x00\xa1\x01\x01\x00q\xfe|\x05d\x11\x17\x00}\x05t\x00t\x04d\x14|\x05\x9b\x00d\x1ft\x02\x9b\x00|\x06\x9b\x00d t\x03\x9b\x00d!|\x10\x9b\x00\x9d\t\x17\x00\x83\x01\x01\x00q\xfed\x00S\x00)"Na\x90\x01\x00\x00\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\x1b[1;92m-\xfa\x01(\xfa\x01+\xfa\x01)\xda\x05tokensy\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x03\xe9 \x00\x00\x00\xe9:\x00\x00\x00r\x00\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x04\x00\x00\x00r\x04\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x92\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x08\xe9i\x00\x00\x00\xe9d\x00\x00\x00\xe9 \x00\x00\x00\xe9T\x00\x00\x00\xe9e\x00\x00\x00\xe9l\x00\x00\x00r\x04\x00\x00\x00r\x02\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x08\x00\x00\x00r\x08\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x92\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x08\xe9f\x00\x00\x00\xe9i\x00\x00\x00\xe9l\x00\x00\x00\xe9e\x00\x00\x00\xe9 \x00\x00\x00r\x01\x00\x00\x00\xe9d\x00\x00\x00r\x04\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x08\x00\x00\x00r\x08\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xda\x01rr\x02\x00\x00\x00\xda\x01\nz@https://dev-th774578003.pantheonsite.io/amged/mmnnbb.php?target=z&&submit=%D9%85%D9%88%D8%A7%D9%81%D9%82sr\x02\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)h\xe9h\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9:\x00\x00\x00\xe9/\x00\x00\x00r\x05\x00\x00\x00\xe9d\x00\x00\x00\xe9e\x00\x00\x00\xe9v\x00\x00\x00\xe9-\x00\x00\x00r\x01\x00\x00\x00r\x00\x00\x00\x00\xe97\x00\x00\x00r\n\x00\x00\x00\xe94\x00\x00\x00\xe95\x00\x00\x00r\n\x00\x00\x00\xe98\x00\x00\x00\xe90\x00\x00\x00r\x0e\x00\x00\x00\xe93\x00\x00\x00\xe9.\x00\x00\x00r\x02\x00\x00\x00\xe9a\x00\x00\x00\xe9n\x00\x00\x00r\x01\x00\x00\x00r\x00\x00\x00\x00r\x07\x00\x00\x00\xe9o\x00\x00\x00r\x12\x00\x00\x00r\x03\x00\x00\x00\xe9i\x00\x00\x00r\x01\x00\x00\x00r\x07\x00\x00\x00r\x10\x00\x00\x00r\x14\x00\x00\x00r\x13\x00\x00\x00r\x05\x00\x00\x00r\x11\x00\x00\x00\xe9m\x00\x00\x00\xe9g\x00\x00\x00r\x07\x00\x00\x00r\x06\x00\x00\x00r\x05\x00\x00\x00r\x15\x00\x00\x00r\x15\x00\x00\x00r\x12\x00\x00\x00r\x12\x00\x00\x00\xe9b\x00\x00\x00r\x17\x00\x00\x00r\x10\x00\x00\x00r\x02\x00\x00\x00r\x00\x00\x00\x00r\x02\x00\x00\x00\xe9?\x00\x00\x00r\x01\x00\x00\x00r\x11\x00\x00\x00\xe9r\x00\x00\x00r\x16\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9=\x00\x00\x00\xe9{\x00\x00\x00\xe9}\x00\x00\x00\xe9&\x00\x00\x00r\x03\x00\x00\x00\xe9u\x00\x00\x00r\x17\x00\x00\x00r\x15\x00\x00\x00r\x14\x00\x00\x00r\x01\x00\x00\x00r\x1a\x00\x00\x00\xe9%\x00\x00\x00\xe9D\x00\x00\x00\xe99\x00\x00\x00r\x1f\x00\x00\x00r\r\x00\x00\x00r\x0c\x00\x00\x00r\x1f\x00\x00\x00r \x00\x00\x00r!\x00\x00\x00r\x1f\x00\x00\x00r\r\x00\x00\x00r\r\x00\x00\x00r\x1f\x00\x00\x00r \x00\x00\x00r\r\x00\x00\x00r\x1f\x00\x00\x00\xe9A\x00\x00\x00r\n\x00\x00\x00r\x1f\x00\x00\x00r \x00\x00\x00r!\x00\x00\x00r\x1f\x00\x00\x00r\r\x00\x00\x00\xe91\x00\x00\x00r\x1f\x00\x00\x00r \x00\x00\x00r!\x00\x00\x00r\x1f\x00\x00\x00r\r\x00\x00\x00\xe92\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\'\x00\x00\x00r\'\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xab\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\r\xe9{\x00\x00\x00\xe9c\x00\x00\x00\xe9o\x00\x00\x00\xe9i\x00\x00\x00\xe9n\x00\x00\x00\xe9s\x00\x00\x00\xe9:\x00\x00\x00\xe9(\x00\x00\x00\xe9.\x00\x00\x00\xe9*\x00\x00\x00\xe9?\x00\x00\x00\xe9)\x00\x00\x00\xe9}\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0f\x00\x00\x00r\x0f\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x8d\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x07\xe9{\x00\x00\x00\xe9c\x00\x00\x00\xe9o\x00\x00\x00\xe9i\x00\x00\x00\xe9n\x00\x00\x00\xe9s\x00\x00\x00\xe9:\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\t\x00\x00\x00r\t\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00r\x01\x00\x00\x00\xda\x01}i\x90\x01\x00\x00\xfa\x01[z\x07] id : z\x0c \n coins >> uy\x00\x00\x00\xe2\x80\xa2 instaup free+\n\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\n[\xf0\x9f\x98\x8d] ID  : ul\x00\x00\x00\n\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0 \xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\n[\xf0\x9f\x98\x8d] coins  : +z\x0c\n\n By @W_7_2s\xf6\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x1c\xe9h\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9p\x00\x00\x00\xe9s\x00\x00\x00\xe9:\x00\x00\x00\xe9/\x00\x00\x00r\x05\x00\x00\x00\xe9a\x00\x00\x00r\x02\x00\x00\x00\xe9i\x00\x00\x00\xe9.\x00\x00\x00r\x01\x00\x00\x00\xe9e\x00\x00\x00\xe9l\x00\x00\x00r\t\x00\x00\x00\xe9g\x00\x00\x00\xe9r\x00\x00\x00r\x06\x00\x00\x00\xe9m\x00\x00\x00r\x08\x00\x00\x00\xe9o\x00\x00\x00r\x0c\x00\x00\x00r\x0b\x00\x00\x00r\x05\x00\x00\x00\xe9b\x00\x00\x00r\x0e\x00\x00\x00r\x01\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x12\x00\x00\x00r\x12\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9/\x00\x00\x00\xe9s\x00\x00\x00\xe9e\x00\x00\x00\xe9n\x00\x00\x00\xe9d\x00\x00\x00\xe9M\x00\x00\x00r\x02\x00\x00\x00r\x01\x00\x00\x00r\x01\x00\x00\x00\xe9a\x00\x00\x00\xe9g\x00\x00\x00r\x02\x00\x00\x00\xe9?\x00\x00\x00\xe9c\x00\x00\x00\xe9h\x00\x00\x00r\x06\x00\x00\x00\xe9t\x00\x00\x00\xe9_\x00\x00\x00\xe9i\x00\x00\x00r\x04\x00\x00\x00\xe9=\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x11\x00\x00\x00r\x11\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x88\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x06\xe9&\x00\x00\x00\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9x\x00\x00\x00r\x01\x00\x00\x00\xe9=\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x07\x00\x00\x00r\x07\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00s\x97\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\t\xe9I\x00\x00\x00\xe9D\x00\x00\x00\xe94\x00\x00\x00\xe90\x00\x00\x00r\x03\x00\x00\x00\xe9.\x00\x00\x00\xe9t\x00\x00\x00\xe9x\x00\x00\x00r\x05\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\t\x00\x00\x00r\t\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xda\x01az\x07]): id z\x03 \n z\n coins >> )\x19\xda\x05print\xda\x05input\xda\x01E\xda\x01C\xda\x01A\xda\x04eval\xda\x07marshal\xda\x05loads\xda\x03len\xda\x04open\xda\x04read\xda\nsplitlines\xda\x08readline\xda\x05split\xda\x04exit\xda\x06format\xda\x08requests\xda\x03get\xda\x02re\xda\x07compile\xda\x07findall\xda\x04text\xda\x03int\xda\x03str\xda\x05write)\x12r\x07\x00\x00\x00\xda\x02ID\xda\x05filesZ\x06userss\xda\x04fileZ\x03kkiZ\x06useridZ\x04u1rl\xda\x03url\xda\x08responseZ\x08responsaZ\x04coinZ\x03rwrZ\x03dprZ\x03scr\xda\x01sZ\x05coinsZ\x07massage\xa9\x00r,\x00\x00\x00\xda\x06string\xda\x07instaup\x16\x00\x00\x00s>\x00\x00\x00\x00\x01\x08\x01:\x01D\x01D\x01\x16\x01\x08\x01\x08\x01\n\x01\x04\x02\x12\x01\n\x01\x04\x01\x06\x01\x0c\x01\x14\x01\n\x01\x14\x01\x0c\x01\x0c\x01\x04\x01\x18\x01\x0e\x01\x08\x01\x0e\x01\x08\x01\x1e\x01\x1c\x01H\x01 \x02\x08\x01r.\x00\x00\x00)\x17Z\x03fooZ\x03barr\x12\x00\x00\x00r\x13\x00\x00\x00r\x14\x00\x00\x00\xda\tcopyright\xda\x02os\xda\x03sys\xda\x06random\xda\x04timer\x1f\x00\x00\x00r\x1d\x00\x00\x00Z\nuser_agentr\x03\x00\x00\x00r\x11\x00\x00\x00\xda\x01Br\x10\x00\x00\x00r\x0f\x00\x00\x00\xda\x01H\xda\x01K\xda\x01Z\xda\x01Mr.\x00\x00\x00r,\x00\x00\x00r,\x00\x00\x00r,\x00\x00\x00r-\x00\x00\x00\xda\x08<module>\x02\x00\x00\x00s*\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x01\x08\x01\x08\x01\x08\x01\x08\x01\x08\x01\x0c\x01\x04\x01\x04\x01\x04\x01\x04\x01\x04\x01\x04\x01\x04\x01\x04\x01\x08"s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02s\xd3\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00g\x00d\x00\xa2\x01\x83\x01\xa0\x01\xa1\x00S\x00)\x01)\x15\xe9#\x00\x00\x00\xe9 \x00\x00\x00\xe9n\x00\x00\x00\xe9o\x00\x00\x00r\x01\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x06\x00\x00\x00r\x03\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x01\x00\x00\x00\xe9f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00r\x01\x00\x00\x00\xe9"\x00\x00\x00\xe9%\x00\x00\x00r\x04\x00\x00\x00r\n\x00\x00\x00)\x02\xda\x05bytes\xda\x06decode\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00\xfa\x01 )\x0cZ\x03fooZ\x03bar\xda\x04eval\xda\x07marshal\xda\x05loads\xda\tcopyright\xda\x03sys\xda\x07version\xda\x04exec\xda\x05printZ\x05feval\xda\x05split\xa9\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x10\x00\x00\x00\x04\x01\x04\x01\x08\x01\x0e\x01\x08\x01\x08\x02\x1c\x01\x10\x02'))
else:
    print(f'# no support for "%s"' % sys.version.split(" ")[0])