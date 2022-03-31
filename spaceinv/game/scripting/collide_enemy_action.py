
from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideEnemyAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        enemies = cast.get_first_actor(ENEMY_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        over_sound = Sound(OVER_SOUND)

        for enemy in enemies:
            ship_body = ship.get_body()
            enemy_body = enemy.get_body()
        
            if self._physics_service.has_collided(ship_body, enemy_body):
                sound = Sound(Shipexplotion_SOUND)
                self._audio_service.play_sound(sound)
                stats.lose_life() 

                if stats.get_lives() > 0:
                    callback.on_next(TRY_AGAIN)
                else:
                    callback.on_next(GAME_OVER)
                    self._audio_service.play_sound(over_sound)   