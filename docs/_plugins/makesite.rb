def copyReadme()
    cwd = File.dirname(__FILE__)
    Dir.chdir(File.absolute_path(File.join(cwd, "..", "..")))
    made = `make site`
    $stdout.write made
end

Jekyll::Hooks.register :site, :after_init do
    copyReadme()
end
