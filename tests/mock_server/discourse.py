from flask import Blueprint, jsonify

discourse = Blueprint("discourse", __name__)


@discourse.route("/")
def healthcheck():
    return "Ok"


@discourse.route("/latest.json", methods=["GET"])
def latest():
    response = {
        "users": [
            {
                "id": -1,
                "username": "system",
                "name": "system",
                "avatar_template": "/images/discourse-logo-sketch-small.png",
                "admin": True,
                "moderator": True,
                "trust_level": 4,
            }
        ],
        "primary_groups": [],
        "topic_list": {
            "can_create_topic": True,
            "per_page": 30,
            "top_tags": [],
            "topics": [
                {
                    "id": 7,
                    "title": "Welcome to Discourse",
                    "fancy_title": "Welcome to Discourse",
                    "slug": "welcome-to-discourse",
                    "posts_count": 1,
                    "reply_count": 0,
                    "highest_post_number": 1,
                    "image_url": None,
                    "created_at": "2021-05-25T13:18:37.926Z",
                    "last_posted_at": "2021-05-25T13:18:38.057Z",
                    "bumped": True,
                    "bumped_at": "2021-05-25T13:18:38.057Z",
                    "archetype": "regular",
                    "unseen": False,
                    "pinned": True,
                    "unpinned": None,
                    "excerpt": "The first paragraph of this pinned topic will be visible as a welcome message to all new visitors on your homepage. It’s important! \nEdit this into a brief description of your community: \n\nWho is it for?\nWhat can they fi&hellip;",
                    "visible": True,
                    "closed": False,
                    "archived": False,
                    "bookmarked": None,
                    "liked": None,
                    "tags": [],
                    "views": 0,
                    "like_count": 0,
                    "has_summary": False,
                    "last_poster_username": "system",
                    "category_id": 1,
                    "pinned_globally": True,
                    "featured_link": None,
                    "posters": [
                        {
                            "extras": "latest single",
                            "description": "Original Poster, Most Recent Poster",
                            "user_id": -1,
                            "primary_group_id": None,
                        }
                    ],
                },
                {
                    "id": 9,
                    "title": "READ ME FIRST: Admin Quick Start Guide",
                    "fancy_title": "READ ME FIRST: Admin Quick Start Guide",
                    "slug": "read-me-first-admin-quick-start-guide",
                    "posts_count": 1,
                    "reply_count": 0,
                    "highest_post_number": 1,
                    "image_url": None,
                    "created_at": "2021-05-25T13:18:38.468Z",
                    "last_posted_at": "2021-05-25T13:18:38.589Z",
                    "bumped": True,
                    "bumped_at": "2021-05-25T13:18:38.589Z",
                    "archetype": "regular",
                    "unseen": False,
                    "last_read_post_number": 1,
                    "unread": 0,
                    "new_posts": 0,
                    "pinned": False,
                    "unpinned": None,
                    "visible": True,
                    "closed": False,
                    "archived": False,
                    "notification_level": 1,
                    "bookmarked": False,
                    "liked": False,
                    "tags": [],
                    "views": 1,
                    "like_count": 0,
                    "has_summary": False,
                    "last_poster_username": "system",
                    "category_id": 3,
                    "pinned_globally": False,
                    "featured_link": None,
                    "posters": [
                        {
                            "extras": "latest single",
                            "description": "Original Poster, Most Recent Poster",
                            "user_id": -1,
                            "primary_group_id": None,
                        }
                    ],
                },
                {
                    "id": 8,
                    "title": "Welcome to the Lounge",
                    "fancy_title": "Welcome to the Lounge",
                    "slug": "welcome-to-the-lounge",
                    "posts_count": 1,
                    "reply_count": 0,
                    "highest_post_number": 1,
                    "image_url": None,
                    "created_at": "2021-05-25T13:18:38.148Z",
                    "last_posted_at": "2021-05-25T13:18:38.294Z",
                    "bumped": True,
                    "bumped_at": "2021-05-25T13:18:38.294Z",
                    "archetype": "regular",
                    "unseen": False,
                    "pinned": True,
                    "unpinned": None,
                    "excerpt": "Congratulations! :confetti_ball: \nIf you can see this topic, you were recently promoted to regular (trust level 3). \nYou can now … \n\nEdit the title of any topic\nChange the category of any topic\nHave all your links follow&hellip;",
                    "visible": True,
                    "closed": False,
                    "archived": False,
                    "bookmarked": None,
                    "liked": None,
                    "tags": [],
                    "views": 0,
                    "like_count": 0,
                    "has_summary": False,
                    "last_poster_username": "system",
                    "category_id": 4,
                    "pinned_globally": False,
                    "featured_link": None,
                    "posters": [
                        {
                            "extras": "latest single",
                            "description": "Original Poster, Most Recent Poster",
                            "user_id": -1,
                            "primary_group_id": None,
                        }
                    ],
                },
                {
                    "id": 6,
                    "title": "Privacy Policy",
                    "fancy_title": "Privacy Policy",
                    "slug": "privacy-policy",
                    "posts_count": 2,
                    "reply_count": 0,
                    "highest_post_number": 2,
                    "image_url": None,
                    "created_at": "2021-05-25T13:18:37.230Z",
                    "last_posted_at": "2021-05-25T13:18:37.737Z",
                    "bumped": True,
                    "bumped_at": "2021-05-25T13:18:37.737Z",
                    "archetype": "regular",
                    "unseen": False,
                    "pinned": False,
                    "unpinned": None,
                    "visible": True,
                    "closed": False,
                    "archived": False,
                    "bookmarked": None,
                    "liked": None,
                    "tags": [],
                    "views": 0,
                    "like_count": 0,
                    "has_summary": False,
                    "last_poster_username": "system",
                    "category_id": 3,
                    "pinned_globally": False,
                    "featured_link": None,
                    "posters": [
                        {
                            "extras": "latest single",
                            "description": "Original Poster, Most Recent Poster",
                            "user_id": -1,
                            "primary_group_id": None,
                        }
                    ],
                },
                {
                    "id": 5,
                    "title": "FAQ/Guidelines",
                    "fancy_title": "FAQ/Guidelines",
                    "slug": "faq-guidelines",
                    "posts_count": 2,
                    "reply_count": 0,
                    "highest_post_number": 2,
                    "image_url": None,
                    "created_at": "2021-05-25T13:18:36.731Z",
                    "last_posted_at": "2021-05-25T13:18:37.061Z",
                    "bumped": True,
                    "bumped_at": "2021-05-25T13:18:37.061Z",
                    "archetype": "regular",
                    "unseen": False,
                    "pinned": False,
                    "unpinned": None,
                    "visible": True,
                    "closed": False,
                    "archived": False,
                    "bookmarked": None,
                    "liked": None,
                    "tags": [],
                    "views": 0,
                    "like_count": 0,
                    "has_summary": False,
                    "last_poster_username": "system",
                    "category_id": 3,
                    "pinned_globally": False,
                    "featured_link": None,
                    "posters": [
                        {
                            "extras": "latest single",
                            "description": "Original Poster, Most Recent Poster",
                            "user_id": -1,
                            "primary_group_id": None,
                        }
                    ],
                },
                {
                    "id": 4,
                    "title": "Terms of Service",
                    "fancy_title": "Terms of Service",
                    "slug": "terms-of-service",
                    "posts_count": 2,
                    "reply_count": 0,
                    "highest_post_number": 2,
                    "image_url": None,
                    "created_at": "2021-05-25T13:18:35.998Z",
                    "last_posted_at": "2021-05-25T13:18:36.580Z",
                    "bumped": True,
                    "bumped_at": "2021-05-25T13:18:36.580Z",
                    "archetype": "regular",
                    "unseen": False,
                    "pinned": False,
                    "unpinned": None,
                    "visible": True,
                    "closed": False,
                    "archived": False,
                    "bookmarked": None,
                    "liked": None,
                    "tags": [],
                    "views": 0,
                    "like_count": 0,
                    "has_summary": False,
                    "last_poster_username": "system",
                    "category_id": 3,
                    "pinned_globally": False,
                    "featured_link": None,
                    "posters": [
                        {
                            "extras": "latest single",
                            "description": "Original Poster, Most Recent Poster",
                            "user_id": -1,
                            "primary_group_id": None,
                        }
                    ],
                },
            ],
        },
    }
    return jsonify(response), 200


@discourse.route("/admin/users/<user_id>/log_out.json", methods=["POST"])
def log_out_user(user_id):
    response = {"success": "OK"}
    return jsonify(response), 200


@discourse.route("/admin/site_settings.json", methods=["GET"])
def get_site_settings():
    response = {
        "site_settings": [
            {
                "setting": "default_locale",
                "default": "en",
                "category": "required",
                "description": "The default language of this Discourse instance. You can replace the text of system generated categories and topics at <a href='/admin/customize/site_texts' target='_blank'>Customize / Text</a>.",
                "type": "enum",
                "preview": None,
                "value": "en",
                "valid_values": [
                    {"name": "اللغة العربية", "value": "ar"},
                    {"name": "беларуская мова", "value": "be"},
                    {"name": "български език", "value": "bg"},
                    {"name": "bosanski jezik", "value": "bs_BA"},
                    {"name": "català", "value": "ca"},
                    {"name": "čeština", "value": "cs"},
                    {"name": "dansk", "value": "da"},
                    {"name": "Deutsch", "value": "de"},
                    {"name": "ελληνικά", "value": "el"},
                    {"name": "English (US)", "value": "en"},
                    {"name": "English (UK)", "value": "en_GB"},
                    {"name": "Español", "value": "es"},
                    {"name": "eesti", "value": "et"},
                    {"name": "فارسی", "value": "fa_IR"},
                    {"name": "suomi", "value": "fi"},
                    {"name": "Français", "value": "fr"},
                    {"name": "galego", "value": "gl"},
                    {"name": "עברית", "value": "he"},
                    {"name": "magyar", "value": "hu"},
                    {"name": "Հայերեն", "value": "hy"},
                    {"name": "Indonesian", "value": "id"},
                    {"name": "Italiano", "value": "it"},
                    {"name": "日本語", "value": "ja"},
                    {"name": "한국어", "value": "ko"},
                    {"name": "lietuvių kalba", "value": "lt"},
                    {"name": "latviešu valoda", "value": "lv"},
                    {"name": "Norsk bokmål", "value": "nb_NO"},
                    {"name": "Nederlands", "value": "nl"},
                    {"name": "polski", "value": "pl_PL"},
                    {"name": "Português", "value": "pt"},
                    {"name": "Português (BR)", "value": "pt_BR"},
                    {"name": "limba română", "value": "ro"},
                    {"name": "Русский", "value": "ru"},
                    {"name": "slovenčina", "value": "sk"},
                    {"name": "slovenščina", "value": "sl"},
                    {"name": "Shqip", "value": "sq"},
                    {"name": "српски језик", "value": "sr"},
                    {"name": "svenska", "value": "sv"},
                    {"name": "Kiswahili", "value": "sw"},
                    {"name": "తెలుగు", "value": "te"},
                    {"name": "ไทย", "value": "th"},
                    {"name": "Türkçe", "value": "tr_TR"},
                    {"name": "українська мова", "value": "uk"},
                    {"name": "اردو", "value": "ur"},
                    {"name": "Việt Nam", "value": "vi"},
                    {"name": "中文", "value": "zh_CN"},
                    {"name": "中文 (TW)", "value": "zh_TW"},
                ],
                "translate_names": False,
            },
            {
                "setting": "title",
                "description": "The name of this site, as used in the title tag.",
                "default": "Discourse",
                "value": "Grayden's Discourse",
                "category": "required",
                "preview": None,
                "secret": False,
                "placeholder": None,
                "type": "string",
            },
        ]
    }
    return jsonify(response), 200


@discourse.route("/admin/site_settings/title", methods=["PUT"])
def update_site_settings():
    return "", 200


@discourse.route("/admin/groups.json", methods=["POST"])
def create_a_group():
    response = {
        "basic_group": {
            "id": 50,
            "automatic": False,
            "name": "0c508ffab7d042d8",
            "user_count": 0,
            "mentionable_level": 0,
            "messageable_level": 0,
            "visibility_level": 0,
            "primary_group": False,
            "title": None,
            "grant_trust_level": None,
            "incoming_email": None,
            "has_messages": False,
            "flair_url": None,
            "flair_bg_color": None,
            "flair_color": None,
            "bio_raw": None,
            "bio_cooked": None,
            "bio_excerpt": None,
            "public_admission": False,
            "public_exit": False,
            "allow_membership_requests": False,
            "full_name": None,
            "default_notification_level": 3,
            "membership_request_template": None,
            "members_visibility_level": 0,
            "can_see_members": True,
            "can_admin_group": True,
            "publish_read_state": False,
        }
    }
    return jsonify(response), 200


@discourse.route("/admin/groups/<group_id>.json", methods=["DELETE"])
def delete_a_group(group_id):
    response = {"success": "OK"}
    return jsonify(response), 200
