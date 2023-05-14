from sqlalchemy import update

from app.database import session, Region, User


def switch_air_alert_of(region_name, isAlert):
    user = session.query(Region).filter(Region.name == region_name).first()
    user.isAlert = isAlert
    session.commit()


def get_list_of_region():
    regions = session.query(Region).all()
    regions_dict = dict()
    for i in regions:
        regions_dict[i.name] = i.isAlert
    return regions_dict

