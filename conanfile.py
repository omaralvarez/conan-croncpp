from conans import ConanFile, CMake


class croncppConan(ConanFile):
    name = "croncpp"
    version = "master"
    description = "A C++17 header-only cross-platform library for handling CRON expressions https://github.com/omaralvarez/croncpp"
    license = "MIT"
    url = "https://github.com/omaralvarez/conan-croncpp"
    repo_url = "https://github.com/omaralvarez/croncpp"
    author = "Marius Bancila, Omar Alvarez"
    exports_sources = "include/*"
    no_copy_source = True

    def source(self):
        self.run_command("git clone %s" % (self.repo_url))
    
    def run_command(self, cmd, cwd=None):
        self.output.info(cmd)
        self.run(cmd, True, cwd)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="croncpp")
        cmake.install()

    def package(self):
        pass

    def package_id(self):
        self.info.header_only()
