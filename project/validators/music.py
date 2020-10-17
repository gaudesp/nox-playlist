import os
from flask import flash, request
from project.models.music import Music
from project.services.urllib import check_link
from project.services.youtube import get_video, get_title

class MusicValidator(object):
  def on_create(self):
    if request.form:
      if request.form["link"]:
        if "youtu" in request.form["link"]:
          # if check_link(request.form["link"]):
            if not Music().fetch_by_video(get_video(request.form["link"])):
              Music().insert_all(get_video(request.form["link"]), get_title(request.form["link"]))
              flash("La musique a bien été ajouté dans la playlist", "success")
              return True
            else:
              flash("Cette musique a déjà été ajouté dans la playlist", "danger")
          # else:
          #   flash("Le lien de la musique est invalide", "danger")
        else:
          flash("Vous devez renseigner un lien YouTube", "danger")
      else:
        flash("Vous devez renseigner le lien d'une musique", "danger")
    return False