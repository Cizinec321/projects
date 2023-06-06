from .models import in_form, tables, models, invitees,invitees_x_table
from django.contrib.auth import get_user_model

def gen_text(in_val):
    return {
        'about': (
            '<div style="width:800px;left:30vw;overflow=auto;">'
            '<p style="font-size:17px; position: relative;margin-right: 2em;margin-left: 2em;background: rgba(255, 255, 255, 0.7); margin-top: 10em; margin-bottom: 0em; text-align: left;"><b>About us and our journey</b><br><br>'


               "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
               "<br><br>"
               "Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum[d] exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? [D]Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur? [33] At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."
              
               "</p>"
            '</div>'  
                ),
        'edu': (
            '<div style="width:800px;left:30vw;overflow=auto;">'
            '<p style="font-size:17px; position: relative;margin-right: 2em;margin-left: 2em;background: rgba(255, 255, 255, 0.7); margin-top: 10em; margin-bottom: 0em; text-align: left;"><b>About you and your participation</b><br><br>'


               "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
               "<br><br>"
               "Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum[d] exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? [D]Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur? [33] At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."
              
            "</p>"
            '</div>'
        ),








        'contact':(
            '<p style="font-size:17px; position: relative;margin-right: 2em;margin-left: 2em; margin-top: 5em; margin-bottom: 0em; text-align: left;"><b>Contact</b><br><br><br>'

            "<b>Email:</b> velich.eduard@gmail.com<br>"

       

        )
    }[in_val]

def get_party_list(table_id,setting_id):

    query_res=invitees_x_table.objects.filter(table_id=table_id,setting_name=setting_id)
    outval='<table style="top: 5%;position: relative;"><tbody><tr><th style="text-align: left;"><label >Seated invitees:<br><br></label></th></tr>'
    for x in  query_res:
        outval=outval+'<tr><th style="text-align: left;"><label >'+str(x.r_name)+'</label></th></tr>'
    outval=outval+'</tbody></table>'
    return outval
def get_party_names(table_id,setting_id):

    query_res=invitees_x_table.objects.filter(table_id=table_id,setting_name=setting_id)
    outval='<table style="top: 5%;position: relative;"><tbody><tr><th style="text-align: left;"><label >Seated invitees:<br><br></label></th></tr>'
    for x in  query_res:
        outval=outval+'<tr><th style="text-align: left;"><label >'+str(x.name)+'</label></th></tr>'
    outval=outval+'</tbody></table>'
    return outval

def get_party_full():
    User = get_user_model()
    users = User.objects.all()
    outval='<table style="top: 5%;position: relative; table-layout: fixed ; width: 100%; "><tbody>'
    for x in  users:
        if str(x.username)!='CP8FYQAILLSI':
            query_res=invitees.objects.filter(name__startswith=str(x.username)).count()  
            party_res=invitees.objects.filter(name__startswith=str(x.username),particpation='Yes').count()    
            outval=outval+'<tr><th style="text-align: left;"><label >'+str(x.username)+'</label></th>'+'<th style="text-align: left;"><label >'+str(query_res)+' Seats</label></th>'+'<th style="text-align: left;"><label >'+str(party_res)+' Participants</label></th>'+'<th style="text-align: left;"><form method="POST"><button type="submit" name="delete_participant" value="'+str(x.username)+'" class="pos_button2">Delete</button><form></th>'+'<th style="text-align: left;"><form method="POST"><button type="submit" name="edit_participant" value="'+str(x.username)+'" class="pos_button2">Details</button><form></th></tr>'
    outval=outval+'</tbody></table>'
    return outval

