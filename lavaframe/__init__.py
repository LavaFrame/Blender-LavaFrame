from .properties import *

class LavaFrameFile:
    """An LF file that contains all needed properties."""

    renderer:Renderer
    camera:Camera
    materials:list[Material]
    lights:list[Light]
    meshes:list[Mesh]

    def __repr__(self) -> str:
        return f"<class 'lavaframe.{__name__}', renderer={self.renderer}, camera={self.camera}, materials=list[lavaframe.properties.Material], lights=list[lavaframe.properties.Light], meshes=list[lavaframe.properties.Mesh]>"
    
    def __str__(self) -> str:
        # creative variable naming ik
        foo = ""
        foo += str(self.renderer)
        foo += str(self.camera)
        for x in self.materials + self.lights + self.meshes:
            foo += str(x)
        return foo