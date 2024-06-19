class Build:
    total = 0

    def __init__(self):
        self.buildtotal()

    def buildtotal(self):
        Build.total += 1
        print(f'build{Build.total}', locals())


for i in range(1, 40 + 1):
    exec(f'build{i} = Build()')
