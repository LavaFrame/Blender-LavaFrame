# properties of an LF file
from enum import Enum
from typing import Literal

class LavaFrameProperty:
    """The base property class for a LavaFrame property."""

    def __str__(self) -> str:
        properties = '\n'.join([
            f"{v} {x}" for v, x in zip(self.__dict__.keys(), self.__dict__.values()) if not v.startswith("__")
        ])
        properties = properties.replace('[', '').replace(']', '').replace(',', '').replace('(', '').replace(')', '')
        if not self.__dict__.get("name"):
            return f"{type(self).__name__}\n{{\n{properties}\n}}"
        else:
            return f"{type(self).__name__} {self.__dict__['name']}\n{{\n{properties}\n}}"
    
    def __init__(self, **kwargs) -> None:
        for v in kwargs.keys():
            self.__dict__[v] = kwargs[v]

    def __call__(self, **kwds):
        return super().__init__(**kwds)

class Renderer(LavaFrameProperty):
    resolution:tuple[int, int]
    maxDepth:int
    tileWidth:int
    tileHeight:int
    envMap:str
    hdrMultiplier:float

class Camera(LavaFrameProperty):
    position:tuple[float, float, float]
    lookAt:tuple[float, float, float]
    fov:float

class mesh(LavaFrameProperty):
    file:str
    material:str
    position:tuple[float, float, float]
    scale:tuple[float, float, float]

class light(LavaFrameProperty):
    type:Literal["Sphere", "Quad"]
    position:tuple[float, float, float]
    emission:tuple[float, float, float]
    radius:float
    v1:tuple[float, float, float]
    v2:tuple[float, float, float]

class material(LavaFrameProperty):
    name:str
    color:tuple[float, float, float]
    albedo:tuple[float, float, float]
    emission:tuple[float, float, float]
    metallic:float
    roughness:float
    subsurface:float
    specular:float
    specularTint:float
    anisotropic:float
    sheen:float
    sheenTint:float
    clearcoat:float
    clearcoatRoughness:float
    transmission:float
    ior:float
    extinction:tuple[float, float, float]
    albedoTexture:str
    metallicRoughness:str
    normalTexture:str

# TODO remove below, this is for testing of the __str__ function.
if __name__ == "__main__":
    r = Renderer(intValue=90, floatValue=10.5, stringValue="John", tupleValue=(1, 2))
    print(str(r))