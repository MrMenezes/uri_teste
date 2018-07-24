def pytest_addoption(parser):
    parser.addoption("--name", action="append", default=[],
                     help="List of name to pass to test functions")


def pytest_generate_tests(metafunc):
    if 'name' in metafunc.fixturenames:
        metafunc.parametrize("name",
                             metafunc.config.getoption('name'))
