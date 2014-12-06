import minecraftturtle
import minecraft
import block
import os,sys
import pibrella, time, signal

mc = minecraft.Minecraft.create()

def handle_button(button):
        pibrella.buzzer.fail()
	mc.postToChat("LAVA!")
	pos = mc.player.getPos()
        mc.setBlock(pos.x, pos.y, pos.z+2, block.LAVA_FLOWING)


pibrella.button.released(handle_button)
signal.pause()
