

from distutils.log import Log
from app.models.BD.Category import Category
from app.models.BD.Status import Status
from app.models.BD.Bid import Bid
from app.models.BD.User import User
from sqlalchemy import Float,Column,Integer,String,ForeignKey,DateTime,Time,Boolean,Date
from sqlalchemy import or_, and_
from sqlalchemy import cast

def getQuery(k,v,obj,idx=0,ret=[]):
    classes = {"User":User,"Log":Log,"Bid":Bid,"Status":Status,"Category":Category}
    if "." in k:
        ks = k.split(".",1)
        property = getattr(obj, ks[0]).has
        gq = getQuery(ks[1],v,classes[ks[0]],idx+1)
        return [property(and_(*gq))]
    else:
        if k[0].isupper():
            return [getattr(obj, k) == v]

        if getattr(obj, k).expression.type.__str__() == "BOOLEAN":
            v = 1 if v else 0
            return [getattr(obj, k).like(f"{v}")]
        # if k[0].isupper():
        #     return getattr(obj, k).is_(v)
        if getattr(obj, k).expression.type.__str__() == "INTEGER":
         
            if v is None:
                return [getattr(obj, k).is_(v)]
            else:
                return [getattr(obj, k).like(v)]

        if getattr(obj, k).expression.type.__str__() == "DATETIME":
            qr = []
            
            MAI = lambda v:cast(getattr(obj, k),Date) >= v
            MEI = lambda v:cast(getattr(obj, k),Date) <= v
            I   = lambda v:cast(getattr(obj, k),Date) == v
            ME  = lambda v:cast(getattr(obj, k),Date) < v
            MA  = lambda v:cast(getattr(obj, k),Date) > v
            K   = {"<=":MEI,">=":MAI,"=":I,"<":ME,">":MA}

            if v is None:
                return [getattr(obj, k).is_(v)]

            for cond in v:
                qr.append(K[cond["operator"]](cond["value"]))

            return qr

        return [getattr(obj, k).like(f"{v}")]