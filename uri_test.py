import subprocess


def test(name):
    module = __import__('casos_' + name)
    for caso in module.casos:
        proc = subprocess.Popen('python ' + name + '.py',
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

        proc.stdin.write(caso['entrada'].encode('utf-8'))
        proc.stdin.flush()
        stdout, stderr = proc.communicate()
        assert stdout == caso['saida'].encode('utf-8')
