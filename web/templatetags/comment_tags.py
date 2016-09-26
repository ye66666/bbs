#coding:utf-8



from django import template


register = template.Library()


def search_tree(d_dic,c_obj):
    for k,v_dic in d_dic.items():
        if k == c_obj.parent_comment:
            d_dic[k][c_obj] = {}
            return
        else:
            search_tree(d_dic[k],c_obj)

def child_generate_comment_html(sub_coment_dic,margin_val):
    html = ''
    for k,v_dic in sub_coment_dic.items():
        html += "<div style='margin-left: %spx' class='comment-node'>"% margin_val+str(k.user)+":&nbsp;&nbsp;"+ k.comment + "</div>"
        if v_dic:
            html += child_generate_comment_html(v_dic,margin_val+15)
    return html

@register.simple_tag()
def comment_tree_tag(comment_list):
    # print "comment info:",comment_list

    comment_dic = {}

    for comment_obj in comment_list:
        if comment_obj.parent_comment is None:
            comment_dic[comment_obj] = {}
        else:
            search_tree(comment_dic,comment_obj)

    html = "<div class='comment-box'>"
    margin_left = 0
    for k,v in comment_dic.items():
        # print type(k),type(k.user),type(k.comment),str(k.user)

        html += "<div class='comment-node'>"+str(k.user)+":&nbsp;&nbsp;"+ k.comment + "</div>"
        html += child_generate_comment_html(v,margin_left+15)

    html += "</div>"
    return html

