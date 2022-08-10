import cx_Freeze

executables = [cx_Freeze.Executable("import.py")]

cx_Freeze.setup(
    name="The Adventure of Chestnut",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["background.png",
                                                                     "checkpoint.png", "DIAMOND.png", "Door.png",
                                                                     "coin.png", "enemy.png",
                                                                     "floor1.png", "logo.png", "nutf2.png", "SPIKE.png",
                                                                     "Title.png", "WALL.png", "Vine.png"]}},
    description="The Adventure of Chestnut Game",
    executables=executables
)
