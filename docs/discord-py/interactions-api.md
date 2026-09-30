---
source: https://discordpy.readthedocs.io/en/stable/interactions/api.html
version: stable (terbaru, discord.py 2.7.1 per PyPI per 2026-09-30 14:07 UTC)
downloaded: 2026-09-30 14:07 UTC
format: markdown (konversi dari HTML dokumentasi)
---

View Documentation For discord discord.ext.commands discord.ext.tasks

search

settings

menu settings

search

### [Table of Contents](https://discordpy.readthedocs.io/en/stable/index.html)

- Interactions API Reference
  - [Models](#models)
    - [Interaction](#interaction)
    - [InteractionResponse](#interactionresponse)
    - [InteractionCallbackResponse](#interactioncallbackresponse)
    - [InteractionCallbackActivityInstance](#interactioncallbackactivityinstance)
    - [InteractionMessage](#interactionmessage)
    - [MessageInteraction](#messageinteraction)
    - [MessageInteractionMetadata](#messageinteractionmetadata)
    - [Component](#component)
    - [ActionRow](#actionrow)
    - [Button](#button)
    - [SelectMenu](#selectmenu)
    - [TextInput](#textinput)
    - [LabelComponent](#labelcomponent)
    - [SectionComponent](#sectioncomponent)
    - [ThumbnailComponent](#thumbnailcomponent)
    - [TextDisplay](#textdisplay)
    - [MediaGalleryComponent](#mediagallerycomponent)
    - [FileComponent](#filecomponent)
    - [SeparatorComponent](#separatorcomponent)
    - [Container](#container)
    - [FileUploadComponent](#fileuploadcomponent)
    - [RadioGroupComponent](#radiogroupcomponent)
    - [CheckboxComponent](#checkboxcomponent)
    - [CheckboxGroupComponent](#checkboxgroupcomponent)
    - [AppCommand](#appcommand)
    - [AppCommandGroup](#appcommandgroup)
    - [AppCommandChannel](#appcommandchannel)
    - [AppCommandThread](#appcommandthread)
    - [AppCommandPermissions](#appcommandpermissions)
    - [AppCommandContext](#appcommandcontext)
    - [AppInstallationType](#appinstallationtype)
    - [GuildAppCommandPermissions](#guildappcommandpermissions)
    - [Argument](#argument)
    - [AllChannels](#allchannels)
  - [Data Classes](#data-classes)
    - [SelectOption](#selectoption)
    - [SelectDefaultValue](#selectdefaultvalue)
    - [Choice](#choice)
    - [UnfurledMediaItem](#unfurledmediaitem)
    - [MediaGalleryItem](#mediagalleryitem)
    - [RadioGroupOption](#radiogroupoption)
    - [CheckboxGroupOption](#checkboxgroupoption)
  - [Enumerations](#enumerations)
  - [Bot UI Kit](#bot-ui-kit)
    - [View](#view)
    - [LayoutView](#layoutview)
    - [Modal](#modal)
    - [Item](#item)
    - [DynamicItem](#dynamicitem)
    - [Button](#id1)
    - [Select Menus](#select-menus)
      - [Select](#select)
      - [ChannelSelect](#channelselect)
      - [RoleSelect](#roleselect)
      - [MentionableSelect](#mentionableselect)
      - [UserSelect](#userselect)
      - [select](#id2)
    - [TextInput](#id3)
    - [Container](#id4)
    - [File](#file)
    - [Label](#label)
    - [MediaGallery](#mediagallery)
    - [Section](#section)
    - [Separator](#separator)
    - [TextDisplay](#id5)
    - [Thumbnail](#thumbnail)
    - [ActionRow](#id6)
    - [FileUpload](#fileupload)
    - [RadioGroup](#radiogroup)
    - [Checkbox](#checkbox)
    - [CheckboxGroup](#checkboxgroup)
  - [Application Commands](#application-commands)
    - [CommandTree](#commandtree)
    - [Commands](#commands)
      - [Command](#command)
      - [Parameter](#parameter)
      - [ContextMenu](#contextmenu)
      - [Group](#group)
    - [Decorators](#decorators)
    - [Checks](#checks)
    - [Cooldown](#cooldown)
    - [Namespace](#namespace)
    - [Transformers](#transformers)
      - [Transformer](#transformer)
      - [Transform](#transform)
      - [Range](#range)
      - [Timestamp](#timestamp)
    - [Translations](#translations)
      - [Translator](#translator)
      - [locale\_str](#locale-str)
      - [TranslationContext](#translationcontext)
      - [TranslationContextLocation](#translationcontextlocation)
    - [Exceptions](#exceptions)
      - [Exception Hierarchy](#exception-hierarchy)

# Interactions API Reference ¶

The following section outlines the API of interactions, as implemented by the library.

For documentation about the rest of the library, check [API Reference](https://discordpy.readthedocs.io/en/stable/api.html).

## Models ¶

Similar to [Discord Models](https://discordpy.readthedocs.io/en/stable/api.html#discord-api-models), these are not meant to be constructed by the user.

### Interaction ¶

Attributes

- [app\_permissions](#discord.Interaction.app_permissions)
- [application\_id](#discord.Interaction.application_id)
- [channel](#discord.Interaction.channel)
- [channel\_id](#discord.Interaction.channel_id)
- [client](#discord.Interaction.client)
- [command](#discord.Interaction.command)
- [command\_failed](#discord.Interaction.command_failed)
- [command\_id](#discord.Interaction.command_id)
- [context](#discord.Interaction.context)
- [created\_at](#discord.Interaction.created_at)
- [custom\_id](#discord.Interaction.custom_id)
- [data](#discord.Interaction.data)
- [entitlement\_sku\_ids](#discord.Interaction.entitlement_sku_ids)
- [entitlements](#discord.Interaction.entitlements)
- [expires\_at](#discord.Interaction.expires_at)
- [extras](#discord.Interaction.extras)
- [filesize\_limit](#discord.Interaction.filesize_limit)
- [followup](#discord.Interaction.followup)
- [guild](#discord.Interaction.guild)
- [guild\_id](#discord.Interaction.guild_id)
- [guild\_locale](#discord.Interaction.guild_locale)
- [id](#discord.Interaction.id)
- [locale](#discord.Interaction.locale)
- [message](#discord.Interaction.message)
- [namespace](#discord.Interaction.namespace)
- [permissions](#discord.Interaction.permissions)
- [response](#discord.Interaction.response)
- [token](#discord.Interaction.token)
- [type](#discord.Interaction.type)
- [user](#discord.Interaction.user)

Methods

- async [delete\_original\_response](#discord.Interaction.delete_original_response)
- async [edit\_original\_response](#discord.Interaction.edit_original_response)
- def [is\_expired](#discord.Interaction.is_expired)
- def [is\_guild\_integration](#discord.Interaction.is_guild_integration)
- def [is\_user\_integration](#discord.Interaction.is_user_integration)
- async [original\_response](#discord.Interaction.original_response)
- async [translate](#discord.Interaction.translate)

<dl><dt>*class*discord.Interaction<a href="#discord.Interaction" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a Discord interaction.

An interaction happens when a user does an action that needs to be notified. Current examples are slash commands and components.

New in version 2.0.

<dl><dt>id<a href="#discord.Interaction.id" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction’s ID.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.Interaction.type" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction type.

<dl><dt>Type</dt>
<dd>

<a href="#discord.InteractionType" title="discord.InteractionType"><code>InteractionType</code></a>

</dd></dl></dd>
</dl><dl><dt>guild_id<a href="#discord.Interaction.guild_id" title="Permalink to this definition">¶</a></dt>
<dd>

The guild ID the interaction was sent from.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>channel<a href="#discord.Interaction.channel" title="Permalink to this definition">¶</a></dt>
<dd>

The channel the interaction was sent from.

Note that due to a Discord limitation, if sent from a DM channel <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.DMChannel.recipient" title="discord.DMChannel.recipient"><code>recipient</code></a> is <code>None</code>.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.PrivateChannel" title="discord.abc.PrivateChannel"><code>abc.PrivateChannel</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a>]]

</dd></dl></dd>
</dl><dl><dt>entitlement_sku_ids<a href="#discord.Interaction.entitlement_sku_ids" title="Permalink to this definition">¶</a></dt>
<dd>

The entitlement SKU IDs that the user has.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>entitlements<a href="#discord.Interaction.entitlements" title="Permalink to this definition">¶</a></dt>
<dd>

The entitlements that the guild or user has.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Entitlement" title="discord.Entitlement"><code>Entitlement</code></a>]

</dd></dl></dd>
</dl><dl><dt>application_id<a href="#discord.Interaction.application_id" title="Permalink to this definition">¶</a></dt>
<dd>

The application ID that the interaction was for.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>user<a href="#discord.Interaction.user" title="Permalink to this definition">¶</a></dt>
<dd>

The user or member that sent the interaction.

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a>]

</dd></dl></dd>
</dl><dl><dt>message<a href="#discord.Interaction.message" title="Permalink to this definition">¶</a></dt>
<dd>

The message that sent this interaction.

This is only available for <a href="#discord.InteractionType.component" title="discord.InteractionType.component"><code>InteractionType.component</code></a> interactions.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>]

</dd></dl></dd>
</dl><dl><dt>token<a href="#discord.Interaction.token" title="Permalink to this definition">¶</a></dt>
<dd>

The token to continue the interaction. These are valid for 15 minutes.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>data<a href="#discord.Interaction.data" title="Permalink to this definition">¶</a></dt>
<dd>

The raw interaction data.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

</dd></dl></dd>
</dl><dl><dt>locale<a href="#discord.Interaction.locale" title="Permalink to this definition">¶</a></dt>
<dd>

The locale of the user invoking the interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>

</dd></dl></dd>
</dl><dl><dt>guild_locale<a href="#discord.Interaction.guild_locale" title="Permalink to this definition">¶</a></dt>
<dd>

The preferred locale of the guild the interaction was sent from, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>]

</dd></dl></dd>
</dl><dl><dt>extras<a href="#discord.Interaction.extras" title="Permalink to this definition">¶</a></dt>
<dd>

A dictionary that can be used to store extraneous data for use during interaction processing. The library will not touch any values or keys within this dictionary.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

</dd></dl></dd>
</dl><dl><dt>command_failed<a href="#discord.Interaction.command_failed" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the command associated with this interaction failed to execute. This includes checks and execution.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>context<a href="#discord.Interaction.context" title="Permalink to this definition">¶</a></dt>
<dd>

The context of the interaction.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

<a href="#discord.app_commands.AppCommandContext" title="discord.app_commands.AppCommandContext"><code>AppCommandContext</code></a>

</dd></dl></dd>
</dl><dl><dt>filesize_limit<a href="#discord.Interaction.filesize_limit" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of bytes a file can have when responding to this interaction.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)">int</a>

</dd></dl></dd>
</dl><dl><dt>*property*client<a href="#discord.Interaction.client" title="Permalink to this definition">¶</a></dt>
<dd>

The client that is handling this interaction.

Note that <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AutoShardedClient" title="discord.AutoShardedClient"><code>AutoShardedClient</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot" title="discord.ext.commands.Bot"><code>Bot</code></a>, and <a href="https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.AutoShardedBot" title="discord.ext.commands.AutoShardedBot"><code>AutoShardedBot</code></a> are all subclasses of client.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client" title="discord.Client"><code>Client</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*guild<a href="#discord.Interaction.guild" title="Permalink to this definition">¶</a></dt>
<dd>

The guild the interaction was sent from.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*channel_id<a href="#discord.Interaction.channel_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the channel the interaction was sent from.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*permissions<a href="#discord.Interaction.permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The resolved permissions of the member in the channel, including overwrites.

In a non-guild context where this doesn’t apply, an empty permissions object is returned.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*app_permissions<a href="#discord.Interaction.app_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The resolved permissions of the application or the bot, including overwrites.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>

</dd></dl></dd>
</dl><dl><dt>namespace<a href="#discord.Interaction.namespace" title="Permalink to this definition">¶</a></dt>
<dd>

The resolved namespace for this interaction.

If the interaction is not an application command related interaction or the client does not have a tree attached to it then this returns an empty namespace.

<dl><dt>Type</dt>
<dd>

<a href="#discord.app_commands.Namespace" title="discord.app_commands.Namespace"><code>app_commands.Namespace</code></a>

</dd></dl></dd>
</dl><dl><dt>command<a href="#discord.Interaction.command" title="Permalink to this definition">¶</a></dt>
<dd>

The command being called from this interaction.

If the interaction is not an application command related interaction or the command is not found in the client’s attached tree then <code>None</code> is returned.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>app_commands.Command</code></a>, <a href="#discord.app_commands.ContextMenu" title="discord.app_commands.ContextMenu"><code>app_commands.ContextMenu</code></a>]]

</dd></dl></dd>
</dl><dl><dt>command_id<a href="#discord.Interaction.command_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the command that triggered this interaction.

Only applicable if <a href="#discord.Interaction.type" title="discord.Interaction.type"><code>type</code></a> is one of, <a href="#discord.InteractionType.application_command" title="discord.InteractionType.application_command"><code>InteractionType.application_command</code></a> or <a href="#discord.InteractionType.autocomplete" title="discord.InteractionType.autocomplete"><code>InteractionType.autocomplete</code></a>.

New in version 2.7.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>response<a href="#discord.Interaction.response" title="Permalink to this definition">¶</a></dt>
<dd>

Returns an object responsible for handling responding to the interaction.

A response can only be done once. If secondary messages need to be sent, consider using <a href="#discord.Interaction.followup" title="discord.Interaction.followup"><code>followup</code></a> instead.

<dl><dt>Type</dt>
<dd>

<a href="#discord.InteractionResponse" title="discord.InteractionResponse"><code>InteractionResponse</code></a>

</dd></dl></dd>
</dl><dl><dt>followup<a href="#discord.Interaction.followup" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the follow up webhook for follow up interactions.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Webhook" title="discord.Webhook"><code>Webhook</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*created_at<a href="#discord.Interaction.created_at" title="Permalink to this definition">¶</a></dt>
<dd>

When the interaction was created.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*expires_at<a href="#discord.Interaction.expires_at" title="Permalink to this definition">¶</a></dt>
<dd>

When the interaction expires.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>

</dd></dl></dd>
</dl><dl><dt>custom_id<a href="#discord.Interaction.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The custom ID of the component that triggered this interaction.

Only applicable if <a href="#discord.Interaction.type" title="discord.Interaction.type"><code>type</code></a> is one of, <a href="#discord.InteractionType.component" title="discord.InteractionType.component"><code>InteractionType.component</code></a> or <a href="#discord.InteractionType.modal_submit" title="discord.InteractionType.modal_submit"><code>InteractionType.modal_submit</code></a>.

New in version 2.7.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>is_expired()<a href="#discord.Interaction.is_expired" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Returns <code>True</code> if the interaction is expired.

</dd></dl><dl><dt>is_guild_integration()<a href="#discord.Interaction.is_guild_integration" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Returns <code>True</code> if the interaction is a guild integration.

New in version 2.4.

</dd></dl><dl><dt>is_user_integration()<a href="#discord.Interaction.is_user_integration" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Returns <code>True</code> if the interaction is a user integration.

New in version 2.4.

</dd></dl><dl><dt>*await* original_response()<a href="#discord.Interaction.original_response" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Fetches the original interaction response message associated with the interaction.

If the interaction response was a newly created message (i.e. through <a href="#discord.InteractionResponse.send_message" title="discord.InteractionResponse.send_message"><code>InteractionResponse.send_message()</code></a> or <a href="#discord.InteractionResponse.defer" title="discord.InteractionResponse.defer"><code>InteractionResponse.defer()</code></a>, where <code>thinking</code> is <code>True</code>) then this returns the message that was sent using that response. Otherwise, this returns the message that triggered the interaction (i.e. through a component).

Repeated calls to this will return a cached value.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Fetching the original response message failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientException" title="discord.ClientException">**ClientException**</a> – The channel for the message could not be resolved.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The interaction response message does not exist.

</dd><dt>Returns</dt>
<dd>

The original interaction response message.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.InteractionMessage" title="discord.InteractionMessage">InteractionMessage</a>

</dd></dl></dd>
</dl><dl><dt>*await* edit_original_response(***, *content=...*, *embeds=...*, *embed=...*, *attachments=...*, *view=...*, *allowed_mentions=None*, *poll=...*)<a href="#discord.Interaction.edit_original_response" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Edits the original interaction response message.

This is a lower level interface to <a href="#discord.InteractionMessage.edit" title="discord.InteractionMessage.edit"><code>InteractionMessage.edit()</code></a> in case you do not want to fetch the message and save an HTTP request.

This method is also the only way to edit the original message if the message sent was ephemeral.

<dl><dt>Parameters</dt>
<dd>

- **content** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The content to edit the message with or <code>None</code> to clear it.
- **embeds** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed" title="discord.Embed"><code>Embed</code></a>]) – A list of embeds to edit the message with.
- **embed** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed" title="discord.Embed"><code>Embed</code></a>]) – The embed to edit the message with. <code>None</code> suppresses the embeds. This should not be mixed with the <code>embeds</code> parameter.
- **attachments** (List\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Attachment" title="discord.Attachment"><code>Attachment</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>File</code></a>]]) –

  A list of attachments to keep in the message as well as new files to upload. If <code>[]</code> is passed then all attachments are removed.

  Note

  New files will always appear after current attachments.
- **allowed\_mentions** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AllowedMentions" title="discord.AllowedMentions"><code>AllowedMentions</code></a>) – Controls the mentions being processed in this message. See <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable.send" title="discord.abc.Messageable.send"><code>abc.Messageable.send()</code></a> for more information.
- **view** (Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]) –

  The updated view to update this message with. If <code>None</code> is passed then the view is removed.

  Note

  If you want to update the message to have a <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>, you must explicitly set the <code>content</code>, <code>embed</code>, <code>embeds</code>, and <code>attachments</code> parameters to <code>None</code> if the previous message had any.
- **poll** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Poll" title="discord.Poll"><code>Poll</code></a>) –

  The poll to create when editing the message.

  New in version 2.5.

  Note

  This is only accepted when the response type is <a href="#discord.InteractionResponseType.deferred_channel_message" title="discord.InteractionResponseType.deferred_channel_message"><code>InteractionResponseType.deferred_channel_message</code></a>.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Editing the message failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The interaction response message does not exist.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – Edited a message that is not yours.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – You specified both <code>embed</code> and <code>embeds</code>
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The length of <code>embeds</code> was invalid.

</dd><dt>Returns</dt>
<dd>

The newly edited message.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.InteractionMessage" title="discord.InteractionMessage"><code>InteractionMessage</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* delete_original_response()<a href="#discord.Interaction.delete_original_response" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Deletes the original interaction response message.

This is a lower level interface to <a href="#discord.InteractionMessage.delete" title="discord.InteractionMessage.delete"><code>InteractionMessage.delete()</code></a> in case you do not want to fetch the message and save an HTTP request.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Deleting the message failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The interaction response message does not exist or has already been deleted.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – Deleted a message that is not yours.

</dd></dl></dd>
</dl><dl><dt>*await* translate(*string*, ***, *locale=...*, *data=...*)<a href="#discord.Interaction.translate" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Translates a string using the set <a href="#discord.app_commands.Translator" title="discord.app_commands.Translator"><code>Translator</code></a>.

New in version 2.1.

<dl><dt>Parameters</dt>
<dd>

- **string** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The string to translate. <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> can be used to add more context, information, or any metadata necessary.
- **locale** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>) – The locale to use, this is handy if you want the translation for a specific locale. Defaults to the user’s <a href="#discord.Interaction.locale" title="discord.Interaction.locale"><code>locale</code></a>.
- **data** (*Any*) – The extraneous data that is being translated. If not specified, either <a href="#discord.Interaction.command" title="discord.Interaction.command"><code>command</code></a> or <a href="#discord.Interaction.message" title="discord.Interaction.message"><code>message</code></a> will be passed, depending on which is available in the context.

</dd><dt>Returns</dt>
<dd>

The translated string, or <code>None</code> if a translator was not set.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl></dd>
</dl>

### InteractionResponse ¶

Attributes

- [type](#discord.InteractionResponse.type)

Methods

- async [autocomplete](#discord.InteractionResponse.autocomplete)
- async [defer](#discord.InteractionResponse.defer)
- async [edit\_message](#discord.InteractionResponse.edit_message)
- def [is\_done](#discord.InteractionResponse.is_done)
- async [launch\_activity](#discord.InteractionResponse.launch_activity)
- async [pong](#discord.InteractionResponse.pong)
- async [send\_message](#discord.InteractionResponse.send_message)
- async [send\_modal](#discord.InteractionResponse.send_modal)

<dl><dt>*class*discord.InteractionResponse<a href="#discord.InteractionResponse" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a Discord interaction response.

This type can be accessed through <a href="#discord.Interaction.response" title="discord.Interaction.response"><code>Interaction.response</code></a>.

New in version 2.0.

<dl><dt>is_done()<a href="#discord.InteractionResponse.is_done" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Indicates whether an interaction response has been done before.

An interaction can only be responded to once.

</dd></dl><dl><dt>*property*type<a href="#discord.InteractionResponse.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of response that was sent, <code>None</code> if response is not done.

<dl><dt>Type</dt>
<dd>

<a href="#discord.InteractionResponseType" title="discord.InteractionResponseType"><code>InteractionResponseType</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* defer(***, *ephemeral=False*, *thinking=False*)<a href="#discord.InteractionResponse.defer" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Defers the interaction response.

This is typically used when the interaction is acknowledged and a secondary action will be done later.

This is only supported with the following interaction types:

- <a href="#discord.InteractionType.application_command" title="discord.InteractionType.application_command"><code>InteractionType.application_command</code></a>
- <a href="#discord.InteractionType.component" title="discord.InteractionType.component"><code>InteractionType.component</code></a>
- <a href="#discord.InteractionType.modal_submit" title="discord.InteractionType.modal_submit"><code>InteractionType.modal_submit</code></a>

Changed in version 2.5: This now returns a <a href="#discord.InteractionCallbackResponse" title="discord.InteractionCallbackResponse"><code>InteractionCallbackResponse</code></a> instance.

<dl><dt>Parameters</dt>
<dd>

- **ephemeral** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Indicates whether the deferred message will eventually be ephemeral. This only applies to <a href="#discord.InteractionType.application_command" title="discord.InteractionType.application_command"><code>InteractionType.application_command</code></a> interactions, or if <code>thinking</code> is <code>True</code>.
- **thinking** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Indicates whether the deferred type should be <a href="#discord.InteractionResponseType.deferred_channel_message" title="discord.InteractionResponseType.deferred_channel_message"><code>InteractionResponseType.deferred_channel_message</code></a> instead of the default <a href="#discord.InteractionResponseType.deferred_message_update" title="discord.InteractionResponseType.deferred_message_update"><code>InteractionResponseType.deferred_message_update</code></a> if both are valid. In UI terms, this is represented as if the bot is thinking of a response. It is your responsibility to eventually send a followup message via <a href="#discord.Interaction.followup" title="discord.Interaction.followup"><code>Interaction.followup</code></a> to make this thinking state go away. Application commands (AKA Slash commands) cannot use <a href="#discord.InteractionResponseType.deferred_message_update" title="discord.InteractionResponseType.deferred_message_update"><code>InteractionResponseType.deferred_message_update</code></a>.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Deferring the interaction failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.InteractionResponded" title="discord.InteractionResponded">**InteractionResponded**</a> – This interaction has already been responded to before.

</dd><dt>Returns</dt>
<dd>

The interaction callback resource, or <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.InteractionCallbackResponse" title="discord.InteractionCallbackResponse"><code>InteractionCallbackResponse</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* pong()<a href="#discord.InteractionResponse.pong" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Pongs the ping interaction.

This should rarely be used.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Ponging the interaction failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.InteractionResponded" title="discord.InteractionResponded">**InteractionResponded**</a> – This interaction has already been responded to before.

</dd></dl></dd>
</dl><dl><dt>*await* send_message(*content=None*, ***, *embed=...*, *embeds=...*, *file=...*, *files=...*, *view=...*, *tts=False*, *ephemeral=False*, *allowed_mentions=...*, *suppress_embeds=False*, *silent=False*, *delete_after=None*, *poll=...*)<a href="#discord.InteractionResponse.send_message" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Responds to this interaction by sending a message.

Changed in version 2.5: This now returns a <a href="#discord.InteractionCallbackResponse" title="discord.InteractionCallbackResponse"><code>InteractionCallbackResponse</code></a> instance.

<dl><dt>Parameters</dt>
<dd>

- **content** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The content of the message to send.
- **embeds** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed" title="discord.Embed"><code>Embed</code></a>]) – A list of embeds to send with the content. Maximum of 10. This cannot be mixed with the <code>embed</code> parameter.
- **embed** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed" title="discord.Embed"><code>Embed</code></a>) – The rich embed for the content to send. This cannot be mixed with <code>embeds</code> parameter.
- **file** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>File</code></a>) – The file to upload.
- **files** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>File</code></a>]) – A list of files to upload. Must be a maximum of 10.
- **tts** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Indicates if the message should be sent using text-to-speech.
- **view** (Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>discord.ui.View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>discord.ui.LayoutView</code></a>]) – The view to send with the message.
- **ephemeral** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Indicates if the message should only be visible to the user who started the interaction. If a view is sent with an ephemeral message and it has no timeout set then the timeout is set to 15 minutes.
- **allowed\_mentions** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AllowedMentions" title="discord.AllowedMentions"><code>AllowedMentions</code></a>) – Controls the mentions being processed in this message. See <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable.send" title="discord.abc.Messageable.send"><code>abc.Messageable.send()</code></a> for more information.
- **suppress\_embeds** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to suppress embeds for the message. This sends the message without any embeds if set to <code>True</code>.
- **silent** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether to suppress push and desktop notifications for the message. This will increment the mention counter in the UI, but will not actually send a notification.

  New in version 2.2.
- **delete\_after** (<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>) –

  If provided, the number of seconds to wait in the background before deleting the message we just sent. If the deletion fails, then it is silently ignored.

  New in version 2.1.
- **poll** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Poll" title="discord.Poll"><code>Poll</code></a>) –

  The poll to send with this message.

  New in version 2.4.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Sending the message failed.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – You specified both <code>embed</code> and <code>embeds</code> or <code>file</code> and <code>files</code>.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The length of <code>embeds</code> was invalid.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.InteractionResponded" title="discord.InteractionResponded">**InteractionResponded**</a> – This interaction has already been responded to before.

</dd><dt>Returns</dt>
<dd>

The interaction callback data.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.InteractionCallbackResponse" title="discord.InteractionCallbackResponse"><code>InteractionCallbackResponse</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* edit_message(***, *content=...*, *embed=...*, *embeds=...*, *attachments=...*, *view=...*, *allowed_mentions=...*, *delete_after=None*, *suppress_embeds=...*)<a href="#discord.InteractionResponse.edit_message" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Responds to this interaction by editing the original message of a component or modal interaction.

Changed in version 2.5: This now returns a <a href="#discord.InteractionCallbackResponse" title="discord.InteractionCallbackResponse"><code>InteractionCallbackResponse</code></a> instance.

<dl><dt>Parameters</dt>
<dd>

- **content** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The new content to replace the message with. <code>None</code> removes the content.
- **embeds** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed" title="discord.Embed"><code>Embed</code></a>]) – A list of embeds to edit the message with.
- **embed** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed" title="discord.Embed"><code>Embed</code></a>]) – The embed to edit the message with. <code>None</code> suppresses the embeds. This should not be mixed with the <code>embeds</code> parameter.
- **attachments** (List\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Attachment" title="discord.Attachment"><code>Attachment</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>File</code></a>]]) –

  A list of attachments to keep in the message as well as new files to upload. If <code>[]</code> is passed then all attachments are removed.

  Note

  New files will always appear after current attachments.
- **view** (Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]) –

  The updated view to update this message with. If <code>None</code> is passed then the view is removed.

  Note

  To update the message to add a <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>, you must explicitly set the <code>content</code>, <code>embed</code>, <code>embeds</code>, and <code>attachments</code> parameters to either <code>None</code> or an empty array, as appropriate.
- **allowed\_mentions** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AllowedMentions" title="discord.AllowedMentions"><code>AllowedMentions</code></a>]) – Controls the mentions being processed in this message. See <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.edit" title="discord.Message.edit"><code>Message.edit()</code></a> for more information.
- **delete\_after** (<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>) –

  If provided, the number of seconds to wait in the background before deleting the message we just edited. If the deletion fails, then it is silently ignored.

  New in version 2.2.
- **suppress\_embeds** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether to suppress embeds for the message. This removes all the embeds if set to <code>True</code>. If set to <code>False</code> this brings the embeds back if they were suppressed. Using this parameter requires <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.manage_messages" title="discord.Permissions.manage_messages"><code>manage_messages</code></a>.

  New in version 2.4.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Editing the message failed.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – You specified both <code>embed</code> and <code>embeds</code>.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.InteractionResponded" title="discord.InteractionResponded">**InteractionResponded**</a> – This interaction has already been responded to before.

</dd><dt>Returns</dt>
<dd>

The interaction callback data, or <code>None</code> if editing the message was not possible.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.InteractionCallbackResponse" title="discord.InteractionCallbackResponse"><code>InteractionCallbackResponse</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* send_modal(*modal*, */*)<a href="#discord.InteractionResponse.send_modal" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Responds to this interaction by sending a modal.

Changed in version 2.5: This now returns a <a href="#discord.InteractionCallbackResponse" title="discord.InteractionCallbackResponse"><code>InteractionCallbackResponse</code></a> instance.

<dl><dt>Parameters</dt>
<dd>

**modal** (<a href="#discord.ui.Modal" title="discord.ui.Modal"><code>Modal</code></a>) – The modal to send.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Sending the modal failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.InteractionResponded" title="discord.InteractionResponded">**InteractionResponded**</a> – This interaction has already been responded to before.

</dd><dt>Returns</dt>
<dd>

The interaction callback data.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.InteractionCallbackResponse" title="discord.InteractionCallbackResponse"><code>InteractionCallbackResponse</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* autocomplete(*choices*)<a href="#discord.InteractionResponse.autocomplete" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Responds to this interaction by giving the user the choices they can use.

<dl><dt>Parameters</dt>
<dd>

**choices** (List\[<a href="#discord.app_commands.Choice" title="discord.app_commands.Choice"><code>Choice</code></a>]) – The list of new choices as the user is typing.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Sending the choices failed.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – This interaction cannot respond with autocomplete.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.InteractionResponded" title="discord.InteractionResponded">**InteractionResponded**</a> – This interaction has already been responded to before.

</dd></dl></dd>
</dl><dl><dt>*await* launch_activity()<a href="#discord.InteractionResponse.launch_activity" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Responds to this interaction by launching the activity associated with the app. Only available for apps with activities enabled.

New in version 2.6.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Launching the activity failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.InteractionResponded" title="discord.InteractionResponded">**InteractionResponded**</a> – This interaction has already been responded to before.

</dd><dt>Returns</dt>
<dd>

The interaction callback data.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.InteractionCallbackResponse" title="discord.InteractionCallbackResponse"><code>InteractionCallbackResponse</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### InteractionCallbackResponse ¶

Attributes

- [activity\_id](#discord.InteractionCallbackResponse.activity_id)
- [id](#discord.InteractionCallbackResponse.id)
- [message\_id](#discord.InteractionCallbackResponse.message_id)
- [resource](#discord.InteractionCallbackResponse.resource)
- [type](#discord.InteractionCallbackResponse.type)

Methods

- def [is\_ephemeral](#discord.InteractionCallbackResponse.is_ephemeral)
- def [is\_thinking](#discord.InteractionCallbackResponse.is_thinking)

<dl><dt>*class*discord.InteractionCallbackResponse<a href="#discord.InteractionCallbackResponse" title="Permalink to this definition">¶</a></dt>
<dd>

Represents an interaction response callback.

New in version 2.5.

<dl><dt>id<a href="#discord.InteractionCallbackResponse.id" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction ID.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.InteractionCallbackResponse.type" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction callback response type.

<dl><dt>Type</dt>
<dd>

<a href="#discord.InteractionResponseType" title="discord.InteractionResponseType"><code>InteractionResponseType</code></a>

</dd></dl></dd>
</dl><dl><dt>resource<a href="#discord.InteractionCallbackResponse.resource" title="Permalink to this definition">¶</a></dt>
<dd>

The resource that the interaction response created. If a message was sent, this will be a <a href="#discord.InteractionMessage" title="discord.InteractionMessage"><code>InteractionMessage</code></a>. If an activity was launched this will be a <a href="#discord.InteractionCallbackActivityInstance" title="discord.InteractionCallbackActivityInstance"><code>InteractionCallbackActivityInstance</code></a>. In any other case, this will be <code>None</code>.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.InteractionMessage" title="discord.InteractionMessage"><code>InteractionMessage</code></a>, <a href="#discord.InteractionCallbackActivityInstance" title="discord.InteractionCallbackActivityInstance"><code>InteractionCallbackActivityInstance</code></a>]]

</dd></dl></dd>
</dl><dl><dt>message_id<a href="#discord.InteractionCallbackResponse.message_id" title="Permalink to this definition">¶</a></dt>
<dd>

The message ID of the resource. Only available if the resource is a <a href="#discord.InteractionMessage" title="discord.InteractionMessage"><code>InteractionMessage</code></a>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>activity_id<a href="#discord.InteractionCallbackResponse.activity_id" title="Permalink to this definition">¶</a></dt>
<dd>

The activity ID of the resource. Only available if the resource is a <a href="#discord.InteractionCallbackActivityInstance" title="discord.InteractionCallbackActivityInstance"><code>InteractionCallbackActivityInstance</code></a>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>is_thinking()<a href="#discord.InteractionCallbackResponse.is_thinking" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the response was a thinking defer.

</dd></dl><dl><dt>is_ephemeral()<a href="#discord.InteractionCallbackResponse.is_ephemeral" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the response was ephemeral.

</dd></dl></dd>
</dl>

### InteractionCallbackActivityInstance ¶

Attributes

- [id](#discord.InteractionCallbackActivityInstance.id)

<dl><dt>*class*discord.InteractionCallbackActivityInstance<a href="#discord.InteractionCallbackActivityInstance" title="Permalink to this definition">¶</a></dt>
<dd>

Represents an activity instance launched as an interaction response.

New in version 2.5.

<dl><dt>id<a href="#discord.InteractionCallbackActivityInstance.id" title="Permalink to this definition">¶</a></dt>
<dd>

The activity instance ID.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### InteractionMessage ¶

Attributes

- [clean\_content](#discord.InteractionMessage.clean_content)
- [created\_at](#discord.InteractionMessage.created_at)
- [edited\_at](#discord.InteractionMessage.edited_at)
- [interaction](#discord.InteractionMessage.interaction)
- [jump\_url](#discord.InteractionMessage.jump_url)
- [pinned\_at](#discord.InteractionMessage.pinned_at)
- [raw\_channel\_mentions](#discord.InteractionMessage.raw_channel_mentions)
- [raw\_mentions](#discord.InteractionMessage.raw_mentions)
- [raw\_role\_mentions](#discord.InteractionMessage.raw_role_mentions)
- [system\_content](#discord.InteractionMessage.system_content)
- [thread](#discord.InteractionMessage.thread)

Methods

- async [add\_files](#discord.InteractionMessage.add_files)
- async [add\_reaction](#discord.InteractionMessage.add_reaction)
- async [clear\_reaction](#discord.InteractionMessage.clear_reaction)
- async [clear\_reactions](#discord.InteractionMessage.clear_reactions)
- async [create\_thread](#discord.InteractionMessage.create_thread)
- async [delete](#discord.InteractionMessage.delete)
- async [edit](#discord.InteractionMessage.edit)
- async [end\_poll](#discord.InteractionMessage.end_poll)
- async [fetch](#discord.InteractionMessage.fetch)
- async [fetch\_thread](#discord.InteractionMessage.fetch_thread)
- async [forward](#discord.InteractionMessage.forward)
- def [is\_forwardable](#discord.InteractionMessage.is_forwardable)
- def [is\_system](#discord.InteractionMessage.is_system)
- async [pin](#discord.InteractionMessage.pin)
- async [publish](#discord.InteractionMessage.publish)
- async [remove\_attachments](#discord.InteractionMessage.remove_attachments)
- async [remove\_reaction](#discord.InteractionMessage.remove_reaction)
- async [reply](#discord.InteractionMessage.reply)
- def [to\_reference](#discord.InteractionMessage.to_reference)
- async [unpin](#discord.InteractionMessage.unpin)

<dl><dt>*class*discord.InteractionMessage<a href="#discord.InteractionMessage" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the original interaction response message.

This allows you to edit or delete the message associated with the interaction response. To retrieve this object see <a href="#discord.Interaction.original_response" title="discord.Interaction.original_response"><code>Interaction.original_response()</code></a>.

This inherits from <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>discord.Message</code></a> with changes to <a href="#discord.InteractionMessage.edit" title="discord.InteractionMessage.edit"><code>edit()</code></a> and <a href="#discord.InteractionMessage.delete" title="discord.InteractionMessage.delete"><code>delete()</code></a> to work.

New in version 2.0.

<dl><dt>*await* add_reaction(*emoji*, */*)<a href="#discord.InteractionMessage.add_reaction" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Adds a reaction to the message.

The emoji may be a unicode emoji or a custom guild <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>.

You must have <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.read_message_history" title="discord.Permissions.read_message_history"><code>read_message_history</code></a> to do this. If nobody else has reacted to the message using this emoji, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.add_reactions" title="discord.Permissions.add_reactions"><code>add_reactions</code></a> is required.

Changed in version 2.0: <code>emoji</code> parameter is now positional-only.

Changed in version 2.0: This function will now raise <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)"><code>TypeError</code></a> instead of <code>InvalidArgument</code>.

<dl><dt>Parameters</dt>
<dd>

**emoji** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Reaction" title="discord.Reaction"><code>Reaction</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The emoji to react with.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Adding the reaction failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the proper permissions to react to the message.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The emoji you specified was not found.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The emoji parameter is invalid.

</dd></dl></dd>
</dl><dl><dt>clean_content<a href="#discord.InteractionMessage.clean_content" title="Permalink to this definition">¶</a></dt>
<dd>

A property that returns the content in a “cleaned up” manner. This basically means that mentions are transformed into the way the client shows it. e.g. <code>&lt;#id&gt;</code> will transform into <code>#name</code>.

This will also transform @everyone and @here mentions into non-mentions.

Note

This *does not* affect markdown. If you want to escape or remove markdown then use <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.utils.escape_markdown" title="discord.utils.escape_markdown"><code>utils.escape_markdown()</code></a> or <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.utils.remove_markdown" title="discord.utils.remove_markdown"><code>utils.remove_markdown()</code></a> respectively, along with this function.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* clear_reaction(*emoji*)<a href="#discord.InteractionMessage.clear_reaction" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Clears a specific reaction from the message.

The emoji may be a unicode emoji or a custom guild <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>.

You must have <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.manage_messages" title="discord.Permissions.manage_messages"><code>manage_messages</code></a> to do this.

New in version 1.3.

Changed in version 2.0: This function will now raise <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)"><code>TypeError</code></a> instead of <code>InvalidArgument</code>.

<dl><dt>Parameters</dt>
<dd>

**emoji** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Reaction" title="discord.Reaction"><code>Reaction</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The emoji to clear.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Clearing the reaction failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the proper permissions to clear the reaction.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The emoji you specified was not found.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The emoji parameter is invalid.

</dd></dl></dd>
</dl><dl><dt>*await* clear_reactions()<a href="#discord.InteractionMessage.clear_reactions" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Removes all the reactions from the message.

You must have <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.manage_messages" title="discord.Permissions.manage_messages"><code>manage_messages</code></a> to do this.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Removing the reactions failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the proper permissions to remove all the reactions.

</dd></dl></dd>
</dl><dl><dt>*await* create_thread(***, *name*, *auto_archive_duration=...*, *slowmode_delay=None*, *reason=None*)<a href="#discord.InteractionMessage.create_thread" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Creates a public thread from this message.

You must have <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.create_public_threads" title="discord.Permissions.create_public_threads"><code>create_public_threads</code></a> in order to create a public thread from a message.

The channel this message belongs in must be a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.TextChannel" title="discord.TextChannel"><code>TextChannel</code></a>.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the thread.
- **auto\_archive\_duration** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) –

  The duration in minutes before a thread is automatically hidden from the channel list. If not provided, the channel’s default auto archive duration is used.

  Must be one of <code>60</code>, <code>1440</code>, <code>4320</code>, or <code>10080</code>, if provided.
- **slowmode\_delay** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – Specifies the slowmode rate limit for user in this channel, in seconds. The maximum value possible is <code>21600</code>. By default no slowmode rate limit if this is <code>None</code>.
- **reason** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The reason for creating a new thread. Shows up on the audit log.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have permissions to create a thread.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Creating the thread failed.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – This message does not have guild info attached.

</dd><dt>Returns</dt>
<dd>

The created thread.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*created_at<a href="#discord.InteractionMessage.created_at" title="Permalink to this definition">¶</a></dt>
<dd>

The message’s creation time in UTC.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* edit(***, *content=...*, *embeds=...*, *embed=...*, *attachments=...*, *view=...*, *allowed_mentions=None*, *delete_after=None*, *poll=...*)<a href="#discord.InteractionMessage.edit" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Edits the message.

<dl><dt>Parameters</dt>
<dd>

- **content** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The content to edit the message with or <code>None</code> to clear it.
- **embeds** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed" title="discord.Embed"><code>Embed</code></a>]) – A list of embeds to edit the message with.
- **embed** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed" title="discord.Embed"><code>Embed</code></a>]) – The embed to edit the message with. <code>None</code> suppresses the embeds. This should not be mixed with the <code>embeds</code> parameter.
- **attachments** (List\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Attachment" title="discord.Attachment"><code>Attachment</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>File</code></a>]]) –

  A list of attachments to keep in the message as well as new files to upload. If <code>[]</code> is passed then all attachments are removed.

  Note

  New files will always appear after current attachments.
- **allowed\_mentions** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AllowedMentions" title="discord.AllowedMentions"><code>AllowedMentions</code></a>) – Controls the mentions being processed in this message. See <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable.send" title="discord.abc.Messageable.send"><code>abc.Messageable.send()</code></a> for more information.
- **view** (Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]) –

  The updated view to update this message with. If <code>None</code> is passed then the view is removed.

  Note

  If you want to update the message to have a <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>, you must explicitly set the <code>content</code>, <code>embed</code>, <code>embeds</code>, and <code>attachments</code> parameters to <code>None</code> if the previous message had any.
- **delete\_after** (Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) –

  If provided, the number of seconds to wait in the background before deleting the message we just sent. If the deletion fails, then it is silently ignored.

  New in version 2.2.
- **poll** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Poll" title="discord.Poll"><code>Poll</code></a>) –

  The poll to create when editing the message.

  New in version 2.5.

  Note

  This is only accepted if the interaction response’s <a href="#discord.InteractionResponse.type" title="discord.InteractionResponse.type"><code>InteractionResponse.type</code></a> attribute is <a href="#discord.InteractionResponseType.deferred_channel_message" title="discord.InteractionResponseType.deferred_channel_message"><code>InteractionResponseType.deferred_channel_message</code></a>.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Editing the message failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – Edited a message that is not yours.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – You specified both <code>embed</code> and <code>embeds</code>
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The length of <code>embeds</code> was invalid.

</dd><dt>Returns</dt>
<dd>

The newly edited message.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.InteractionMessage" title="discord.InteractionMessage"><code>InteractionMessage</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*edited_at<a href="#discord.InteractionMessage.edited_at" title="Permalink to this definition">¶</a></dt>
<dd>

An aware UTC datetime object containing the edited time of the message.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* end_poll()<a href="#discord.InteractionMessage.end_poll" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Ends the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Poll" title="discord.Poll"><code>Poll</code></a> attached to this message.

This can only be done if you are the message author.

If the poll was successfully ended, then it returns the updated <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>.

<dl><dt>Raises</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Ending the poll failed.

</dd><dt>Returns</dt>
<dd>

The updated message.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch()<a href="#discord.InteractionMessage.fetch" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Fetches the partial message to a full <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The message was not found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the permissions required to get a message.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the message failed.

</dd><dt>Returns</dt>
<dd>

The full message.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_thread()<a href="#discord.InteractionMessage.fetch_thread" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves the public thread attached to this message.

Note

This method is an API call. For general usage, consider <a href="#discord.InteractionMessage.thread" title="discord.InteractionMessage.thread"><code>thread</code></a> instead.

New in version 2.4.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.InvalidData" title="discord.InvalidData">**InvalidData**</a> – An unknown channel type was received from Discord or the guild the thread belongs to is not the same as the one in this object points to.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the thread failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – There is no thread attached to this message.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have permission to fetch this channel.

</dd><dt>Returns</dt>
<dd>

The public thread attached to this message.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* forward(*destination*, ***, *fail_if_not_exists=True*)<a href="#discord.InteractionMessage.forward" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Forwards this message to a channel.

New in version 2.5.

<dl><dt>Parameters</dt>
<dd>

- **destination** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable" title="discord.abc.Messageable"><code>Messageable</code></a>) – The channel to forward this message to.
- **fail\_if\_not\_exists** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether replying using the message reference should raise <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException"><code>HTTPException</code></a> if the message no longer exists or Discord could not fetch the message.

</dd><dt>Raises</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Forwarding the message failed.

</dd><dt>Returns</dt>
<dd>

The message sent to the channel.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*interaction<a href="#discord.InteractionMessage.interaction" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction that this message is a response to.

New in version 2.0.

Deprecated since version 2.4: This attribute is deprecated and will be removed in a future version. Use <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.interaction_metadata" title="discord.Message.interaction_metadata"><code>interaction_metadata</code></a> instead.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.MessageInteraction" title="discord.MessageInteraction"><code>MessageInteraction</code></a>]

</dd></dl></dd>
</dl><dl><dt>is_forwardable()<a href="#discord.InteractionMessage.is_forwardable" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the message can be forwarded using <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.forward" title="discord.Message.forward"><code>Message.forward()</code></a>.

A message is forwardable only if it is a basic message type and does not contain a poll, call, or activity, and is not a system message.

New in version 2.7.

</dd></dl><dl><dt>is_system()<a href="#discord.InteractionMessage.is_system" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the message is a system message.

A system message is a message that is constructed entirely by the Discord API in response to something.

New in version 1.3.

</dd></dl><dl><dt>*property*jump_url<a href="#discord.InteractionMessage.jump_url" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a URL that allows the client to jump to this message.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* pin(***, *reason=None*)<a href="#discord.InteractionMessage.pin" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Pins the message.

You must have <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.pin_messages" title="discord.Permissions.pin_messages"><code>pin_messages</code></a> to do this in a non-private channel context.

<dl><dt>Parameters</dt>
<dd>

**reason** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) –

The reason for pinning the message. Shows up on the audit log.

New in version 1.4.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have permissions to pin the message.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The message or channel was not found or deleted.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Pinning the message failed, probably due to the channel having more than 250 pinned messages.

</dd></dl></dd>
</dl><dl><dt>*property*pinned_at<a href="#discord.InteractionMessage.pinned_at" title="Permalink to this definition">¶</a></dt>
<dd>

An aware UTC datetime object containing the time when the message was pinned.

Note

This is only set for messages that are returned by <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable.pins" title="discord.abc.Messageable.pins"><code>abc.Messageable.pins()</code></a>.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* publish()<a href="#discord.InteractionMessage.publish" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Publishes this message to the channel’s followers.

The message must have been sent in a news channel. You must have <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.send_messages" title="discord.Permissions.send_messages"><code>send_messages</code></a> to do this.

If the message is not your own then <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.manage_messages" title="discord.Permissions.manage_messages"><code>manage_messages</code></a> is also needed.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the proper permissions to publish this message or the channel is not a news channel.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Publishing the message failed.

</dd></dl></dd>
</dl><dl><dt>raw_channel_mentions<a href="#discord.InteractionMessage.raw_channel_mentions" title="Permalink to this definition">¶</a></dt>
<dd>

A property that returns an array of channel IDs matched with the syntax of <code>&lt;#channel_id&gt;</code> in the message content.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>raw_mentions<a href="#discord.InteractionMessage.raw_mentions" title="Permalink to this definition">¶</a></dt>
<dd>

A property that returns an array of user IDs matched with the syntax of <code>&lt;@user_id&gt;</code> in the message content.

This allows you to receive the user IDs of mentioned users even in a private message context.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>raw_role_mentions<a href="#discord.InteractionMessage.raw_role_mentions" title="Permalink to this definition">¶</a></dt>
<dd>

A property that returns an array of role IDs matched with the syntax of <code>&lt;@&amp;role_id&gt;</code> in the message content.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* remove_reaction(*emoji*, *member*)<a href="#discord.InteractionMessage.remove_reaction" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Remove a reaction by the member from the message.

The emoji may be a unicode emoji or a custom guild <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>.

If the reaction is not your own (i.e. <code>member</code> parameter is not you) then <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.manage_messages" title="discord.Permissions.manage_messages"><code>manage_messages</code></a> is needed.

The <code>member</code> parameter must represent a member and meet the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>abc.Snowflake</code></a> abc.

Changed in version 2.0: This function will now raise <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)"><code>TypeError</code></a> instead of <code>InvalidArgument</code>.

<dl><dt>Parameters</dt>
<dd>

- **emoji** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Reaction" title="discord.Reaction"><code>Reaction</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The emoji to remove.
- **member** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>abc.Snowflake</code></a>) – The member for which to remove the reaction.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Removing the reaction failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the proper permissions to remove the reaction.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The member or emoji you specified was not found.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The emoji parameter is invalid.

</dd></dl></dd>
</dl><dl><dt>*await* reply(*content=None*, ***kwargs*)<a href="#discord.InteractionMessage.reply" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A shortcut method to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable.send" title="discord.abc.Messageable.send"><code>abc.Messageable.send()</code></a> to reply to the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>.

New in version 1.6.

Changed in version 2.0: This function will now raise <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)"><code>TypeError</code></a> or <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)"><code>ValueError</code></a> instead of <code>InvalidArgument</code>.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Sending the message failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the proper permissions to send the message.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The <code>files</code> list is not of the appropriate size
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – You specified both <code>file</code> and <code>files</code>.

</dd><dt>Returns</dt>
<dd>

The message that was sent.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>

</dd></dl></dd>
</dl><dl><dt>system_content<a href="#discord.InteractionMessage.system_content" title="Permalink to this definition">¶</a></dt>
<dd>

A property that returns the content that is rendered regardless of the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.type" title="discord.Message.type"><code>Message.type</code></a>.

In the case of <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MessageType.default" title="discord.MessageType.default"><code>MessageType.default</code></a> and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MessageType.reply" title="discord.MessageType.reply"><code>MessageType.reply</code></a>, this just returns the regular <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.content" title="discord.Message.content"><code>Message.content</code></a>. Otherwise this returns an English message denoting the contents of the system message.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*thread<a href="#discord.InteractionMessage.thread" title="Permalink to this definition">¶</a></dt>
<dd>

The public thread created from this message, if it exists.

Note

For messages received via the gateway this does not retrieve archived threads, as they are not retained in the internal cache. Use <a href="#discord.InteractionMessage.fetch_thread" title="discord.InteractionMessage.fetch_thread"><code>fetch_thread()</code></a> instead.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a>]

</dd></dl></dd>
</dl><dl><dt>to_reference(***, *fail_if_not_exists=True*, *type=&lt;MessageReferenceType.default: 0&gt;*)<a href="#discord.InteractionMessage.to_reference" title="Permalink to this definition">¶</a></dt>
<dd>

Creates a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MessageReference" title="discord.MessageReference"><code>MessageReference</code></a> from the current message.

New in version 1.6.

<dl><dt>Parameters</dt>
<dd>

- **fail\_if\_not\_exists** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the referenced message should raise <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException"><code>HTTPException</code></a> if the message no longer exists or Discord could not fetch the message.

  New in version 1.7.
- **type** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MessageReferenceType" title="discord.MessageReferenceType"><code>MessageReferenceType</code></a>) –

  The type of message reference.

  New in version 2.5.

</dd><dt>Returns</dt>
<dd>

The reference to this message.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MessageReference" title="discord.MessageReference"><code>MessageReference</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* unpin(***, *reason=None*)<a href="#discord.InteractionMessage.unpin" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Unpins the message.

You must have <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.pin_messages" title="discord.Permissions.pin_messages"><code>pin_messages</code></a> to do this in a non-private channel context.

<dl><dt>Parameters</dt>
<dd>

**reason** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) –

The reason for unpinning the message. Shows up on the audit log.

New in version 1.4.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have permissions to unpin the message.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The message or channel was not found or deleted.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Unpinning the message failed.

</dd></dl></dd>
</dl><dl><dt>*await* add_files(**files*)<a href="#discord.InteractionMessage.add_files" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Adds new files to the end of the message attachments.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

**\*files** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>File</code></a>) – New files to add to the message.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Editing the message failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – Tried to edit a message that isn’t yours.

</dd><dt>Returns</dt>
<dd>

The newly edited message.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.InteractionMessage" title="discord.InteractionMessage"><code>InteractionMessage</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* remove_attachments(**attachments*)<a href="#discord.InteractionMessage.remove_attachments" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Removes attachments from the message.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

**\*attachments** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Attachment" title="discord.Attachment"><code>Attachment</code></a>) – Attachments to remove from the message.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Editing the message failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – Tried to edit a message that isn’t yours.

</dd><dt>Returns</dt>
<dd>

The newly edited message.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.InteractionMessage" title="discord.InteractionMessage"><code>InteractionMessage</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* delete(***, *delay=None*)<a href="#discord.InteractionMessage.delete" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Deletes the message.

<dl><dt>Parameters</dt>
<dd>

**delay** (Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – If provided, the number of seconds to wait before deleting the message. The waiting is done in the background and deletion failures are ignored.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have proper permissions to delete the message.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The message was deleted already.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Deleting the message failed.

</dd></dl></dd>
</dl></dd>
</dl>

### MessageInteraction ¶

Attributes

- [created\_at](#discord.MessageInteraction.created_at)
- [id](#discord.MessageInteraction.id)
- [name](#discord.MessageInteraction.name)
- [type](#discord.MessageInteraction.type)
- [user](#discord.MessageInteraction.user)

<dl><dt>*class*discord.MessageInteraction<a href="#discord.MessageInteraction" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the interaction that a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a> is a response to.

New in version 2.0.

<dl><dt>x == y</dt>
<dd>

Checks if two message interactions are equal.

</dd></dl><dl><dt>x != y</dt>
<dd>

Checks if two message interactions are not equal.

</dd></dl><dl><dt>hash(x)</dt>
<dd>

Returns the message interaction’s hash.

</dd></dl>

<dl><dt>id<a href="#discord.MessageInteraction.id" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction ID.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.MessageInteraction.type" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction type.

<dl><dt>Type</dt>
<dd>

<a href="#discord.InteractionType" title="discord.InteractionType"><code>InteractionType</code></a>

</dd></dl></dd>
</dl><dl><dt>name<a href="#discord.MessageInteraction.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>user<a href="#discord.MessageInteraction.user" title="Permalink to this definition">¶</a></dt>
<dd>

The user or member that invoked the interaction.

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*created_at<a href="#discord.MessageInteraction.created_at" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction’s creation time in UTC.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### MessageInteractionMetadata ¶

Attributes

- [created\_at](#discord.MessageInteractionMetadata.created_at)
- [id](#discord.MessageInteractionMetadata.id)
- [interacted\_message](#discord.MessageInteractionMetadata.interacted_message)
- [interacted\_message\_id](#discord.MessageInteractionMetadata.interacted_message_id)
- [modal\_interaction](#discord.MessageInteractionMetadata.modal_interaction)
- [original\_response\_message](#discord.MessageInteractionMetadata.original_response_message)
- [original\_response\_message\_id](#discord.MessageInteractionMetadata.original_response_message_id)
- [target\_message](#discord.MessageInteractionMetadata.target_message)
- [target\_message\_id](#discord.MessageInteractionMetadata.target_message_id)
- [target\_user](#discord.MessageInteractionMetadata.target_user)
- [type](#discord.MessageInteractionMetadata.type)
- [user](#discord.MessageInteractionMetadata.user)

Methods

- def [is\_guild\_integration](#discord.MessageInteractionMetadata.is_guild_integration)
- def [is\_user\_integration](#discord.MessageInteractionMetadata.is_user_integration)

<dl><dt>*class*discord.MessageInteractionMetadata<a href="#discord.MessageInteractionMetadata" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the interaction metadata of a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a> if it was sent in response to an interaction.

New in version 2.4.

<dl><dt>x == y</dt>
<dd>

Checks if two message interactions are equal.

</dd></dl><dl><dt>x != y</dt>
<dd>

Checks if two message interactions are not equal.

</dd></dl><dl><dt>hash(x)</dt>
<dd>

Returns the message interaction’s hash.

</dd></dl>

<dl><dt>id<a href="#discord.MessageInteractionMetadata.id" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction ID.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.MessageInteractionMetadata.type" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction type.

<dl><dt>Type</dt>
<dd>

<a href="#discord.InteractionType" title="discord.InteractionType"><code>InteractionType</code></a>

</dd></dl></dd>
</dl><dl><dt>user<a href="#discord.MessageInteractionMetadata.user" title="Permalink to this definition">¶</a></dt>
<dd>

The user that invoked the interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a>

</dd></dl></dd>
</dl><dl><dt>original_response_message_id<a href="#discord.MessageInteractionMetadata.original_response_message_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the original response message if the message is a follow-up.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>interacted_message_id<a href="#discord.MessageInteractionMetadata.interacted_message_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the message that containes the interactive components, if applicable.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>modal_interaction<a href="#discord.MessageInteractionMetadata.modal_interaction" title="Permalink to this definition">¶</a></dt>
<dd>

The metadata of the modal submit interaction that triggered this interaction, if applicable.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.MessageInteractionMetadata" title="discord.MessageInteractionMetadata"><code>MessageInteractionMetadata</code></a>]

</dd></dl></dd>
</dl><dl><dt>target_user<a href="#discord.MessageInteractionMetadata.target_user" title="Permalink to this definition">¶</a></dt>
<dd>

The user the command was run on, only applicable to user context menus.

New in version 2.5.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a>]

</dd></dl></dd>
</dl><dl><dt>target_message_id<a href="#discord.MessageInteractionMetadata.target_message_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the message the command was run on, only applicable to message context menus.

New in version 2.5.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*created_at<a href="#discord.MessageInteractionMetadata.created_at" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction’s creation time in UTC.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*original_response_message<a href="#discord.MessageInteractionMetadata.original_response_message" title="Permalink to this definition">¶</a></dt>
<dd>

The original response message if the message is a follow-up and is found in cache.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*interacted_message<a href="#discord.MessageInteractionMetadata.interacted_message" title="Permalink to this definition">¶</a></dt>
<dd>

The message that containes the interactive components, if applicable and is found in cache.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*target_message<a href="#discord.MessageInteractionMetadata.target_message" title="Permalink to this definition">¶</a></dt>
<dd>

The target message, if applicable and is found in cache.

New in version 2.5.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>]

</dd></dl></dd>
</dl><dl><dt>is_guild_integration()<a href="#discord.MessageInteractionMetadata.is_guild_integration" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Returns <code>True</code> if the interaction is a guild integration.

</dd></dl><dl><dt>is_user_integration()<a href="#discord.MessageInteractionMetadata.is_user_integration" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Returns <code>True</code> if the interaction is a user integration.

</dd></dl></dd>
</dl>

### Component ¶

Attributes

- [type](#discord.Component.type)

<dl><dt>*class*discord.Component<a href="#discord.Component" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a Discord Bot UI Kit Component.

The components supported by Discord are:

- <a href="#discord.ActionRow" title="discord.ActionRow"><code>ActionRow</code></a>
- <a href="#discord.Button" title="discord.Button"><code>Button</code></a>
- <a href="#discord.SelectMenu" title="discord.SelectMenu"><code>SelectMenu</code></a>
- <a href="#discord.TextInput" title="discord.TextInput"><code>TextInput</code></a>
- <a href="#discord.SectionComponent" title="discord.SectionComponent"><code>SectionComponent</code></a>
- <a href="#discord.TextDisplay" title="discord.TextDisplay"><code>TextDisplay</code></a>
- <a href="#discord.ThumbnailComponent" title="discord.ThumbnailComponent"><code>ThumbnailComponent</code></a>
- <a href="#discord.MediaGalleryComponent" title="discord.MediaGalleryComponent"><code>MediaGalleryComponent</code></a>
- <a href="#discord.FileComponent" title="discord.FileComponent"><code>FileComponent</code></a>
- <a href="#discord.SeparatorComponent" title="discord.SeparatorComponent"><code>SeparatorComponent</code></a>
- <a href="#discord.Container" title="discord.Container"><code>Container</code></a>
- <a href="#discord.LabelComponent" title="discord.LabelComponent"><code>LabelComponent</code></a>
- <a href="#discord.FileUploadComponent" title="discord.FileUploadComponent"><code>FileUploadComponent</code></a>

This class is abstract and cannot be instantiated.

New in version 2.0.

<dl><dt>*property*type<a href="#discord.Component.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### ActionRow ¶

Attributes

- [children](#discord.ActionRow.children)
- [id](#discord.ActionRow.id)
- [type](#discord.ActionRow.type)

<dl><dt>*class*discord.ActionRow<a href="#discord.ActionRow" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a Discord Bot UI Kit Action Row.

This is a component that holds up to 5 children components in a row.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

New in version 2.0.

<dl><dt>children<a href="#discord.ActionRow.children" title="Permalink to this definition">¶</a></dt>
<dd>

The children components that this holds, if any.

<dl><dt>Type</dt>
<dd>

List\[Union\[<a href="#discord.Button" title="discord.Button"><code>Button</code></a>, <a href="#discord.SelectMenu" title="discord.SelectMenu"><code>SelectMenu</code></a>, <a href="#discord.TextInput" title="discord.TextInput"><code>TextInput</code></a>]]

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.ActionRow.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.ActionRow.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### Button ¶

Attributes

- [custom\_id](#discord.Button.custom_id)
- [disabled](#discord.Button.disabled)
- [emoji](#discord.Button.emoji)
- [id](#discord.Button.id)
- [label](#discord.Button.label)
- [sku\_id](#discord.Button.sku_id)
- [style](#discord.Button.style)
- [type](#discord.Button.type)
- [url](#discord.Button.url)

<dl><dt>*class*discord.Button<a href="#discord.Button" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a button from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type to create a button is <a href="#discord.ui.Button" title="discord.ui.Button"><code>discord.ui.Button</code></a> not this one.

New in version 2.0.

<dl><dt>style<a href="#discord.Button.style" title="Permalink to this definition">¶</a></dt>
<dd>

The style of the button.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ButtonStyle" title="discord.ButtonStyle"><code>ButtonStyle</code></a>

</dd></dl></dd>
</dl><dl><dt>custom_id<a href="#discord.Button.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the button that gets received during an interaction. If this button is for a URL, it does not have a custom ID.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>url<a href="#discord.Button.url" title="Permalink to this definition">¶</a></dt>
<dd>

The URL this button sends you to.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>disabled<a href="#discord.Button.disabled" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the button is disabled or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>label<a href="#discord.Button.label" title="Permalink to this definition">¶</a></dt>
<dd>

The label of the button, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>emoji<a href="#discord.Button.emoji" title="Permalink to this definition">¶</a></dt>
<dd>

The emoji of the button, if available.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>]

</dd></dl></dd>
</dl><dl><dt>sku_id<a href="#discord.Button.sku_id" title="Permalink to this definition">¶</a></dt>
<dd>

The SKU ID this button sends you to, if available.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.Button.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.Button.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### SelectMenu ¶

Attributes

- [channel\_types](#discord.SelectMenu.channel_types)
- [custom\_id](#discord.SelectMenu.custom_id)
- [disabled](#discord.SelectMenu.disabled)
- [id](#discord.SelectMenu.id)
- [max\_values](#discord.SelectMenu.max_values)
- [min\_values](#discord.SelectMenu.min_values)
- [options](#discord.SelectMenu.options)
- [placeholder](#discord.SelectMenu.placeholder)
- [required](#discord.SelectMenu.required)
- [type](#discord.SelectMenu.type)

<dl><dt>*class*discord.SelectMenu<a href="#discord.SelectMenu" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a select menu from the Discord Bot UI Kit.

A select menu is functionally the same as a dropdown, however on mobile it renders a bit differently.

Note

The user constructible and usable type to create a select menu is <a href="#discord.ui.Select" title="discord.ui.Select"><code>discord.ui.Select</code></a> not this one.

New in version 2.0.

<dl><dt>type<a href="#discord.SelectMenu.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl><dl><dt>custom_id<a href="#discord.SelectMenu.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the select menu that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>placeholder<a href="#discord.SelectMenu.placeholder" title="Permalink to this definition">¶</a></dt>
<dd>

The placeholder text that is shown if nothing is selected, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>min_values<a href="#discord.SelectMenu.min_values" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum number of items that must be chosen for this select menu. Defaults to 1 and must be between 0 and 25.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>max_values<a href="#discord.SelectMenu.max_values" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of items that must be chosen for this select menu. Defaults to 1 and must be between 1 and 25.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>options<a href="#discord.SelectMenu.options" title="Permalink to this definition">¶</a></dt>
<dd>

A list of options that can be selected in this menu.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.SelectOption" title="discord.SelectOption"><code>SelectOption</code></a>]

</dd></dl></dd>
</dl><dl><dt>disabled<a href="#discord.SelectMenu.disabled" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is disabled or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>channel_types<a href="#discord.SelectMenu.channel_types" title="Permalink to this definition">¶</a></dt>
<dd>

A list of channel types that are allowed to be chosen in this select menu.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelType" title="discord.ChannelType"><code>ChannelType</code></a>]

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.SelectMenu.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>required<a href="#discord.SelectMenu.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is required. Only applicable within modals.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### TextInput ¶

Attributes

- [custom\_id](#discord.TextInput.custom_id)
- [default](#discord.TextInput.default)
- [id](#discord.TextInput.id)
- [label](#discord.TextInput.label)
- [max\_length](#discord.TextInput.max_length)
- [min\_length](#discord.TextInput.min_length)
- [placeholder](#discord.TextInput.placeholder)
- [required](#discord.TextInput.required)
- [style](#discord.TextInput.style)
- [type](#discord.TextInput.type)
- [value](#discord.TextInput.value)

<dl><dt>*class*discord.TextInput<a href="#discord.TextInput" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a text input from the Discord Bot UI Kit.

Note

The user constructible and usable type to create a text input is <a href="#discord.ui.TextInput" title="discord.ui.TextInput"><code>discord.ui.TextInput</code></a> not this one.

New in version 2.0.

<dl><dt>custom_id<a href="#discord.TextInput.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the text input that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>label<a href="#discord.TextInput.label" title="Permalink to this definition">¶</a></dt>
<dd>

The label to display above the text input.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>style<a href="#discord.TextInput.style" title="Permalink to this definition">¶</a></dt>
<dd>

The style of the text input.

<dl><dt>Type</dt>
<dd>

<a href="#discord.TextStyle" title="discord.TextStyle"><code>TextStyle</code></a>

</dd></dl></dd>
</dl><dl><dt>placeholder<a href="#discord.TextInput.placeholder" title="Permalink to this definition">¶</a></dt>
<dd>

The placeholder text to display when the text input is empty.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>value<a href="#discord.TextInput.value" title="Permalink to this definition">¶</a></dt>
<dd>

The default value of the text input.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>required<a href="#discord.TextInput.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the text input is required.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>min_length<a href="#discord.TextInput.min_length" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum length of the text input.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>max_length<a href="#discord.TextInput.max_length" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum length of the text input.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.TextInput.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.TextInput.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*default<a href="#discord.TextInput.default" title="Permalink to this definition">¶</a></dt>
<dd>

The default value of the text input.

This is an alias to <a href="#discord.TextInput.value" title="discord.TextInput.value"><code>value</code></a>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl></dd>
</dl>

### LabelComponent ¶

Attributes

- [component](#discord.LabelComponent.component)
- [description](#discord.LabelComponent.description)
- [id](#discord.LabelComponent.id)
- [label](#discord.LabelComponent.label)
- [type](#discord.LabelComponent.type)

<dl><dt>*class*discord.LabelComponent<a href="#discord.LabelComponent" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a label component from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type for creating a label is <a href="#discord.ui.Label" title="discord.ui.Label"><code>discord.ui.Label</code></a> not this one.

New in version 2.6.

<dl><dt>label<a href="#discord.LabelComponent.label" title="Permalink to this definition">¶</a></dt>
<dd>

The label text to display.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.LabelComponent.description" title="Permalink to this definition">¶</a></dt>
<dd>

The description text to display below the label, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>component<a href="#discord.LabelComponent.component" title="Permalink to this definition">¶</a></dt>
<dd>

The component that this label is associated with.

<dl><dt>Type</dt>
<dd>

<a href="#discord.Component" title="discord.Component"><code>Component</code></a>

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.LabelComponent.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.LabelComponent.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### SectionComponent ¶

Attributes

- [accessory](#discord.SectionComponent.accessory)
- [children](#discord.SectionComponent.children)
- [id](#discord.SectionComponent.id)
- [type](#discord.SectionComponent.type)

<dl><dt>*class*discord.SectionComponent<a href="#discord.SectionComponent" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a section from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type to create a section is <a href="#discord.ui.Section" title="discord.ui.Section"><code>discord.ui.Section</code></a> not this one.

New in version 2.6.

<dl><dt>children<a href="#discord.SectionComponent.children" title="Permalink to this definition">¶</a></dt>
<dd>

The components on this section.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.TextDisplay" title="discord.TextDisplay"><code>TextDisplay</code></a>]

</dd></dl></dd>
</dl><dl><dt>accessory<a href="#discord.SectionComponent.accessory" title="Permalink to this definition">¶</a></dt>
<dd>

The section accessory.

<dl><dt>Type</dt>
<dd>

<a href="#discord.Component" title="discord.Component"><code>Component</code></a>

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.SectionComponent.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.SectionComponent.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### ThumbnailComponent ¶

Attributes

- [description](#discord.ThumbnailComponent.description)
- [id](#discord.ThumbnailComponent.id)
- [media](#discord.ThumbnailComponent.media)
- [spoiler](#discord.ThumbnailComponent.spoiler)
- [type](#discord.ThumbnailComponent.type)

<dl><dt>*class*discord.ThumbnailComponent<a href="#discord.ThumbnailComponent" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a Thumbnail from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type to create a thumbnail is <a href="#discord.ui.Thumbnail" title="discord.ui.Thumbnail"><code>discord.ui.Thumbnail</code></a> not this one.

New in version 2.6.

<dl><dt>media<a href="#discord.ThumbnailComponent.media" title="Permalink to this definition">¶</a></dt>
<dd>

The media for this thumbnail.

<dl><dt>Type</dt>
<dd>

<a href="#discord.UnfurledMediaItem" title="discord.UnfurledMediaItem"><code>UnfurledMediaItem</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.ThumbnailComponent.description" title="Permalink to this definition">¶</a></dt>
<dd>

The description shown within this thumbnail.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>spoiler<a href="#discord.ThumbnailComponent.spoiler" title="Permalink to this definition">¶</a></dt>
<dd>

Whether this thumbnail is flagged as a spoiler.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.ThumbnailComponent.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.ThumbnailComponent.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### TextDisplay ¶

Attributes

- [content](#discord.TextDisplay.content)
- [id](#discord.TextDisplay.id)
- [type](#discord.TextDisplay.type)

<dl><dt>*class*discord.TextDisplay<a href="#discord.TextDisplay" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a text display from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type to create a text display is <a href="#discord.ui.TextDisplay" title="discord.ui.TextDisplay"><code>discord.ui.TextDisplay</code></a> not this one.

New in version 2.6.

<dl><dt>content<a href="#discord.TextDisplay.content" title="Permalink to this definition">¶</a></dt>
<dd>

The content that this display shows.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.TextDisplay.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.TextDisplay.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### MediaGalleryComponent ¶

Attributes

- [id](#discord.MediaGalleryComponent.id)
- [items](#discord.MediaGalleryComponent.items)
- [type](#discord.MediaGalleryComponent.type)

<dl><dt>*class*discord.MediaGalleryComponent<a href="#discord.MediaGalleryComponent" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a Media Gallery component from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type for creating a media gallery is <a href="#discord.ui.MediaGallery" title="discord.ui.MediaGallery"><code>discord.ui.MediaGallery</code></a> not this one.

New in version 2.6.

<dl><dt>items<a href="#discord.MediaGalleryComponent.items" title="Permalink to this definition">¶</a></dt>
<dd>

The items this gallery has.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.MediaGalleryItem" title="discord.MediaGalleryItem"><code>MediaGalleryItem</code></a>]

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.MediaGalleryComponent.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.MediaGalleryComponent.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### FileComponent ¶

Attributes

- [id](#discord.FileComponent.id)
- [media](#discord.FileComponent.media)
- [name](#discord.FileComponent.name)
- [size](#discord.FileComponent.size)
- [spoiler](#discord.FileComponent.spoiler)
- [type](#discord.FileComponent.type)

<dl><dt>*class*discord.FileComponent<a href="#discord.FileComponent" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a File component from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type for create a file component is <a href="#discord.ui.File" title="discord.ui.File"><code>discord.ui.File</code></a> not this one.

New in version 2.6.

<dl><dt>media<a href="#discord.FileComponent.media" title="Permalink to this definition">¶</a></dt>
<dd>

The unfurled attachment contents of the file.

<dl><dt>Type</dt>
<dd>

<a href="#discord.UnfurledMediaItem" title="discord.UnfurledMediaItem"><code>UnfurledMediaItem</code></a>

</dd></dl></dd>
</dl><dl><dt>spoiler<a href="#discord.FileComponent.spoiler" title="Permalink to this definition">¶</a></dt>
<dd>

Whether this file is flagged as a spoiler.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.FileComponent.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>name<a href="#discord.FileComponent.name" title="Permalink to this definition">¶</a></dt>
<dd>

The displayed file name, only available when received from the API.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>size<a href="#discord.FileComponent.size" title="Permalink to this definition">¶</a></dt>
<dd>

The file size in MiB, only available when received from the API.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.FileComponent.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### SeparatorComponent ¶

Attributes

- [id](#discord.SeparatorComponent.id)
- [spacing](#discord.SeparatorComponent.spacing)
- [type](#discord.SeparatorComponent.type)
- [visible](#discord.SeparatorComponent.visible)

<dl><dt>*class*discord.SeparatorComponent<a href="#discord.SeparatorComponent" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a Separator from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type for creating a separator is <a href="#discord.ui.Separator" title="discord.ui.Separator"><code>discord.ui.Separator</code></a> not this one.

New in version 2.6.

<dl><dt>spacing<a href="#discord.SeparatorComponent.spacing" title="Permalink to this definition">¶</a></dt>
<dd>

The spacing size of the separator.

<dl><dt>Type</dt>
<dd>

<a href="#discord.SeparatorSpacing" title="discord.SeparatorSpacing"><code>SeparatorSpacing</code></a>

</dd></dl></dd>
</dl><dl><dt>visible<a href="#discord.SeparatorComponent.visible" title="Permalink to this definition">¶</a></dt>
<dd>

Whether this separator is visible and shows a divider.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.SeparatorComponent.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.SeparatorComponent.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### Container ¶

Attributes

- [accent\_color](#discord.Container.accent_color)
- [accent\_colour](#discord.Container.accent_colour)
- [children](#discord.Container.children)
- [id](#discord.Container.id)
- [spoiler](#discord.Container.spoiler)
- [type](#discord.Container.type)

<dl><dt>*class*discord.Container<a href="#discord.Container" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a Container from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type for creating a container is <a href="#discord.ui.Container" title="discord.ui.Container"><code>discord.ui.Container</code></a> not this one.

New in version 2.6.

<dl><dt>children<a href="#discord.Container.children" title="Permalink to this definition">¶</a></dt>
<dd>

This container’s children.

<dl><dt>Type</dt>
<dd>

<a href="#discord.Component" title="discord.Component"><code>Component</code></a>

</dd></dl></dd>
</dl><dl><dt>spoiler<a href="#discord.Container.spoiler" title="Permalink to this definition">¶</a></dt>
<dd>

Whether this container is flagged as a spoiler.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.Container.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*accent_colour<a href="#discord.Container.accent_colour" title="Permalink to this definition">¶</a></dt>
<dd>

The container’s accent colour.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Colour" title="discord.Colour"><code>Colour</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*accent_color<a href="#discord.Container.accent_color" title="Permalink to this definition">¶</a></dt>
<dd>

The container’s accent colour.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Colour" title="discord.Colour"><code>Colour</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.Container.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### FileUploadComponent ¶

Attributes

- [custom\_id](#discord.FileUploadComponent.custom_id)
- [id](#discord.FileUploadComponent.id)
- [max\_values](#discord.FileUploadComponent.max_values)
- [min\_values](#discord.FileUploadComponent.min_values)
- [required](#discord.FileUploadComponent.required)
- [type](#discord.FileUploadComponent.type)

<dl><dt>*class*discord.FileUploadComponent<a href="#discord.FileUploadComponent" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a file upload component from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type for creating a file upload is <a href="#discord.ui.FileUpload" title="discord.ui.FileUpload"><code>discord.ui.FileUpload</code></a> not this one.

New in version 2.7.

<dl><dt>custom_id<a href="#discord.FileUploadComponent.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the component that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>min_values<a href="#discord.FileUploadComponent.min_values" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum number of files that must be uploaded for this component. Defaults to 1 and must be between 0 and 10.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>max_values<a href="#discord.FileUploadComponent.max_values" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of files that must be uploaded for this component. Defaults to 1 and must be between 1 and 10.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.FileUploadComponent.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>required<a href="#discord.FileUploadComponent.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the component is required. Defaults to <code>True</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.FileUploadComponent.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### RadioGroupComponent ¶

Attributes

- [custom\_id](#discord.RadioGroupComponent.custom_id)
- [id](#discord.RadioGroupComponent.id)
- [options](#discord.RadioGroupComponent.options)
- [required](#discord.RadioGroupComponent.required)
- [type](#discord.RadioGroupComponent.type)

<dl><dt>*class*discord.RadioGroupComponent<a href="#discord.RadioGroupComponent" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a radio group component from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type for creating a radio group is <a href="#discord.ui.RadioGroup" title="discord.ui.RadioGroup"><code>discord.ui.RadioGroup</code></a> not this one.

New in version 2.7.

<dl><dt>custom_id<a href="#discord.RadioGroupComponent.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the component that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.RadioGroupComponent.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>required<a href="#discord.RadioGroupComponent.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the component is required. Defaults to <code>True</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>options<a href="#discord.RadioGroupComponent.options" title="Permalink to this definition">¶</a></dt>
<dd>

A list of options that can be selected in this group.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.RadioGroupOption" title="discord.RadioGroupOption"><code>RadioGroupOption</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.RadioGroupComponent.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### CheckboxComponent ¶

Attributes

- [custom\_id](#discord.CheckboxComponent.custom_id)
- [default](#discord.CheckboxComponent.default)
- [id](#discord.CheckboxComponent.id)
- [type](#discord.CheckboxComponent.type)

<dl><dt>*class*discord.CheckboxComponent<a href="#discord.CheckboxComponent" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a checkbox component from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type for creating a checkbox is <a href="#discord.ui.Checkbox" title="discord.ui.Checkbox"><code>discord.ui.Checkbox</code></a> not this one.

New in version 2.7.

<dl><dt>custom_id<a href="#discord.CheckboxComponent.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the component that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.CheckboxComponent.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>default<a href="#discord.CheckboxComponent.default" title="Permalink to this definition">¶</a></dt>
<dd>

Whether this checkbox is selected by default.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.CheckboxComponent.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### CheckboxGroupComponent ¶

Attributes

- [custom\_id](#discord.CheckboxGroupComponent.custom_id)
- [id](#discord.CheckboxGroupComponent.id)
- [max\_values](#discord.CheckboxGroupComponent.max_values)
- [min\_values](#discord.CheckboxGroupComponent.min_values)
- [options](#discord.CheckboxGroupComponent.options)
- [required](#discord.CheckboxGroupComponent.required)
- [type](#discord.CheckboxGroupComponent.type)

<dl><dt>*class*discord.CheckboxGroupComponent<a href="#discord.CheckboxGroupComponent" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a checkbox group component from the Discord Bot UI Kit.

This inherits from <a href="#discord.Component" title="discord.Component"><code>Component</code></a>.

Note

The user constructible and usable type for creating a checkbox group is <a href="#discord.ui.CheckboxGroup" title="discord.ui.CheckboxGroup"><code>discord.ui.CheckboxGroup</code></a> not this one.

New in version 2.7.

<dl><dt>custom_id<a href="#discord.CheckboxGroupComponent.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the component that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.CheckboxGroupComponent.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>required<a href="#discord.CheckboxGroupComponent.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the component is required. Defaults to <code>True</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>min_values<a href="#discord.CheckboxGroupComponent.min_values" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum number of options that must be selected in this component. Must be between 0 and 10. Defaults to 0.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>max_values<a href="#discord.CheckboxGroupComponent.max_values" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of options that can be selected in this component. Must be between 1 and 10. Defaults to 1.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>options<a href="#discord.CheckboxGroupComponent.options" title="Permalink to this definition">¶</a></dt>
<dd>

A list of options that can be selected in this group.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.CheckboxGroupOption" title="discord.CheckboxGroupOption"><code>CheckboxGroupOption</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.CheckboxGroupComponent.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### AppCommand ¶

Attributes

- [allowed\_contexts](#discord.app_commands.AppCommand.allowed_contexts)
- [allowed\_installs](#discord.app_commands.AppCommand.allowed_installs)
- [application\_id](#discord.app_commands.AppCommand.application_id)
- [default\_member\_permissions](#discord.app_commands.AppCommand.default_member_permissions)
- [description](#discord.app_commands.AppCommand.description)
- [description\_localizations](#discord.app_commands.AppCommand.description_localizations)
- [dm\_permission](#discord.app_commands.AppCommand.dm_permission)
- [guild](#discord.app_commands.AppCommand.guild)
- [guild\_id](#discord.app_commands.AppCommand.guild_id)
- [id](#discord.app_commands.AppCommand.id)
- [mention](#discord.app_commands.AppCommand.mention)
- [name](#discord.app_commands.AppCommand.name)
- [name\_localizations](#discord.app_commands.AppCommand.name_localizations)
- [nsfw](#discord.app_commands.AppCommand.nsfw)
- [options](#discord.app_commands.AppCommand.options)
- [type](#discord.app_commands.AppCommand.type)

Methods

- async [delete](#discord.app_commands.AppCommand.delete)
- async [edit](#discord.app_commands.AppCommand.edit)
- async [fetch\_permissions](#discord.app_commands.AppCommand.fetch_permissions)

<dl><dt>*class*discord.app_commands.AppCommand<a href="#discord.app_commands.AppCommand" title="Permalink to this definition">¶</a></dt>
<dd>

Represents an application command.

In common parlance this is referred to as a “Slash Command” or a “Context Menu Command”.

New in version 2.0.

<dl><dt>x == y</dt>
<dd>

Checks if two application commands are equal.

</dd></dl><dl><dt>x != y</dt>
<dd>

Checks if two application commands are not equal.

</dd></dl><dl><dt>hash(x)</dt>
<dd>

Returns the application command’s hash.

</dd></dl><dl><dt>str(x)</dt>
<dd>

Returns the application command’s name.

</dd></dl>

<dl><dt>id<a href="#discord.app_commands.AppCommand.id" title="Permalink to this definition">¶</a></dt>
<dd>

The application command’s ID.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>application_id<a href="#discord.app_commands.AppCommand.application_id" title="Permalink to this definition">¶</a></dt>
<dd>

The application command’s application’s ID.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.app_commands.AppCommand.type" title="Permalink to this definition">¶</a></dt>
<dd>

The application command’s type.

<dl><dt>Type</dt>
<dd>

<a href="#discord.AppCommandType" title="discord.AppCommandType"><code>AppCommandType</code></a>

</dd></dl></dd>
</dl><dl><dt>name<a href="#discord.app_commands.AppCommand.name" title="Permalink to this definition">¶</a></dt>
<dd>

The application command’s name.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.app_commands.AppCommand.description" title="Permalink to this definition">¶</a></dt>
<dd>

The application command’s description.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>name_localizations<a href="#discord.app_commands.AppCommand.name_localizations" title="Permalink to this definition">¶</a></dt>
<dd>

The localised names of the application command. Used for display purposes.

<dl><dt>Type</dt>
<dd>

Dict\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>description_localizations<a href="#discord.app_commands.AppCommand.description_localizations" title="Permalink to this definition">¶</a></dt>
<dd>

The localised descriptions of the application command. Used for display purposes.

<dl><dt>Type</dt>
<dd>

Dict\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>options<a href="#discord.app_commands.AppCommand.options" title="Permalink to this definition">¶</a></dt>
<dd>

A list of options.

<dl><dt>Type</dt>
<dd>

List\[Union\[<a href="#discord.app_commands.Argument" title="discord.app_commands.Argument"><code>Argument</code></a>, <a href="#discord.app_commands.AppCommandGroup" title="discord.app_commands.AppCommandGroup"><code>AppCommandGroup</code></a>]]

</dd></dl></dd>
</dl><dl><dt>default_member_permissions<a href="#discord.app_commands.AppCommand.default_member_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The default member permissions that can run this command.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>]

</dd></dl></dd>
</dl><dl><dt>dm_permission<a href="#discord.app_commands.AppCommand.dm_permission" title="Permalink to this definition">¶</a></dt>
<dd>

A boolean that indicates whether this command can be run in direct messages.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>allowed_contexts<a href="#discord.app_commands.AppCommand.allowed_contexts" title="Permalink to this definition">¶</a></dt>
<dd>

The contexts that this command is allowed to be used in. Overrides the <code>dm_permission</code> attribute.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.AppCommandContext" title="discord.app_commands.AppCommandContext"><code>AppCommandContext</code></a>]

</dd></dl></dd>
</dl><dl><dt>allowed_installs<a href="#discord.app_commands.AppCommand.allowed_installs" title="Permalink to this definition">¶</a></dt>
<dd>

The installation contexts that this command is allowed to be installed in.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.AppInstallationType" title="discord.app_commands.AppInstallationType"><code>AppInstallationType</code></a>]

</dd></dl></dd>
</dl><dl><dt>guild_id<a href="#discord.app_commands.AppCommand.guild_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the guild this command is registered in. A value of <code>None</code> denotes that it is a global command.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>nsfw<a href="#discord.app_commands.AppCommand.nsfw" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the command is NSFW and should only work in NSFW channels.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*mention<a href="#discord.app_commands.AppCommand.mention" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a string that allows you to mention the given AppCommand.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*guild<a href="#discord.app_commands.AppCommand.guild" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the guild this command is registered to if it exists.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* delete()<a href="#discord.app_commands.AppCommand.delete" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Deletes the application command.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The application command was not found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have permission to delete this application command.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Deleting the application command failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The client does not have an application ID.

</dd></dl></dd>
</dl><dl><dt>*await* edit(***, *name=...*, *description=...*, *default_member_permissions=...*, *dm_permission=...*, *options=...*)<a href="#discord.app_commands.AppCommand.edit" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Edits the application command.

<dl><dt>Parameters</dt>
<dd>

- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The new name for the application command.
- **description** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The new description for the application command.
- **default\_member\_permissions** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>]) – The new default permissions needed to use this application command. Pass value of <code>None</code> to remove any permission requirements.
- **dm\_permission** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Indicates if the application command can be used in DMs.
- **options** (List\[Union\[<a href="#discord.app_commands.Argument" title="discord.app_commands.Argument"><code>Argument</code></a>, <a href="#discord.app_commands.AppCommandGroup" title="discord.app_commands.AppCommandGroup"><code>AppCommandGroup</code></a>]]) – List of new options for this application command.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The application command was not found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have permission to edit this application command.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Editing the application command failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The client does not have an application ID.

</dd><dt>Returns</dt>
<dd>

The newly edited application command.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.app_commands.AppCommand" title="discord.app_commands.AppCommand"><code>AppCommand</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_permissions(*guild*)<a href="#discord.app_commands.AppCommand.fetch_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves this command’s permission in the guild.

<dl><dt>Parameters</dt>
<dd>

**guild** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>) – The guild to retrieve the permissions from.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have permission to fetch the application command’s permissions.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Fetching the application command’s permissions failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The client does not have an application ID.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The application command’s permissions could not be found. This can also indicate that the permissions are synced with the guild (i.e. they are unchanged from the default).

</dd><dt>Returns</dt>
<dd>

An object representing the application command’s permissions in the guild.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.app_commands.GuildAppCommandPermissions" title="discord.app_commands.GuildAppCommandPermissions"><code>GuildAppCommandPermissions</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### AppCommandGroup ¶

Attributes

- [description](#discord.app_commands.AppCommandGroup.description)
- [description\_localizations](#discord.app_commands.AppCommandGroup.description_localizations)
- [mention](#discord.app_commands.AppCommandGroup.mention)
- [name](#discord.app_commands.AppCommandGroup.name)
- [name\_localizations](#discord.app_commands.AppCommandGroup.name_localizations)
- [options](#discord.app_commands.AppCommandGroup.options)
- [parent](#discord.app_commands.AppCommandGroup.parent)
- [qualified\_name](#discord.app_commands.AppCommandGroup.qualified_name)
- [type](#discord.app_commands.AppCommandGroup.type)

<dl><dt>*class*discord.app_commands.AppCommandGroup<a href="#discord.app_commands.AppCommandGroup" title="Permalink to this definition">¶</a></dt>
<dd>

Represents an application command subcommand.

New in version 2.0.

<dl><dt>type<a href="#discord.app_commands.AppCommandGroup.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of subcommand.

<dl><dt>Type</dt>
<dd>

<a href="#discord.AppCommandOptionType" title="discord.AppCommandOptionType"><code>AppCommandOptionType</code></a>

</dd></dl></dd>
</dl><dl><dt>name<a href="#discord.app_commands.AppCommandGroup.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the subcommand.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.app_commands.AppCommandGroup.description" title="Permalink to this definition">¶</a></dt>
<dd>

The description of the subcommand.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>name_localizations<a href="#discord.app_commands.AppCommandGroup.name_localizations" title="Permalink to this definition">¶</a></dt>
<dd>

The localised names of the subcommand. Used for display purposes.

<dl><dt>Type</dt>
<dd>

Dict\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>description_localizations<a href="#discord.app_commands.AppCommandGroup.description_localizations" title="Permalink to this definition">¶</a></dt>
<dd>

The localised descriptions of the subcommand. Used for display purposes.

<dl><dt>Type</dt>
<dd>

Dict\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>options<a href="#discord.app_commands.AppCommandGroup.options" title="Permalink to this definition">¶</a></dt>
<dd>

A list of options.

<dl><dt>Type</dt>
<dd>

List\[Union\[<a href="#discord.app_commands.Argument" title="discord.app_commands.Argument"><code>Argument</code></a>, <a href="#discord.app_commands.AppCommandGroup" title="discord.app_commands.AppCommandGroup"><code>AppCommandGroup</code></a>]]

</dd></dl></dd>
</dl><dl><dt>parent<a href="#discord.app_commands.AppCommandGroup.parent" title="Permalink to this definition">¶</a></dt>
<dd>

The parent application command.

<dl><dt>Type</dt>
<dd>

Union\[<a href="#discord.app_commands.AppCommand" title="discord.app_commands.AppCommand"><code>AppCommand</code></a>, <a href="#discord.app_commands.AppCommandGroup" title="discord.app_commands.AppCommandGroup"><code>AppCommandGroup</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*qualified_name<a href="#discord.app_commands.AppCommandGroup.qualified_name" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the fully qualified command name.

The qualified name includes the parent name as well. For example, in a command like <code>/foo bar</code> the qualified name is <code>foo bar</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*mention<a href="#discord.app_commands.AppCommandGroup.mention" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a string that allows you to mention the given AppCommandGroup.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### AppCommandChannel ¶

Attributes

- [category\_id](#discord.app_commands.AppCommandChannel.category_id)
- [created\_at](#discord.app_commands.AppCommandChannel.created_at)
- [flags](#discord.app_commands.AppCommandChannel.flags)
- [guild](#discord.app_commands.AppCommandChannel.guild)
- [guild\_id](#discord.app_commands.AppCommandChannel.guild_id)
- [id](#discord.app_commands.AppCommandChannel.id)
- [jump\_url](#discord.app_commands.AppCommandChannel.jump_url)
- [last\_message\_id](#discord.app_commands.AppCommandChannel.last_message_id)
- [mention](#discord.app_commands.AppCommandChannel.mention)
- [name](#discord.app_commands.AppCommandChannel.name)
- [nsfw](#discord.app_commands.AppCommandChannel.nsfw)
- [permissions](#discord.app_commands.AppCommandChannel.permissions)
- [position](#discord.app_commands.AppCommandChannel.position)
- [slowmode\_delay](#discord.app_commands.AppCommandChannel.slowmode_delay)
- [topic](#discord.app_commands.AppCommandChannel.topic)
- [type](#discord.app_commands.AppCommandChannel.type)

Methods

- async [fetch](#discord.app_commands.AppCommandChannel.fetch)
- def [is\_news](#discord.app_commands.AppCommandChannel.is_news)
- def [is\_nsfw](#discord.app_commands.AppCommandChannel.is_nsfw)
- def [resolve](#discord.app_commands.AppCommandChannel.resolve)

<dl><dt>*class*discord.app_commands.AppCommandChannel<a href="#discord.app_commands.AppCommandChannel" title="Permalink to this definition">¶</a></dt>
<dd>

Represents an application command partially resolved channel object.

New in version 2.0.

<dl><dt>x == y</dt>
<dd>

Checks if two channels are equal.

</dd></dl><dl><dt>x != y</dt>
<dd>

Checks if two channels are not equal.

</dd></dl><dl><dt>hash(x)</dt>
<dd>

Returns the channel’s hash.

</dd></dl><dl><dt>str(x)</dt>
<dd>

Returns the channel’s name.

</dd></dl>

<dl><dt>id<a href="#discord.app_commands.AppCommandChannel.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the channel.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.app_commands.AppCommandChannel.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of channel.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelType" title="discord.ChannelType"><code>ChannelType</code></a>

</dd></dl></dd>
</dl><dl><dt>name<a href="#discord.app_commands.AppCommandChannel.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the channel.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>permissions<a href="#discord.app_commands.AppCommandChannel.permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The resolved permissions of the user who invoked the application command in that channel.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>

</dd></dl></dd>
</dl><dl><dt>guild_id<a href="#discord.app_commands.AppCommandChannel.guild_id" title="Permalink to this definition">¶</a></dt>
<dd>

The guild ID this channel belongs to.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>category_id<a href="#discord.app_commands.AppCommandChannel.category_id" title="Permalink to this definition">¶</a></dt>
<dd>

The category channel ID this channel belongs to, if applicable.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>topic<a href="#discord.app_commands.AppCommandChannel.topic" title="Permalink to this definition">¶</a></dt>
<dd>

The channel’s topic. <code>None</code> if it doesn’t exist.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>position<a href="#discord.app_commands.AppCommandChannel.position" title="Permalink to this definition">¶</a></dt>
<dd>

The position in the channel list. This is a number that starts at 0. e.g. the top channel is position 0.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>last_message_id<a href="#discord.app_commands.AppCommandChannel.last_message_id" title="Permalink to this definition">¶</a></dt>
<dd>

The last message ID of the message sent to this channel. It may *not* point to an existing or valid message.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>slowmode_delay<a href="#discord.app_commands.AppCommandChannel.slowmode_delay" title="Permalink to this definition">¶</a></dt>
<dd>

The number of seconds a member must wait between sending messages in this channel. A value of <code>0</code> denotes that it is disabled. Bots and users with <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.bypass_slowmode" title="discord.Permissions.bypass_slowmode"><code>bypass_slowmode</code></a> bypass slowmode.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>nsfw<a href="#discord.app_commands.AppCommandChannel.nsfw" title="Permalink to this definition">¶</a></dt>
<dd>

If the channel is marked as “not safe for work” or “age restricted”.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*guild<a href="#discord.app_commands.AppCommandChannel.guild" title="Permalink to this definition">¶</a></dt>
<dd>

The channel’s guild, from cache, if found.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*flags<a href="#discord.app_commands.AppCommandChannel.flags" title="Permalink to this definition">¶</a></dt>
<dd>

The flags associated with this channel object.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelFlags" title="discord.ChannelFlags"><code>ChannelFlags</code></a>

</dd></dl></dd>
</dl><dl><dt>is_nsfw()<a href="#discord.app_commands.AppCommandChannel.is_nsfw" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Checks if the channel is NSFW.

New in version 2.6.

</dd></dl><dl><dt>is_news()<a href="#discord.app_commands.AppCommandChannel.is_news" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Checks if the channel is a news channel.

New in version 2.6.

</dd></dl><dl><dt>resolve()<a href="#discord.app_commands.AppCommandChannel.resolve" title="Permalink to this definition">¶</a></dt>
<dd>

Resolves the application command channel to the appropriate channel from cache if found.

<dl><dt>Returns</dt>
<dd>

The resolved guild channel or <code>None</code> if not found in cache.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* fetch()<a href="#discord.app_commands.AppCommandChannel.fetch" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Fetches the partial channel to a full <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a>.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The channel was not found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the permissions required to get a channel.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the channel failed.

</dd><dt>Returns</dt>
<dd>

The full channel.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*mention<a href="#discord.app_commands.AppCommandChannel.mention" title="Permalink to this definition">¶</a></dt>
<dd>

The string that allows you to mention the channel.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*jump_url<a href="#discord.app_commands.AppCommandChannel.jump_url" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a URL that allows the client to jump to the channel.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*created_at<a href="#discord.app_commands.AppCommandChannel.created_at" title="Permalink to this definition">¶</a></dt>
<dd>

An aware timestamp of when this channel was created in UTC.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### AppCommandThread ¶

Attributes

- [applied\_tags](#discord.app_commands.AppCommandThread.applied_tags)
- [archive\_timestamp](#discord.app_commands.AppCommandThread.archive_timestamp)
- [archived](#discord.app_commands.AppCommandThread.archived)
- [archiver\_id](#discord.app_commands.AppCommandThread.archiver_id)
- [auto\_archive\_duration](#discord.app_commands.AppCommandThread.auto_archive_duration)
- [created\_at](#discord.app_commands.AppCommandThread.created_at)
- [flags](#discord.app_commands.AppCommandThread.flags)
- [guild](#discord.app_commands.AppCommandThread.guild)
- [guild\_id](#discord.app_commands.AppCommandThread.guild_id)
- [id](#discord.app_commands.AppCommandThread.id)
- [invitable](#discord.app_commands.AppCommandThread.invitable)
- [jump\_url](#discord.app_commands.AppCommandThread.jump_url)
- [last\_message\_id](#discord.app_commands.AppCommandThread.last_message_id)
- [locked](#discord.app_commands.AppCommandThread.locked)
- [member\_count](#discord.app_commands.AppCommandThread.member_count)
- [mention](#discord.app_commands.AppCommandThread.mention)
- [message\_count](#discord.app_commands.AppCommandThread.message_count)
- [name](#discord.app_commands.AppCommandThread.name)
- [owner](#discord.app_commands.AppCommandThread.owner)
- [owner\_id](#discord.app_commands.AppCommandThread.owner_id)
- [parent](#discord.app_commands.AppCommandThread.parent)
- [parent\_id](#discord.app_commands.AppCommandThread.parent_id)
- [permissions](#discord.app_commands.AppCommandThread.permissions)
- [slowmode\_delay](#discord.app_commands.AppCommandThread.slowmode_delay)
- [total\_message\_sent](#discord.app_commands.AppCommandThread.total_message_sent)
- [type](#discord.app_commands.AppCommandThread.type)

Methods

- async [fetch](#discord.app_commands.AppCommandThread.fetch)
- def [resolve](#discord.app_commands.AppCommandThread.resolve)

<dl><dt>*class*discord.app_commands.AppCommandThread<a href="#discord.app_commands.AppCommandThread" title="Permalink to this definition">¶</a></dt>
<dd>

Represents an application command partially resolved thread object.

New in version 2.0.

<dl><dt>x == y</dt>
<dd>

Checks if two thread are equal.

</dd></dl><dl><dt>x != y</dt>
<dd>

Checks if two thread are not equal.

</dd></dl><dl><dt>hash(x)</dt>
<dd>

Returns the thread’s hash.

</dd></dl><dl><dt>str(x)</dt>
<dd>

Returns the thread’s name.

</dd></dl>

<dl><dt>id<a href="#discord.app_commands.AppCommandThread.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the thread.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.app_commands.AppCommandThread.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of thread.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelType" title="discord.ChannelType"><code>ChannelType</code></a>

</dd></dl></dd>
</dl><dl><dt>name<a href="#discord.app_commands.AppCommandThread.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the thread.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>parent_id<a href="#discord.app_commands.AppCommandThread.parent_id" title="Permalink to this definition">¶</a></dt>
<dd>

The parent text channel ID this thread belongs to.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>owner_id<a href="#discord.app_commands.AppCommandThread.owner_id" title="Permalink to this definition">¶</a></dt>
<dd>

The user’s ID that created this thread.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>last_message_id<a href="#discord.app_commands.AppCommandThread.last_message_id" title="Permalink to this definition">¶</a></dt>
<dd>

The last message ID of the message sent to this thread. It may *not* point to an existing or valid message.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>slowmode_delay<a href="#discord.app_commands.AppCommandThread.slowmode_delay" title="Permalink to this definition">¶</a></dt>
<dd>

The number of seconds a member must wait between sending messages in this thread. A value of <code>0</code> denotes that it is disabled. Bots and users with <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.bypass_slowmode" title="discord.Permissions.bypass_slowmode"><code>bypass_slowmode</code></a> bypass slowmode.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>message_count<a href="#discord.app_commands.AppCommandThread.message_count" title="Permalink to this definition">¶</a></dt>
<dd>

An approximate number of messages in this thread.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>member_count<a href="#discord.app_commands.AppCommandThread.member_count" title="Permalink to this definition">¶</a></dt>
<dd>

An approximate number of members in this thread. This caps at 50.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>total_message_sent<a href="#discord.app_commands.AppCommandThread.total_message_sent" title="Permalink to this definition">¶</a></dt>
<dd>

The total number of messages sent, including deleted messages.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>permissions<a href="#discord.app_commands.AppCommandThread.permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The resolved permissions of the user who invoked the application command in that thread.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>

</dd></dl></dd>
</dl><dl><dt>guild_id<a href="#discord.app_commands.AppCommandThread.guild_id" title="Permalink to this definition">¶</a></dt>
<dd>

The guild ID this thread belongs to.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>archived<a href="#discord.app_commands.AppCommandThread.archived" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the thread is archived.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>locked<a href="#discord.app_commands.AppCommandThread.locked" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the thread is locked.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>invitable<a href="#discord.app_commands.AppCommandThread.invitable" title="Permalink to this definition">¶</a></dt>
<dd>

Whether non-moderators can add other non-moderators to this thread. This is always <code>True</code> for public threads.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>archiver_id<a href="#discord.app_commands.AppCommandThread.archiver_id" title="Permalink to this definition">¶</a></dt>
<dd>

The user’s ID that archived this thread.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>auto_archive_duration<a href="#discord.app_commands.AppCommandThread.auto_archive_duration" title="Permalink to this definition">¶</a></dt>
<dd>

The duration in minutes until the thread is automatically hidden from the channel list. Usually a value of 60, 1440, 4320 and 10080.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>archive_timestamp<a href="#discord.app_commands.AppCommandThread.archive_timestamp" title="Permalink to this definition">¶</a></dt>
<dd>

An aware timestamp of when the thread’s archived status was last updated in UTC.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*guild<a href="#discord.app_commands.AppCommandThread.guild" title="Permalink to this definition">¶</a></dt>
<dd>

The channel’s guild, from cache, if found.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*applied_tags<a href="#discord.app_commands.AppCommandThread.applied_tags" title="Permalink to this definition">¶</a></dt>
<dd>

A list of tags applied to this thread.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ForumTag" title="discord.ForumTag"><code>ForumTag</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.app_commands.AppCommandThread.parent" title="Permalink to this definition">¶</a></dt>
<dd>

The parent channel this thread belongs to.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ForumChannel" title="discord.ForumChannel"><code>ForumChannel</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.TextChannel" title="discord.TextChannel"><code>TextChannel</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*flags<a href="#discord.app_commands.AppCommandThread.flags" title="Permalink to this definition">¶</a></dt>
<dd>

The flags associated with this thread.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelFlags" title="discord.ChannelFlags"><code>ChannelFlags</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*owner<a href="#discord.app_commands.AppCommandThread.owner" title="Permalink to this definition">¶</a></dt>
<dd>

The member this thread belongs to.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*mention<a href="#discord.app_commands.AppCommandThread.mention" title="Permalink to this definition">¶</a></dt>
<dd>

The string that allows you to mention the thread.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*jump_url<a href="#discord.app_commands.AppCommandThread.jump_url" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a URL that allows the client to jump to the thread.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*created_at<a href="#discord.app_commands.AppCommandThread.created_at" title="Permalink to this definition">¶</a></dt>
<dd>

An aware timestamp of when the thread was created in UTC.

Note

This timestamp only exists for threads created after 9 January 2022, otherwise returns <code>None</code>.

</dd></dl><dl><dt>resolve()<a href="#discord.app_commands.AppCommandThread.resolve" title="Permalink to this definition">¶</a></dt>
<dd>

Resolves the application command channel to the appropriate channel from cache if found.

<dl><dt>Returns</dt>
<dd>

The resolved guild channel or <code>None</code> if not found in cache.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* fetch()<a href="#discord.app_commands.AppCommandThread.fetch" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Fetches the partial channel to a full <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a>.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The thread was not found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the permissions required to get a thread.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the thread failed.

</dd><dt>Returns</dt>
<dd>

The full thread.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### AppCommandPermissions ¶

Attributes

- [guild](#discord.app_commands.AppCommandPermissions.guild)
- [id](#discord.app_commands.AppCommandPermissions.id)
- [permission](#discord.app_commands.AppCommandPermissions.permission)
- [target](#discord.app_commands.AppCommandPermissions.target)
- [type](#discord.app_commands.AppCommandPermissions.type)

<dl><dt>*class*discord.app_commands.AppCommandPermissions<a href="#discord.app_commands.AppCommandPermissions" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the permissions for an application command.

New in version 2.0.

<dl><dt>guild<a href="#discord.app_commands.AppCommandPermissions.guild" title="Permalink to this definition">¶</a></dt>
<dd>

The guild associated with this permission.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.app_commands.AppCommandPermissions.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the permission target, such as a role, channel, or guild. The special <code>guild_id - 1</code> sentinel is used to represent “all channels”.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>target<a href="#discord.app_commands.AppCommandPermissions.target" title="Permalink to this definition">¶</a></dt>
<dd>

The role, user, or channel associated with this permission. This could also be the <a href="#discord.app_commands.AllChannels" title="discord.app_commands.AllChannels"><code>AllChannels</code></a> sentinel type. Falls back to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Object" title="discord.Object"><code>Object</code></a> if the target could not be found in the cache.

<dl><dt>Type</dt>
<dd>

Any

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.app_commands.AppCommandPermissions.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of permission.

<dl><dt>Type</dt>
<dd>

<a href="#discord.AppCommandPermissionType" title="discord.AppCommandPermissionType"><code>AppCommandPermissionType</code></a>

</dd></dl></dd>
</dl><dl><dt>permission<a href="#discord.app_commands.AppCommandPermissions.permission" title="Permalink to this definition">¶</a></dt>
<dd>

The permission value. <code>True</code> for allow, <code>False</code> for deny.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### AppCommandContext ¶

Attributes

- [dm\_channel](#discord.app_commands.AppCommandContext.dm_channel)
- [guild](#discord.app_commands.AppCommandContext.guild)
- [private\_channel](#discord.app_commands.AppCommandContext.private_channel)

<dl><dt>*class*discord.app_commands.AppCommandContext(***, *guild=None*, *dm_channel=None*, *private_channel=None*)<a href="#discord.app_commands.AppCommandContext" title="Permalink to this definition">¶</a></dt>
<dd>

Wraps up the Discord <a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a> execution context.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

- **guild** (Optional\[<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]) – Whether the context allows usage in a guild.
- **dm\_channel** (Optional\[<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]) – Whether the context allows usage in a DM channel.
- **private\_channel** (Optional\[<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]) – Whether the context allows usage in a DM or a GDM channel.

</dd></dl><dl><dt>*property*guild<a href="#discord.app_commands.AppCommandContext.guild" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the context allows usage in a guild.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*dm_channel<a href="#discord.app_commands.AppCommandContext.dm_channel" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the context allows usage in a DM channel.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*private_channel<a href="#discord.app_commands.AppCommandContext.private_channel" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the context allows usage in a DM or a GDM channel.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### AppInstallationType ¶

Attributes

- [guild](#discord.app_commands.AppInstallationType.guild)
- [user](#discord.app_commands.AppInstallationType.user)

<dl><dt>*class*discord.app_commands.AppInstallationType(***, *guild=None*, *user=None*)<a href="#discord.app_commands.AppInstallationType" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the installation location of an application command.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

- **guild** (Optional\[<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]) – Whether the integration is a guild install.
- **user** (Optional\[<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]) – Whether the integration is a user install.

</dd></dl><dl><dt>*property*guild<a href="#discord.app_commands.AppInstallationType.guild" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the integration is a guild install.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*user<a href="#discord.app_commands.AppInstallationType.user" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the integration is a user install.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### GuildAppCommandPermissions ¶

Attributes

- [application\_id](#discord.app_commands.GuildAppCommandPermissions.application_id)
- [command](#discord.app_commands.GuildAppCommandPermissions.command)
- [guild](#discord.app_commands.GuildAppCommandPermissions.guild)
- [guild\_id](#discord.app_commands.GuildAppCommandPermissions.guild_id)
- [id](#discord.app_commands.GuildAppCommandPermissions.id)
- [permissions](#discord.app_commands.GuildAppCommandPermissions.permissions)

<dl><dt>*class*discord.app_commands.GuildAppCommandPermissions<a href="#discord.app_commands.GuildAppCommandPermissions" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the permissions for an application command in a guild.

New in version 2.0.

<dl><dt>application_id<a href="#discord.app_commands.GuildAppCommandPermissions.application_id" title="Permalink to this definition">¶</a></dt>
<dd>

The application ID.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>command<a href="#discord.app_commands.GuildAppCommandPermissions.command" title="Permalink to this definition">¶</a></dt>
<dd>

The application command associated with the permissions.

<dl><dt>Type</dt>
<dd>

<a href="#discord.app_commands.AppCommand" title="discord.app_commands.AppCommand"><code>AppCommand</code></a>

</dd></dl></dd>
</dl><dl><dt>id<a href="#discord.app_commands.GuildAppCommandPermissions.id" title="Permalink to this definition">¶</a></dt>
<dd>

ID of the command or the application ID. When this is the application ID instead of a command ID, the permissions apply to all commands that do not contain explicit overwrites.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>guild_id<a href="#discord.app_commands.GuildAppCommandPermissions.guild_id" title="Permalink to this definition">¶</a></dt>
<dd>

The guild ID associated with the permissions.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>permissions<a href="#discord.app_commands.GuildAppCommandPermissions.permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The permissions, this is a max of 100.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.app_commands.AppCommandPermissions" title="discord.app_commands.AppCommandPermissions"><code>AppCommandPermissions</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*guild<a href="#discord.app_commands.GuildAppCommandPermissions.guild" title="Permalink to this definition">¶</a></dt>
<dd>

The guild associated with the permissions.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### Argument ¶

Attributes

- [autocomplete](#discord.app_commands.Argument.autocomplete)
- [channel\_types](#discord.app_commands.Argument.channel_types)
- [choices](#discord.app_commands.Argument.choices)
- [description](#discord.app_commands.Argument.description)
- [description\_localizations](#discord.app_commands.Argument.description_localizations)
- [max\_length](#discord.app_commands.Argument.max_length)
- [max\_value](#discord.app_commands.Argument.max_value)
- [min\_length](#discord.app_commands.Argument.min_length)
- [min\_value](#discord.app_commands.Argument.min_value)
- [name](#discord.app_commands.Argument.name)
- [name\_localizations](#discord.app_commands.Argument.name_localizations)
- [parent](#discord.app_commands.Argument.parent)
- [required](#discord.app_commands.Argument.required)
- [type](#discord.app_commands.Argument.type)

<dl><dt>*class*discord.app_commands.Argument<a href="#discord.app_commands.Argument" title="Permalink to this definition">¶</a></dt>
<dd>

Represents an application command argument.

New in version 2.0.

<dl><dt>type<a href="#discord.app_commands.Argument.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of argument.

<dl><dt>Type</dt>
<dd>

<a href="#discord.AppCommandOptionType" title="discord.AppCommandOptionType"><code>AppCommandOptionType</code></a>

</dd></dl></dd>
</dl><dl><dt>name<a href="#discord.app_commands.Argument.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the argument.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.app_commands.Argument.description" title="Permalink to this definition">¶</a></dt>
<dd>

The description of the argument.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>name_localizations<a href="#discord.app_commands.Argument.name_localizations" title="Permalink to this definition">¶</a></dt>
<dd>

The localised names of the argument. Used for display purposes.

<dl><dt>Type</dt>
<dd>

Dict\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>description_localizations<a href="#discord.app_commands.Argument.description_localizations" title="Permalink to this definition">¶</a></dt>
<dd>

The localised descriptions of the argument. Used for display purposes.

<dl><dt>Type</dt>
<dd>

Dict\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>required<a href="#discord.app_commands.Argument.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the argument is required.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>choices<a href="#discord.app_commands.Argument.choices" title="Permalink to this definition">¶</a></dt>
<dd>

A list of choices for the command to choose from for this argument.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.app_commands.Choice" title="discord.app_commands.Choice"><code>Choice</code></a>]

</dd></dl></dd>
</dl><dl><dt>parent<a href="#discord.app_commands.Argument.parent" title="Permalink to this definition">¶</a></dt>
<dd>

The parent application command that has this argument.

<dl><dt>Type</dt>
<dd>

Union\[<a href="#discord.app_commands.AppCommand" title="discord.app_commands.AppCommand"><code>AppCommand</code></a>, <a href="#discord.app_commands.AppCommandGroup" title="discord.app_commands.AppCommandGroup"><code>AppCommandGroup</code></a>]

</dd></dl></dd>
</dl><dl><dt>channel_types<a href="#discord.app_commands.Argument.channel_types" title="Permalink to this definition">¶</a></dt>
<dd>

The channel types that are allowed for this parameter.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelType" title="discord.ChannelType"><code>ChannelType</code></a>]

</dd></dl></dd>
</dl><dl><dt>min_value<a href="#discord.app_commands.Argument.min_value" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum supported value for this parameter.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]]

</dd></dl></dd>
</dl><dl><dt>max_value<a href="#discord.app_commands.Argument.max_value" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum supported value for this parameter.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]]

</dd></dl></dd>
</dl><dl><dt>min_length<a href="#discord.app_commands.Argument.min_length" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum allowed length for this parameter.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>max_length<a href="#discord.app_commands.Argument.max_length" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum allowed length for this parameter.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>autocomplete<a href="#discord.app_commands.Argument.autocomplete" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the argument has autocomplete.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### AllChannels ¶

Attributes

- [guild](#discord.app_commands.AllChannels.guild)
- [id](#discord.app_commands.AllChannels.id)

<dl><dt>*class*discord.app_commands.AllChannels<a href="#discord.app_commands.AllChannels" title="Permalink to this definition">¶</a></dt>
<dd>

Represents all channels for application command permissions.

New in version 2.0.

<dl><dt>guild<a href="#discord.app_commands.AllChannels.guild" title="Permalink to this definition">¶</a></dt>
<dd>

The guild the application command permission is for.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*id<a href="#discord.app_commands.AllChannels.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID sentinel used to represent all channels. Equivalent to the guild’s ID minus 1.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

## Data Classes ¶

Similar to [Data Classes](https://discordpy.readthedocs.io/en/stable/api.html#discord-api-data), these can be received and constructed by users.

### SelectOption ¶

Attributes

- [default](#discord.SelectOption.default)
- [description](#discord.SelectOption.description)
- [emoji](#discord.SelectOption.emoji)
- [label](#discord.SelectOption.label)
- [value](#discord.SelectOption.value)

<dl><dt>*class*discord.SelectOption(***, *label*, *value=...*, *description=None*, *emoji=None*, *default=False*)<a href="#discord.SelectOption" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a select menu’s option.

These can be created by users.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **label** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The label of the option. This is displayed to users. Can only be up to 100 characters.
- **value** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The value of the option. This is not displayed to users. If not provided when constructed then it defaults to the label. Can only be up to 100 characters.
- **description** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – An additional description of the option, if any. Can only be up to 100 characters.
- **emoji** (Optional\[Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>]]) – The emoji of the option, if available.
- **default** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this option is selected by default.

</dd></dl><dl><dt>label<a href="#discord.SelectOption.label" title="Permalink to this definition">¶</a></dt>
<dd>

The label of the option. This is displayed to users.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>value<a href="#discord.SelectOption.value" title="Permalink to this definition">¶</a></dt>
<dd>

The value of the option. This is not displayed to users. If not provided when constructed then it defaults to the label.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.SelectOption.description" title="Permalink to this definition">¶</a></dt>
<dd>

An additional description of the option, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>default<a href="#discord.SelectOption.default" title="Permalink to this definition">¶</a></dt>
<dd>

Whether this option is selected by default.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*emoji<a href="#discord.SelectOption.emoji" title="Permalink to this definition">¶</a></dt>
<dd>

The emoji of the option, if available.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>]

</dd></dl></dd>
</dl></dd>
</dl>

### SelectDefaultValue ¶

Attributes

- [type](#discord.SelectDefaultValue.type)

Methods

- cls [SelectDefaultValue.from\_channel](#discord.SelectDefaultValue.from_channel)
- cls [SelectDefaultValue.from\_role](#discord.SelectDefaultValue.from_role)
- cls [SelectDefaultValue.from\_user](#discord.SelectDefaultValue.from_user)

<dl><dt>*class*discord.SelectDefaultValue(***, *id*, *type*)<a href="#discord.SelectDefaultValue" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a select menu’s default value.

These can be created by users.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

- **id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The id of a role, user, or channel.
- **type** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.SelectDefaultValueType" title="discord.SelectDefaultValueType"><code>SelectDefaultValueType</code></a>) – The type of value that <code>id</code> represents.

</dd></dl><dl><dt>*property*type<a href="#discord.SelectDefaultValue.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of value that <code>id</code> represents.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.SelectDefaultValueType" title="discord.SelectDefaultValueType"><code>SelectDefaultValueType</code></a>

</dd></dl></dd>
</dl><dl><dt>*classmethod* from_channel(*channel*, */*)<a href="#discord.SelectDefaultValue.from_channel" title="Permalink to this definition">¶</a></dt>
<dd>

Creates a <a href="#discord.SelectDefaultValue" title="discord.SelectDefaultValue"><code>SelectDefaultValue</code></a> with the type set to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.SelectDefaultValueType.channel" title="discord.SelectDefaultValueType.channel"><code>channel</code></a>.

<dl><dt>Parameters</dt>
<dd>

**channel** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>) – The channel to create the default value for.

</dd><dt>Returns</dt>
<dd>

The default value created with the channel.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.SelectDefaultValue" title="discord.SelectDefaultValue"><code>SelectDefaultValue</code></a>

</dd></dl></dd>
</dl><dl><dt>*classmethod* from_role(*role*, */*)<a href="#discord.SelectDefaultValue.from_role" title="Permalink to this definition">¶</a></dt>
<dd>

Creates a <a href="#discord.SelectDefaultValue" title="discord.SelectDefaultValue"><code>SelectDefaultValue</code></a> with the type set to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.SelectDefaultValueType.role" title="discord.SelectDefaultValueType.role"><code>role</code></a>.

<dl><dt>Parameters</dt>
<dd>

**role** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>) – The role to create the default value for.

</dd><dt>Returns</dt>
<dd>

The default value created with the role.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.SelectDefaultValue" title="discord.SelectDefaultValue"><code>SelectDefaultValue</code></a>

</dd></dl></dd>
</dl><dl><dt>*classmethod* from_user(*user*, */*)<a href="#discord.SelectDefaultValue.from_user" title="Permalink to this definition">¶</a></dt>
<dd>

Creates a <a href="#discord.SelectDefaultValue" title="discord.SelectDefaultValue"><code>SelectDefaultValue</code></a> with the type set to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.SelectDefaultValueType.user" title="discord.SelectDefaultValueType.user"><code>user</code></a>.

<dl><dt>Parameters</dt>
<dd>

**user** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>) – The user to create the default value for.

</dd><dt>Returns</dt>
<dd>

The default value created with the user.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.SelectDefaultValue" title="discord.SelectDefaultValue"><code>SelectDefaultValue</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### Choice ¶

<dl><dt>*class*discord.app_commands.Choice(***, *name*, *value*)<a href="#discord.app_commands.Choice" title="Permalink to this definition">¶</a></dt>
<dd>

Represents an application command argument choice.

New in version 2.0.

<dl><dt>x == y</dt>
<dd>

Checks if two choices are equal.

</dd></dl><dl><dt>x != y</dt>
<dd>

Checks if two choices are not equal.

</dd></dl><dl><dt>hash(x)</dt>
<dd>

Returns the choice’s hash.

</dd></dl>

<dl><dt>Parameters</dt>
<dd>

- **name** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The name of the choice. Used for display purposes. Can only be up to 100 characters.
- **name\_localizations** (Dict\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The localised names of the choice. Used for display purposes.
- **value** (Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – The value of the choice. If it’s a string, it can only be up to 100 characters long.

</dd></dl></dd>
</dl>

### UnfurledMediaItem ¶

Attributes

- [attachment\_id](#discord.UnfurledMediaItem.attachment_id)
- [content\_type](#discord.UnfurledMediaItem.content_type)
- [flags](#discord.UnfurledMediaItem.flags)
- [height](#discord.UnfurledMediaItem.height)
- [loading\_state](#discord.UnfurledMediaItem.loading_state)
- [placeholder](#discord.UnfurledMediaItem.placeholder)
- [proxy\_url](#discord.UnfurledMediaItem.proxy_url)
- [url](#discord.UnfurledMediaItem.url)
- [width](#discord.UnfurledMediaItem.width)

<dl><dt>*class*discord.UnfurledMediaItem(*url*)<a href="#discord.UnfurledMediaItem" title="Permalink to this definition">¶</a></dt>
<dd>

Represents an unfurled media item.

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

**url** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The URL of this media item. This can be an arbitrary url or a reference to a local file uploaded as an attachment within the message, which can be accessed with the <code>attachment://&lt;filename&gt;</code> format.

</dd></dl><dl><dt>url<a href="#discord.UnfurledMediaItem.url" title="Permalink to this definition">¶</a></dt>
<dd>

The URL of this media item.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>proxy_url<a href="#discord.UnfurledMediaItem.proxy_url" title="Permalink to this definition">¶</a></dt>
<dd>

The proxy URL. This is a cached version of the <a href="#discord.UnfurledMediaItem.url" title="discord.UnfurledMediaItem.url"><code>url</code></a> in the case of images. When the message is deleted, this URL might be valid for a few minutes or not valid at all.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>height<a href="#discord.UnfurledMediaItem.height" title="Permalink to this definition">¶</a></dt>
<dd>

The media item’s height, in pixels. Only applicable to images and videos.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>width<a href="#discord.UnfurledMediaItem.width" title="Permalink to this definition">¶</a></dt>
<dd>

The media item’s width, in pixels. Only applicable to images and videos.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>content_type<a href="#discord.UnfurledMediaItem.content_type" title="Permalink to this definition">¶</a></dt>
<dd>

The media item’s <a href="https://en.wikipedia.org/wiki/Media_type">media type</a>

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>placeholder<a href="#discord.UnfurledMediaItem.placeholder" title="Permalink to this definition">¶</a></dt>
<dd>

The media item’s placeholder.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>loading_state<a href="#discord.UnfurledMediaItem.loading_state" title="Permalink to this definition">¶</a></dt>
<dd>

The loading state of this media item.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MediaItemLoadingState" title="discord.MediaItemLoadingState"><code>MediaItemLoadingState</code></a>]

</dd></dl></dd>
</dl><dl><dt>attachment_id<a href="#discord.UnfurledMediaItem.attachment_id" title="Permalink to this definition">¶</a></dt>
<dd>

The attachment id this media item points to, only available if the url points to a local file uploaded within the component message.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*flags<a href="#discord.UnfurledMediaItem.flags" title="Permalink to this definition">¶</a></dt>
<dd>

This media item’s flags.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AttachmentFlags" title="discord.AttachmentFlags"><code>AttachmentFlags</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### MediaGalleryItem ¶

Attributes

- [media](#discord.MediaGalleryItem.media)

<dl><dt>*class*discord.MediaGalleryItem(*media*, ***, *description=...*, *spoiler=...*)<a href="#discord.MediaGalleryItem" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a <a href="#discord.MediaGalleryComponent" title="discord.MediaGalleryComponent"><code>MediaGalleryComponent</code></a> media item.

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

- **media** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>discord.File</code></a>, <a href="#discord.UnfurledMediaItem" title="discord.UnfurledMediaItem"><code>UnfurledMediaItem</code></a>]) – The media item data. This can be a string representing a local file uploaded as an attachment in the message, which can be accessed using the <code>attachment://&lt;filename&gt;</code> format, or an arbitrary url.
- **description** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The description to show within this item. Up to 256 characters. Defaults to <code>None</code>.
- **spoiler** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this item should be flagged as a spoiler.

</dd></dl><dl><dt>*property*media<a href="#discord.MediaGalleryItem.media" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s media data.

<dl><dt>Type</dt>
<dd>

<a href="#discord.UnfurledMediaItem" title="discord.UnfurledMediaItem"><code>UnfurledMediaItem</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### RadioGroupOption ¶

Attributes

- [default](#discord.RadioGroupOption.default)
- [description](#discord.RadioGroupOption.description)
- [label](#discord.RadioGroupOption.label)
- [value](#discord.RadioGroupOption.value)

<dl><dt>*class*discord.RadioGroupOption<a href="#discord.RadioGroupOption" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a radio group’s option

These can be created by users.

New in version 2.7.

<dl><dt>Parameters</dt>
<dd>

- **label** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The label of the option. This is displayed to users. Can only be up to 100 characters.
- **value** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The value of the option. This is not displayed to users. If not provided when constructed then it defaults to the label. Can only be up to 100 characters.
- **description** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – An additional description of the option, if any. Can only be up to 100 characters.
- **default** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this option is selected by default.

</dd></dl><dl><dt>label<a href="#discord.RadioGroupOption.label" title="Permalink to this definition">¶</a></dt>
<dd>

The label of the option. This is displayed to users.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>value<a href="#discord.RadioGroupOption.value" title="Permalink to this definition">¶</a></dt>
<dd>

The value of the option. This is not displayed to users. If not provided when constructed then it defaults to the label.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.RadioGroupOption.description" title="Permalink to this definition">¶</a></dt>
<dd>

An additional description of the option, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>default<a href="#discord.RadioGroupOption.default" title="Permalink to this definition">¶</a></dt>
<dd>

Whether this option is selected by default.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### CheckboxGroupOption ¶

Attributes

- [default](#discord.CheckboxGroupOption.default)
- [description](#discord.CheckboxGroupOption.description)
- [label](#discord.CheckboxGroupOption.label)
- [value](#discord.CheckboxGroupOption.value)

<dl><dt>*class*discord.CheckboxGroupOption<a href="#discord.CheckboxGroupOption" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a checkbox group’s option

These can be created by users.

New in version 2.7.

<dl><dt>Parameters</dt>
<dd>

- **label** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The label of the option. This is displayed to users. Can only be up to 100 characters.
- **value** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The value of the option. This is not displayed to users. If not provided when constructed then it defaults to the label. Can only be up to 100 characters.
- **description** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – An additional description of the option, if any. Can only be up to 100 characters.
- **default** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this option is selected by default.

</dd></dl><dl><dt>label<a href="#discord.CheckboxGroupOption.label" title="Permalink to this definition">¶</a></dt>
<dd>

The label of the option. This is displayed to users.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>value<a href="#discord.CheckboxGroupOption.value" title="Permalink to this definition">¶</a></dt>
<dd>

The value of the option. This is not displayed to users. If not provided when constructed then it defaults to the label.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.CheckboxGroupOption.description" title="Permalink to this definition">¶</a></dt>
<dd>

An additional description of the option, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>default<a href="#discord.CheckboxGroupOption.default" title="Permalink to this definition">¶</a></dt>
<dd>

Whether this option is selected by default.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

## Enumerations ¶

<dl><dt>*class*discord.InteractionType<a href="#discord.InteractionType" title="Permalink to this definition">¶</a></dt>
<dd>

Specifies the type of <a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>.

New in version 2.0.

<dl><dt>ping<a href="#discord.InteractionType.ping" title="Permalink to this definition">¶</a></dt>
<dd>

Represents Discord pinging to see if the interaction response server is alive.

</dd></dl><dl><dt>application_command<a href="#discord.InteractionType.application_command" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a slash command interaction.

</dd></dl><dl><dt>component<a href="#discord.InteractionType.component" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a component based interaction, i.e. using the Discord Bot UI Kit.

</dd></dl><dl><dt>autocomplete<a href="#discord.InteractionType.autocomplete" title="Permalink to this definition">¶</a></dt>
<dd>

Represents an auto complete interaction.

</dd></dl><dl><dt>modal_submit<a href="#discord.InteractionType.modal_submit" title="Permalink to this definition">¶</a></dt>
<dd>

Represents submission of a modal interaction.

</dd></dl></dd>
</dl><dl><dt>*class*discord.InteractionResponseType<a href="#discord.InteractionResponseType" title="Permalink to this definition">¶</a></dt>
<dd>

Specifies the response type for the interaction.

New in version 2.0.

<dl><dt>pong<a href="#discord.InteractionResponseType.pong" title="Permalink to this definition">¶</a></dt>
<dd>

Pongs the interaction when given a ping.

See also <a href="#discord.InteractionResponse.pong" title="discord.InteractionResponse.pong"><code>InteractionResponse.pong()</code></a>

</dd></dl><dl><dt>channel_message<a href="#discord.InteractionResponseType.channel_message" title="Permalink to this definition">¶</a></dt>
<dd>

Respond to the interaction with a message.

See also <a href="#discord.InteractionResponse.send_message" title="discord.InteractionResponse.send_message"><code>InteractionResponse.send_message()</code></a>

</dd></dl><dl><dt>deferred_channel_message<a href="#discord.InteractionResponseType.deferred_channel_message" title="Permalink to this definition">¶</a></dt>
<dd>

Responds to the interaction with a message at a later time.

See also <a href="#discord.InteractionResponse.defer" title="discord.InteractionResponse.defer"><code>InteractionResponse.defer()</code></a>

</dd></dl><dl><dt>deferred_message_update<a href="#discord.InteractionResponseType.deferred_message_update" title="Permalink to this definition">¶</a></dt>
<dd>

Acknowledges the component interaction with a promise that the message will update later (though there is no need to actually update the message).

See also <a href="#discord.InteractionResponse.defer" title="discord.InteractionResponse.defer"><code>InteractionResponse.defer()</code></a>

</dd></dl><dl><dt>message_update<a href="#discord.InteractionResponseType.message_update" title="Permalink to this definition">¶</a></dt>
<dd>

Responds to the interaction by editing the message.

See also <a href="#discord.InteractionResponse.edit_message" title="discord.InteractionResponse.edit_message"><code>InteractionResponse.edit_message()</code></a>

</dd></dl><dl><dt>autocomplete_result<a href="#discord.InteractionResponseType.autocomplete_result" title="Permalink to this definition">¶</a></dt>
<dd>

Responds to the autocomplete interaction with suggested choices.

See also <a href="#discord.InteractionResponse.autocomplete" title="discord.InteractionResponse.autocomplete"><code>InteractionResponse.autocomplete()</code></a>

</dd></dl><dl><dt>modal<a href="#discord.InteractionResponseType.modal" title="Permalink to this definition">¶</a></dt>
<dd>

Responds to the interaction with a modal.

See also <a href="#discord.InteractionResponse.send_modal" title="discord.InteractionResponse.send_modal"><code>InteractionResponse.send_modal()</code></a>

</dd></dl></dd>
</dl><dl><dt>*class*discord.ComponentType<a href="#discord.ComponentType" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the component type of a component.

New in version 2.0.

<dl><dt>action_row<a href="#discord.ComponentType.action_row" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a component which holds different components in a row.

</dd></dl><dl><dt>button<a href="#discord.ComponentType.button" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a button component.

</dd></dl><dl><dt>text_input<a href="#discord.ComponentType.text_input" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a text box component.

</dd></dl><dl><dt>select<a href="#discord.ComponentType.select" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a select component.

</dd></dl><dl><dt>string_select<a href="#discord.ComponentType.string_select" title="Permalink to this definition">¶</a></dt>
<dd>

An alias to <a href="#discord.ComponentType.select" title="discord.ComponentType.select"><code>select</code></a>. Represents a default select component.

</dd></dl><dl><dt>user_select<a href="#discord.ComponentType.user_select" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a user select component.

</dd></dl><dl><dt>role_select<a href="#discord.ComponentType.role_select" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a role select component.

</dd></dl><dl><dt>mentionable_select<a href="#discord.ComponentType.mentionable_select" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a select in which both users and roles can be selected.

</dd></dl><dl><dt>channel_select<a href="#discord.ComponentType.channel_select" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a channel select component.

</dd></dl><dl><dt>section<a href="#discord.ComponentType.section" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a component which holds different components in a section.

New in version 2.6.

</dd></dl><dl><dt>text_display<a href="#discord.ComponentType.text_display" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a text display component.

New in version 2.6.

</dd></dl><dl><dt>thumbnail<a href="#discord.ComponentType.thumbnail" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a thumbnail component.

New in version 2.6.

</dd></dl><dl><dt>media_gallery<a href="#discord.ComponentType.media_gallery" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a media gallery component.

New in version 2.6.

</dd></dl><dl><dt>file<a href="#discord.ComponentType.file" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a file component.

New in version 2.6.

</dd></dl><dl><dt>separator<a href="#discord.ComponentType.separator" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a separator component.

New in version 2.6.

</dd></dl><dl><dt>container<a href="#discord.ComponentType.container" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a component which holds different components in a container.

New in version 2.6.

</dd></dl><dl><dt>label<a href="#discord.ComponentType.label" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a label container component, usually in a modal.

New in version 2.6.

</dd></dl><dl><dt>file_upload<a href="#discord.ComponentType.file_upload" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a file upload component, usually in a modal.

> New in version 2.7.

</dd></dl><dl><dt>radio_group<a href="#discord.ComponentType.radio_group" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a radio group component.

New in version 2.7.

</dd></dl><dl><dt>checkbox_group<a href="#discord.ComponentType.checkbox_group" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a checkbox group component.

New in version 2.7.

</dd></dl><dl><dt>checkbox<a href="#discord.ComponentType.checkbox" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a checkbox component.

New in version 2.7.

</dd></dl></dd>
</dl><dl><dt>*class*discord.ButtonStyle<a href="#discord.ButtonStyle" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the style of the button component.

New in version 2.0.

<dl><dt>primary<a href="#discord.ButtonStyle.primary" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a blurple button for the primary action.

</dd></dl><dl><dt>secondary<a href="#discord.ButtonStyle.secondary" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a grey button for the secondary action.

</dd></dl><dl><dt>success<a href="#discord.ButtonStyle.success" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a green button for a successful action.

</dd></dl><dl><dt>danger<a href="#discord.ButtonStyle.danger" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a red button for a dangerous action.

</dd></dl><dl><dt>link<a href="#discord.ButtonStyle.link" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a link button.

</dd></dl><dl><dt>premium<a href="#discord.ButtonStyle.premium" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a button denoting that buying a SKU is required to perform this action.

New in version 2.4.

</dd></dl><dl><dt>blurple<a href="#discord.ButtonStyle.blurple" title="Permalink to this definition">¶</a></dt>
<dd>

An alias for <a href="#discord.ButtonStyle.primary" title="discord.ButtonStyle.primary"><code>primary</code></a>.

</dd></dl><dl><dt>grey<a href="#discord.ButtonStyle.grey" title="Permalink to this definition">¶</a></dt>
<dd>

An alias for <a href="#discord.ButtonStyle.secondary" title="discord.ButtonStyle.secondary"><code>secondary</code></a>.

</dd></dl><dl><dt>gray<a href="#discord.ButtonStyle.gray" title="Permalink to this definition">¶</a></dt>
<dd>

An alias for <a href="#discord.ButtonStyle.secondary" title="discord.ButtonStyle.secondary"><code>secondary</code></a>.

</dd></dl><dl><dt>green<a href="#discord.ButtonStyle.green" title="Permalink to this definition">¶</a></dt>
<dd>

An alias for <a href="#discord.ButtonStyle.success" title="discord.ButtonStyle.success"><code>success</code></a>.

</dd></dl><dl><dt>red<a href="#discord.ButtonStyle.red" title="Permalink to this definition">¶</a></dt>
<dd>

An alias for <a href="#discord.ButtonStyle.danger" title="discord.ButtonStyle.danger"><code>danger</code></a>.

</dd></dl><dl><dt>url<a href="#discord.ButtonStyle.url" title="Permalink to this definition">¶</a></dt>
<dd>

An alias for <a href="#discord.ButtonStyle.link" title="discord.ButtonStyle.link"><code>link</code></a>.

</dd></dl></dd>
</dl><dl><dt>*class*discord.TextStyle<a href="#discord.TextStyle" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the style of the text box component.

New in version 2.0.

<dl><dt>short<a href="#discord.TextStyle.short" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a short text box.

</dd></dl><dl><dt>paragraph<a href="#discord.TextStyle.paragraph" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a long form text box.

</dd></dl><dl><dt>long<a href="#discord.TextStyle.long" title="Permalink to this definition">¶</a></dt>
<dd>

An alias for <a href="#discord.TextStyle.paragraph" title="discord.TextStyle.paragraph"><code>paragraph</code></a>.

</dd></dl></dd>
</dl><dl><dt>*class*discord.AppCommandOptionType<a href="#discord.AppCommandOptionType" title="Permalink to this definition">¶</a></dt>
<dd>

The application command’s option type. This is usually the type of parameter an application command takes.

New in version 2.0.

<dl><dt>subcommand<a href="#discord.AppCommandOptionType.subcommand" title="Permalink to this definition">¶</a></dt>
<dd>

A subcommand.

</dd></dl><dl><dt>subcommand_group<a href="#discord.AppCommandOptionType.subcommand_group" title="Permalink to this definition">¶</a></dt>
<dd>

A subcommand group.

</dd></dl><dl><dt>string<a href="#discord.AppCommandOptionType.string" title="Permalink to this definition">¶</a></dt>
<dd>

A string parameter.

</dd></dl><dl><dt>integer<a href="#discord.AppCommandOptionType.integer" title="Permalink to this definition">¶</a></dt>
<dd>

A integer parameter.

</dd></dl><dl><dt>boolean<a href="#discord.AppCommandOptionType.boolean" title="Permalink to this definition">¶</a></dt>
<dd>

A boolean parameter.

</dd></dl><dl><dt>user<a href="#discord.AppCommandOptionType.user" title="Permalink to this definition">¶</a></dt>
<dd>

A user parameter.

</dd></dl><dl><dt>channel<a href="#discord.AppCommandOptionType.channel" title="Permalink to this definition">¶</a></dt>
<dd>

A channel parameter.

</dd></dl><dl><dt>role<a href="#discord.AppCommandOptionType.role" title="Permalink to this definition">¶</a></dt>
<dd>

A role parameter.

</dd></dl><dl><dt>mentionable<a href="#discord.AppCommandOptionType.mentionable" title="Permalink to this definition">¶</a></dt>
<dd>

A mentionable parameter.

</dd></dl><dl><dt>number<a href="#discord.AppCommandOptionType.number" title="Permalink to this definition">¶</a></dt>
<dd>

A number parameter.

</dd></dl><dl><dt>attachment<a href="#discord.AppCommandOptionType.attachment" title="Permalink to this definition">¶</a></dt>
<dd>

An attachment parameter.

</dd></dl></dd>
</dl><dl><dt>*class*discord.AppCommandType<a href="#discord.AppCommandType" title="Permalink to this definition">¶</a></dt>
<dd>

The type of application command.

New in version 2.0.

<dl><dt>chat_input<a href="#discord.AppCommandType.chat_input" title="Permalink to this definition">¶</a></dt>
<dd>

A slash command.

</dd></dl><dl><dt>user<a href="#discord.AppCommandType.user" title="Permalink to this definition">¶</a></dt>
<dd>

A user context menu command.

</dd></dl><dl><dt>message<a href="#discord.AppCommandType.message" title="Permalink to this definition">¶</a></dt>
<dd>

A message context menu command.

</dd></dl></dd>
</dl><dl><dt>*class*discord.AppCommandPermissionType<a href="#discord.AppCommandPermissionType" title="Permalink to this definition">¶</a></dt>
<dd>

The application command’s permission type.

New in version 2.0.

<dl><dt>role<a href="#discord.AppCommandPermissionType.role" title="Permalink to this definition">¶</a></dt>
<dd>

The permission is for a role.

</dd></dl><dl><dt>channel<a href="#discord.AppCommandPermissionType.channel" title="Permalink to this definition">¶</a></dt>
<dd>

The permission is for one or all channels.

</dd></dl><dl><dt>user<a href="#discord.AppCommandPermissionType.user" title="Permalink to this definition">¶</a></dt>
<dd>

The permission is for a user.

</dd></dl></dd>
</dl><dl><dt>*class*discord.SeparatorSpacing<a href="#discord.SeparatorSpacing" title="Permalink to this definition">¶</a></dt>
<dd>

The separator’s size type.

New in version 2.6.

<dl><dt>small<a href="#discord.SeparatorSpacing.small" title="Permalink to this definition">¶</a></dt>
<dd>

A small separator.

</dd></dl><dl><dt>large<a href="#discord.SeparatorSpacing.large" title="Permalink to this definition">¶</a></dt>
<dd>

A large separator.

</dd></dl></dd>
</dl>

## Bot UI Kit ¶

The library has helpers to aid in creating component-based UIs. These are all in the `discord.ui` package.

### View ¶

Attributes

- [children](#discord.ui.View.children)
- [timeout](#discord.ui.View.timeout)
- [total\_children\_count](#discord.ui.View.total_children_count)

Methods

- cls [View.from\_message](#discord.ui.View.from_message)
- def [add\_item](#discord.ui.View.add_item)
- def [clear\_items](#discord.ui.View.clear_items)
- def [find\_item](#discord.ui.View.find_item)
- async [interaction\_check](#discord.ui.View.interaction_check)
- def [is\_dispatching](#discord.ui.View.is_dispatching)
- def [is\_finished](#discord.ui.View.is_finished)
- def [is\_persistent](#discord.ui.View.is_persistent)
- async [on\_error](#discord.ui.View.on_error)
- async [on\_timeout](#discord.ui.View.on_timeout)
- def [remove\_item](#discord.ui.View.remove_item)
- def [stop](#discord.ui.View.stop)
- async [wait](#discord.ui.View.wait)
- def [walk\_children](#discord.ui.View.walk_children)

<dl><dt>*class*discord.ui.View(***, *timeout=180.0*)<a href="#discord.ui.View" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI view.

This object must be inherited to create a UI within Discord.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

**timeout** (Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – Timeout in seconds from last interaction with the UI before no longer accepting input. If <code>None</code> then there is no timeout.

</dd></dl><dl><dt>*classmethod* from_message(*message*, */*, ***, *timeout=180.0*)<a href="#discord.ui.View.from_message" title="Permalink to this definition">¶</a></dt>
<dd>

Converts a message’s components into a <a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a> or <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>.

The <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.components" title="discord.Message.components"><code>Message.components</code></a> of a message are read-only and separate types from those in the <code>discord.ui</code> namespace. In order to modify and edit message components they must be converted into a <a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a> or <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a> first.

If the message has any v2 components, then you must use <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a> in order for them to be converted into their respective items. <a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a> does not support v2 components.

<dl><dt>Parameters</dt>
<dd>

- **message** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>discord.Message</code></a>) – The message with components to convert into a view.
- **timeout** (Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – The timeout of the converted view.

</dd><dt>Returns</dt>
<dd>

The converted view. This will always return one of <a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a> or <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>, and not one of its subclasses.

</dd><dt>Return type</dt>
<dd>

Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]

</dd></dl></dd>
</dl><dl><dt>add_item(*item*)<a href="#discord.ui.View.add_item" title="Permalink to this definition">¶</a></dt>
<dd>

Adds an item to the view.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to add to the view.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – An <a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> was not passed.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – Maximum number of children has been exceeded, the row the item is trying to be added to is full or the item you tried to add is not allowed in this View.

</dd></dl></dd>
</dl><dl><dt>remove_item(*item*)<a href="#discord.ui.View.remove_item" title="Permalink to this definition">¶</a></dt>
<dd>

Removes an item from the view.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to remove from the view.

</dd></dl></dd>
</dl><dl><dt>clear_items()<a href="#discord.ui.View.clear_items" title="Permalink to this definition">¶</a></dt>
<dd>

Removes all items from the view.

This function returns the class instance to allow for fluent-style chaining.

</dd></dl><dl><dt>*property*children<a href="#discord.ui.View.children" title="Permalink to this definition">¶</a></dt>
<dd>

The list of children attached to this view.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>find_item(*id*, */*)<a href="#discord.ui.View.find_item" title="Permalink to this definition">¶</a></dt>
<dd>

Gets an item with <a href="#discord.ui.Item.id" title="discord.ui.Item.id"><code>Item.id</code></a> set as <code>id</code>, or <code>None</code> if not found.

Warning

This is **not the same** as <code>custom_id</code>.

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID of the component.

</dd><dt>Returns</dt>
<dd>

The item found, or <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.View.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within the view that checks whether the view should process item callbacks for the interaction.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>on_error()</code></a> is called.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the view children’s callbacks should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>is_dispatching()<a href="#discord.ui.View.is_dispatching" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the view has been added for dispatching purposes.

</dd></dl><dl><dt>is_finished()<a href="#discord.ui.View.is_finished" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the view has finished interacting.

</dd></dl><dl><dt>is_persistent()<a href="#discord.ui.View.is_persistent" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the view is set up as persistent.

A persistent view has all their components with a set <code>custom_id</code> and a <a href="#discord.ui.View.timeout" title="discord.ui.View.timeout"><code>timeout</code></a> set to <code>None</code>.

</dd></dl><dl><dt>*await* on_error(*interaction*, *error*, *item*, */*)<a href="#discord.ui.View.on_error" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an item’s callback or <a href="#discord.ui.View.interaction_check" title="discord.ui.View.interaction_check"><code>interaction_check()</code></a> fails with an error.

The default implementation logs to the library logger.

<dl><dt>Parameters</dt>
<dd>

- **interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that led to the failure.
- **error** (<a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a>) – The exception that was raised.
- **item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item that failed the dispatch.

</dd></dl></dd>
</dl><dl><dt>*await* on_timeout()<a href="#discord.ui.View.on_timeout" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when a view’s timeout elapses without being explicitly stopped.

</dd></dl><dl><dt>stop()<a href="#discord.ui.View.stop" title="Permalink to this definition">¶</a></dt>
<dd>

Stops listening to interaction events from this view.

This operation cannot be undone.

</dd></dl><dl><dt>*property*timeout<a href="#discord.ui.View.timeout" title="Permalink to this definition">¶</a></dt>
<dd>

The timeout in seconds from last interaction with the UI before no longer accepting input. If <code>None</code> then there is no timeout.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*total_children_count<a href="#discord.ui.View.total_children_count" title="Permalink to this definition">¶</a></dt>
<dd>

The total number of children in this view, including those from nested items.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* wait()<a href="#discord.ui.View.wait" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Waits until the view has finished interacting.

A view is considered finished when <a href="#discord.ui.View.stop" title="discord.ui.View.stop"><code>stop()</code></a> is called or it times out.

<dl><dt>Returns</dt>
<dd>

If <code>True</code>, then the view timed out. If <code>False</code> then the view finished normally.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*for ... in* walk_children()<a href="#discord.ui.View.walk_children" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all the children of this view and its children, if applicable.

New in version 2.6.

<dl><dt>Yields</dt>
<dd>

<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> – An item in the view.

</dd></dl></dd>
</dl></dd>
</dl>

### LayoutView ¶

Attributes

- [children](#discord.ui.LayoutView.children)
- [timeout](#discord.ui.LayoutView.timeout)
- [total\_children\_count](#discord.ui.LayoutView.total_children_count)

Methods

- cls [LayoutView.from\_message](#discord.ui.LayoutView.from_message)
- def [add\_item](#discord.ui.LayoutView.add_item)
- def [clear\_items](#discord.ui.LayoutView.clear_items)
- def [content\_length](#discord.ui.LayoutView.content_length)
- def [find\_item](#discord.ui.LayoutView.find_item)
- async [interaction\_check](#discord.ui.LayoutView.interaction_check)
- def [is\_dispatching](#discord.ui.LayoutView.is_dispatching)
- def [is\_finished](#discord.ui.LayoutView.is_finished)
- def [is\_persistent](#discord.ui.LayoutView.is_persistent)
- async [on\_error](#discord.ui.LayoutView.on_error)
- async [on\_timeout](#discord.ui.LayoutView.on_timeout)
- def [remove\_item](#discord.ui.LayoutView.remove_item)
- def [stop](#discord.ui.LayoutView.stop)
- async [wait](#discord.ui.LayoutView.wait)
- def [walk\_children](#discord.ui.LayoutView.walk_children)

<dl><dt>*class*discord.ui.LayoutView(***, *timeout=180.0*)<a href="#discord.ui.LayoutView" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a layout view for components.

This object must be inherited to create a UI within Discord.

This differs from a <a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a> in that it supports all component types and uses what Discord refers to as “v2 components”.

You can find usage examples in the <a href="https://github.com/Rapptz/discord.py/tree/v2.7.1/examples">repository</a>

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

**timeout** (Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – Timeout in seconds from last interaction with the UI before no longer accepting input. If <code>None</code> then there is no timeout.

</dd></dl><dl><dt>*classmethod* from_message(*message*, */*, ***, *timeout=180.0*)<a href="#discord.ui.LayoutView.from_message" title="Permalink to this definition">¶</a></dt>
<dd>

Converts a message’s components into a <a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a> or <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>.

The <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.components" title="discord.Message.components"><code>Message.components</code></a> of a message are read-only and separate types from those in the <code>discord.ui</code> namespace. In order to modify and edit message components they must be converted into a <a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a> or <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a> first.

If the message has any v2 components, then you must use <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a> in order for them to be converted into their respective items. <a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a> does not support v2 components.

<dl><dt>Parameters</dt>
<dd>

- **message** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>discord.Message</code></a>) – The message with components to convert into a view.
- **timeout** (Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – The timeout of the converted view.

</dd><dt>Returns</dt>
<dd>

The converted view. This will always return one of <a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a> or <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>, and not one of its subclasses.

</dd><dt>Return type</dt>
<dd>

Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]

</dd></dl></dd>
</dl><dl><dt>add_item(*item*)<a href="#discord.ui.LayoutView.add_item" title="Permalink to this definition">¶</a></dt>
<dd>

Adds an item to the view.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to add to the view.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – An <a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> was not passed.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – Maximum number of children has been exceeded, the row the item is trying to be added to is full or the item you tried to add is not allowed in this View.

</dd></dl></dd>
</dl><dl><dt>content_length()<a href="#discord.ui.LayoutView.content_length" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>: Returns the total length of all text content in the view’s items.

A view is allowed to have a maximum of 4000 display characters across all its items.

</dd></dl><dl><dt>*property*children<a href="#discord.ui.LayoutView.children" title="Permalink to this definition">¶</a></dt>
<dd>

The list of children attached to this view.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>clear_items()<a href="#discord.ui.LayoutView.clear_items" title="Permalink to this definition">¶</a></dt>
<dd>

Removes all items from the view.

This function returns the class instance to allow for fluent-style chaining.

</dd></dl><dl><dt>find_item(*id*, */*)<a href="#discord.ui.LayoutView.find_item" title="Permalink to this definition">¶</a></dt>
<dd>

Gets an item with <a href="#discord.ui.Item.id" title="discord.ui.Item.id"><code>Item.id</code></a> set as <code>id</code>, or <code>None</code> if not found.

Warning

This is **not the same** as <code>custom_id</code>.

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID of the component.

</dd><dt>Returns</dt>
<dd>

The item found, or <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.LayoutView.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within the view that checks whether the view should process item callbacks for the interaction.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>on_error()</code></a> is called.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the view children’s callbacks should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>is_dispatching()<a href="#discord.ui.LayoutView.is_dispatching" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the view has been added for dispatching purposes.

</dd></dl><dl><dt>is_finished()<a href="#discord.ui.LayoutView.is_finished" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the view has finished interacting.

</dd></dl><dl><dt>is_persistent()<a href="#discord.ui.LayoutView.is_persistent" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the view is set up as persistent.

A persistent view has all their components with a set <code>custom_id</code> and a <a href="#discord.ui.LayoutView.timeout" title="discord.ui.LayoutView.timeout"><code>timeout</code></a> set to <code>None</code>.

</dd></dl><dl><dt>*await* on_error(*interaction*, *error*, *item*, */*)<a href="#discord.ui.LayoutView.on_error" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an item’s callback or <a href="#discord.ui.LayoutView.interaction_check" title="discord.ui.LayoutView.interaction_check"><code>interaction_check()</code></a> fails with an error.

The default implementation logs to the library logger.

<dl><dt>Parameters</dt>
<dd>

- **interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that led to the failure.
- **error** (<a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a>) – The exception that was raised.
- **item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item that failed the dispatch.

</dd></dl></dd>
</dl><dl><dt>*await* on_timeout()<a href="#discord.ui.LayoutView.on_timeout" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when a view’s timeout elapses without being explicitly stopped.

</dd></dl><dl><dt>remove_item(*item*)<a href="#discord.ui.LayoutView.remove_item" title="Permalink to this definition">¶</a></dt>
<dd>

Removes an item from the view.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to remove from the view.

</dd></dl></dd>
</dl><dl><dt>stop()<a href="#discord.ui.LayoutView.stop" title="Permalink to this definition">¶</a></dt>
<dd>

Stops listening to interaction events from this view.

This operation cannot be undone.

</dd></dl><dl><dt>*property*timeout<a href="#discord.ui.LayoutView.timeout" title="Permalink to this definition">¶</a></dt>
<dd>

The timeout in seconds from last interaction with the UI before no longer accepting input. If <code>None</code> then there is no timeout.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*total_children_count<a href="#discord.ui.LayoutView.total_children_count" title="Permalink to this definition">¶</a></dt>
<dd>

The total number of children in this view, including those from nested items.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* wait()<a href="#discord.ui.LayoutView.wait" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Waits until the view has finished interacting.

A view is considered finished when <a href="#discord.ui.LayoutView.stop" title="discord.ui.LayoutView.stop"><code>stop()</code></a> is called or it times out.

<dl><dt>Returns</dt>
<dd>

If <code>True</code>, then the view timed out. If <code>False</code> then the view finished normally.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*for ... in* walk_children()<a href="#discord.ui.LayoutView.walk_children" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all the children of this view and its children, if applicable.

New in version 2.6.

<dl><dt>Yields</dt>
<dd>

<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> – An item in the view.

</dd></dl></dd>
</dl></dd>
</dl>

### Modal ¶

Attributes

- [children](#discord.ui.Modal.children)
- [custom\_id](#discord.ui.Modal.custom_id)
- [timeout](#discord.ui.Modal.timeout)
- [title](#discord.ui.Modal.title)
- [total\_children\_count](#discord.ui.Modal.total_children_count)

Methods

- def [add\_item](#discord.ui.Modal.add_item)
- def [clear\_items](#discord.ui.Modal.clear_items)
- def [find\_item](#discord.ui.Modal.find_item)
- async [interaction\_check](#discord.ui.Modal.interaction_check)
- def [is\_dispatching](#discord.ui.Modal.is_dispatching)
- def [is\_finished](#discord.ui.Modal.is_finished)
- def [is\_persistent](#discord.ui.Modal.is_persistent)
- async [on\_error](#discord.ui.Modal.on_error)
- async [on\_submit](#discord.ui.Modal.on_submit)
- async [on\_timeout](#discord.ui.Modal.on_timeout)
- def [remove\_item](#discord.ui.Modal.remove_item)
- def [stop](#discord.ui.Modal.stop)
- async [wait](#discord.ui.Modal.wait)
- def [walk\_children](#discord.ui.Modal.walk_children)

<dl><dt>*class*discord.ui.Modal(***, *title=...*, *timeout=None*, *custom_id=...*)<a href="#discord.ui.Modal" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI modal.

This object must be inherited to create a modal popup window within discord.

New in version 2.0.

Examples

```
import discord
from discord import ui

class Questionnaire(ui.Modal, title='Questionnaire Response'):
    name = ui.Label(text='Name', component=ui.TextInput())
    answer = ui.Label(text='Answer', component=ui.TextInput(style=discord.TextStyle.paragraph))

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response, {self.name.component.value}!', ephemeral=True)

```

<dl><dt>Parameters</dt>
<dd>

- **title** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The title of the modal. Can only be up to 45 characters.
- **timeout** (Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – Timeout in seconds from last interaction with the UI before no longer accepting input. If <code>None</code> then there is no timeout.
- **custom\_id** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The ID of the modal that gets received during an interaction. If not given then one is generated for you. Can only be up to 100 characters.

</dd></dl><dl><dt>title<a href="#discord.ui.Modal.title" title="Permalink to this definition">¶</a></dt>
<dd>

The title of the modal.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>custom_id<a href="#discord.ui.Modal.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the modal that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* on_submit(*interaction*, */*)<a href="#discord.ui.Modal.on_submit" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Called when the modal is submitted.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that submitted this modal.

</dd></dl></dd>
</dl><dl><dt>*await* on_error(*interaction*, *error*, */*)<a href="#discord.ui.Modal.on_error" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when <a href="#discord.ui.Modal.on_submit" title="discord.ui.Modal.on_submit"><code>on_submit()</code></a> fails with an error.

The default implementation logs to the library logger.

<dl><dt>Parameters</dt>
<dd>

- **interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that led to the failure.
- **error** (<a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a>) – The exception that was raised.

</dd></dl></dd>
</dl><dl><dt>add_item(*item*)<a href="#discord.ui.Modal.add_item" title="Permalink to this definition">¶</a></dt>
<dd>

Adds an item to the view.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to add to the view.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – An <a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> was not passed.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – Maximum number of children has been exceeded, the row the item is trying to be added to is full or the item you tried to add is not allowed in this View.

</dd></dl></dd>
</dl><dl><dt>*property*children<a href="#discord.ui.Modal.children" title="Permalink to this definition">¶</a></dt>
<dd>

The list of children attached to this view.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>clear_items()<a href="#discord.ui.Modal.clear_items" title="Permalink to this definition">¶</a></dt>
<dd>

Removes all items from the view.

This function returns the class instance to allow for fluent-style chaining.

</dd></dl><dl><dt>find_item(*id*, */*)<a href="#discord.ui.Modal.find_item" title="Permalink to this definition">¶</a></dt>
<dd>

Gets an item with <a href="#discord.ui.Item.id" title="discord.ui.Item.id"><code>Item.id</code></a> set as <code>id</code>, or <code>None</code> if not found.

Warning

This is **not the same** as <code>custom_id</code>.

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID of the component.

</dd><dt>Returns</dt>
<dd>

The item found, or <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.Modal.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within the view that checks whether the view should process item callbacks for the interaction.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.Modal.on_error" title="discord.ui.Modal.on_error"><code>on_error()</code></a> is called.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the view children’s callbacks should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>is_dispatching()<a href="#discord.ui.Modal.is_dispatching" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the view has been added for dispatching purposes.

</dd></dl><dl><dt>is_finished()<a href="#discord.ui.Modal.is_finished" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the view has finished interacting.

</dd></dl><dl><dt>is_persistent()<a href="#discord.ui.Modal.is_persistent" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the view is set up as persistent.

A persistent view has all their components with a set <code>custom_id</code> and a <a href="#discord.ui.Modal.timeout" title="discord.ui.Modal.timeout"><code>timeout</code></a> set to <code>None</code>.

</dd></dl><dl><dt>*await* on_timeout()<a href="#discord.ui.Modal.on_timeout" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when a view’s timeout elapses without being explicitly stopped.

</dd></dl><dl><dt>remove_item(*item*)<a href="#discord.ui.Modal.remove_item" title="Permalink to this definition">¶</a></dt>
<dd>

Removes an item from the view.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to remove from the view.

</dd></dl></dd>
</dl><dl><dt>stop()<a href="#discord.ui.Modal.stop" title="Permalink to this definition">¶</a></dt>
<dd>

Stops listening to interaction events from this view.

This operation cannot be undone.

</dd></dl><dl><dt>*property*timeout<a href="#discord.ui.Modal.timeout" title="Permalink to this definition">¶</a></dt>
<dd>

The timeout in seconds from last interaction with the UI before no longer accepting input. If <code>None</code> then there is no timeout.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*total_children_count<a href="#discord.ui.Modal.total_children_count" title="Permalink to this definition">¶</a></dt>
<dd>

The total number of children in this view, including those from nested items.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* wait()<a href="#discord.ui.Modal.wait" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Waits until the view has finished interacting.

A view is considered finished when <a href="#discord.ui.Modal.stop" title="discord.ui.Modal.stop"><code>stop()</code></a> is called or it times out.

<dl><dt>Returns</dt>
<dd>

If <code>True</code>, then the view timed out. If <code>False</code> then the view finished normally.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*for ... in* walk_children()<a href="#discord.ui.Modal.walk_children" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all the children of this view and its children, if applicable.

New in version 2.6.

<dl><dt>Yields</dt>
<dd>

<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> – An item in the view.

</dd></dl></dd>
</dl></dd>
</dl>

### Item ¶

Attributes

- [id](#discord.ui.Item.id)
- [parent](#discord.ui.Item.parent)
- [view](#discord.ui.Item.view)

Methods

- async [callback](#discord.ui.Item.callback)
- async [interaction\_check](#discord.ui.Item.interaction_check)

<dl><dt>*class*discord.ui.Item<a href="#discord.ui.Item" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the base UI item that all UI components inherit from.

The current UI items supported are:

- <a href="#discord.ui.Button" title="discord.ui.Button"><code>discord.ui.Button</code></a>
- <a href="#discord.ui.Select" title="discord.ui.Select"><code>discord.ui.Select</code></a>
- <a href="#discord.ui.TextInput" title="discord.ui.TextInput"><code>discord.ui.TextInput</code></a>
- <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>discord.ui.ActionRow</code></a>
- <a href="#discord.ui.Container" title="discord.ui.Container"><code>discord.ui.Container</code></a>
- <a href="#discord.ui.File" title="discord.ui.File"><code>discord.ui.File</code></a>
- <a href="#discord.ui.MediaGallery" title="discord.ui.MediaGallery"><code>discord.ui.MediaGallery</code></a>
- <a href="#discord.ui.Section" title="discord.ui.Section"><code>discord.ui.Section</code></a>
- <a href="#discord.ui.Separator" title="discord.ui.Separator"><code>discord.ui.Separator</code></a>
- <a href="#discord.ui.TextDisplay" title="discord.ui.TextDisplay"><code>discord.ui.TextDisplay</code></a>
- <a href="#discord.ui.Thumbnail" title="discord.ui.Thumbnail"><code>discord.ui.Thumbnail</code></a>
- <a href="#discord.ui.Label" title="discord.ui.Label"><code>discord.ui.Label</code></a>
- <a href="#discord.ui.RadioGroup" title="discord.ui.RadioGroup"><code>discord.ui.RadioGroup</code></a>
- <a href="#discord.ui.CheckboxGroup" title="discord.ui.CheckboxGroup"><code>discord.ui.CheckboxGroup</code></a>
- <a href="#discord.ui.Checkbox" title="discord.ui.Checkbox"><code>discord.ui.Checkbox</code></a>

New in version 2.0.

<dl><dt>*property*view<a href="#discord.ui.Item.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*id<a href="#discord.ui.Item.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.Item.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* callback(*interaction*)<a href="#discord.ui.Item.callback" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The callback associated with this UI item.

This can be overridden by subclasses.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that triggered this UI item.

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.Item.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within this item that checks whether the callback should be processed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>View.on_error()</code></a> (or <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>LayoutView.on_error()</code></a>) is called.

For <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> this does not call the <code>on_error</code> handler.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the callback should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### DynamicItem ¶

Attributes

- [custom\_id](#discord.ui.DynamicItem.custom_id)
- [id](#discord.ui.DynamicItem.id)
- [item](#discord.ui.DynamicItem.item)
- [parent](#discord.ui.DynamicItem.parent)
- [template](#discord.ui.DynamicItem.template)
- [view](#discord.ui.DynamicItem.view)

Methods

- cls [DynamicItem.from\_custom\_id](#discord.ui.DynamicItem.from_custom_id)
- async [callback](#discord.ui.DynamicItem.callback)
- async [interaction\_check](#discord.ui.DynamicItem.interaction_check)

<dl><dt>*class*discord.ui.DynamicItem(*item*, ***, *row=None*)<a href="#discord.ui.DynamicItem" title="Permalink to this definition">¶</a></dt>
<dd>

Represents an item with a dynamic <code>custom_id</code> that can be used to store state within that <code>custom_id</code>.

The <code>custom_id</code> parsing is done using the <code>re</code> module by passing a <code>template</code> parameter to the class parameter list.

This item is generated every time the component is dispatched. This means that any variable that holds an instance of this class will eventually be out of date and should not be used long term. Their only purpose is to act as a “template” for the actual dispatched item.

When this item is generated, <a href="#discord.ui.DynamicItem.view" title="discord.ui.DynamicItem.view"><code>view</code></a> is set to a regular <a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a> instance, but to a <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a> if the component was sent with one, this is obtained from the original message given from the interaction. This means that custom view subclasses cannot be accessed from this item.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

- **item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to wrap with dynamic custom ID parsing.
- **template** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <code>re.Pattern</code>]) – The template to use for parsing the <code>custom_id</code>. This can be a string or a compiled regular expression. This must be passed as a keyword argument to the class creation.
- **row** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The relative row this button belongs to. A Discord component can only have 5 rows. By default, items are arranged automatically into those 5 rows. If you’d like to control the relative positioning of the row then passing an index is advised. For example, row=1 will show up before row=2. Defaults to <code>None</code>, which is automatic ordering. The row number must be between 0 and 4 (i.e. zero indexed).

</dd></dl><dl><dt>item<a href="#discord.ui.DynamicItem.item" title="Permalink to this definition">¶</a></dt>
<dd>

The item that is wrapped with dynamic custom ID parsing.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*template<a href="#discord.ui.DynamicItem.template" title="Permalink to this definition">¶</a></dt>
<dd>

The compiled regular expression that is used to parse the <code>custom_id</code>.

<dl><dt>Type</dt>
<dd>

<code>re.Pattern</code>

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.DynamicItem.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the dynamic item that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*id<a href="#discord.ui.DynamicItem.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.DynamicItem.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.DynamicItem.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*classmethod await* from_custom_id(*interaction*, *item*, *match*, */*)<a href="#discord.ui.DynamicItem.from_custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A classmethod that is called when the <code>custom_id</code> of a component matches the <code>template</code> of the class. This is called when the component is dispatched.

It must return a new instance of the <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a>.

Subclasses *must* implement this method.

Exceptions raised in this method are logged and ignored.

Warning

This method is called before the callback is dispatched, therefore it means that it is subject to the same timing restrictions as the callback. Ergo, you must reply to an interaction within 3 seconds of it being dispatched.

<dl><dt>Parameters</dt>
<dd>

- **interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that the component belongs to.
- **item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The base item that is being dispatched.
- **match** (<code>re.Match</code>) – The match object that was created from the <code>template</code> matching the <code>custom_id</code>.

</dd><dt>Returns</dt>
<dd>

The new instance of the <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> with information from the <code>match</code> object.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* callback(*interaction*)<a href="#discord.ui.DynamicItem.callback" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The callback associated with this UI item.

This can be overridden by subclasses.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that triggered this UI item.

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.DynamicItem.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within this item that checks whether the callback should be processed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>View.on_error()</code></a> (or <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>LayoutView.on_error()</code></a>) is called.

For <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> this does not call the <code>on_error</code> handler.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the callback should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### Button ¶

Attributes

- [custom\_id](#discord.ui.Button.custom_id)
- [disabled](#discord.ui.Button.disabled)
- [emoji](#discord.ui.Button.emoji)
- [id](#discord.ui.Button.id)
- [label](#discord.ui.Button.label)
- [parent](#discord.ui.Button.parent)
- [sku\_id](#discord.ui.Button.sku_id)
- [style](#discord.ui.Button.style)
- [url](#discord.ui.Button.url)
- [view](#discord.ui.Button.view)

Methods

- async [callback](#discord.ui.Button.callback)
- async [interaction\_check](#discord.ui.Button.interaction_check)

<dl><dt>*class*discord.ui.Button(***, *style=&lt;ButtonStyle.secondary: 2&gt;*, *label=None*, *disabled=False*, *custom_id=None*, *url=None*, *emoji=None*, *row=None*, *sku_id=None*, *id=None*)<a href="#discord.ui.Button" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI button.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **style** (<a href="#discord.ButtonStyle" title="discord.ButtonStyle"><code>discord.ButtonStyle</code></a>) – The style of the button.
- **custom\_id** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The ID of the button that gets received during an interaction. If this button is for a URL, it does not have a custom ID. Can only be up to 100 characters.
- **url** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The URL this button sends you to.
- **disabled** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the button is disabled or not.
- **label** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The label of the button, if any. Can only be up to 80 characters.
- **emoji** (Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]]) – The emoji of the button, if available.
- **row** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The relative row this button belongs to. A Discord component can only have 5 rows. By default, items are arranged automatically into those 5 rows. If you’d like to control the relative positioning of the row then passing an index is advised. For example, row=1 will show up before row=2. Defaults to <code>None</code>, which is automatic ordering. The row number must be between 0 and 4 (i.e. zero indexed).

  Note

  This parameter is ignored when used in a <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>ActionRow</code></a> or v2 component.
- **sku\_id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The SKU ID this button sends you to. Can’t be combined with <code>url</code>, <code>label</code>, <code>emoji</code> nor <code>custom_id</code>.

  New in version 2.4.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of this component. This must be unique across the view.

  New in version 2.6.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.Button.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this button.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*style<a href="#discord.ui.Button.style" title="Permalink to this definition">¶</a></dt>
<dd>

The style of the button.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ButtonStyle" title="discord.ButtonStyle"><code>discord.ButtonStyle</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.Button.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the button that gets received during an interaction.

If this button is for a URL, it does not have a custom ID.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*url<a href="#discord.ui.Button.url" title="Permalink to this definition">¶</a></dt>
<dd>

The URL this button sends you to.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*disabled<a href="#discord.ui.Button.disabled" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the button is disabled or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*label<a href="#discord.ui.Button.label" title="Permalink to this definition">¶</a></dt>
<dd>

The label of the button, if available.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*emoji<a href="#discord.ui.Button.emoji" title="Permalink to this definition">¶</a></dt>
<dd>

The emoji of the button, if available.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*sku_id<a href="#discord.ui.Button.sku_id" title="Permalink to this definition">¶</a></dt>
<dd>

The SKU ID this button sends you to.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* callback(*interaction*)<a href="#discord.ui.Button.callback" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The callback associated with this UI item.

This can be overridden by subclasses.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that triggered this UI item.

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.Button.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within this item that checks whether the callback should be processed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>View.on_error()</code></a> (or <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>LayoutView.on_error()</code></a>) is called.

For <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> this does not call the <code>on_error</code> handler.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the callback should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.Button.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.Button.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>@discord.ui.button(***, *label=None*, *custom_id=None*, *disabled=False*, *style=&lt;ButtonStyle.secondary: 2&gt;*, *emoji=None*, *row=None*, *id=None*)<a href="#discord.ui.button" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that attaches a button to a component.

The function being decorated should have three parameters, <code>self</code> representing the <a href="#discord.ui.View" title="discord.ui.View"><code>discord.ui.View</code></a>, the <a href="#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a> you receive and the <a href="#discord.ui.Button" title="discord.ui.Button"><code>discord.ui.Button</code></a> being pressed.

Note

Buttons with a URL or an SKU cannot be created with this function. Consider creating a <a href="#discord.ui.Button" title="discord.ui.Button"><code>Button</code></a> manually instead. This is because these buttons cannot have a callback associated with them since Discord does not do any processing with them.

<dl><dt>Parameters</dt>
<dd>

- **label** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The label of the button, if any. Can only be up to 80 characters.
- **custom\_id** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The ID of the button that gets received during an interaction. It is recommended not to set this parameter to prevent conflicts. Can only be up to 100 characters.
- **style** (<a href="#discord.ButtonStyle" title="discord.ButtonStyle"><code>ButtonStyle</code></a>) – The style of the button. Defaults to <a href="#discord.ButtonStyle.grey" title="discord.ButtonStyle.grey"><code>ButtonStyle.grey</code></a>.
- **disabled** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the button is disabled or not. Defaults to <code>False</code>.
- **emoji** (Optional\[Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>]]) – The emoji of the button. This can be in string form or a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a> or a full <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>.
- **row** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The relative row this button belongs to. A Discord component can only have 5 rows. By default, items are arranged automatically into those 5 rows. If you’d like to control the relative positioning of the row then passing an index is advised. For example, row=1 will show up before row=2. Defaults to <code>None</code>, which is automatic ordering. The row number must be between 0 and 4 (i.e. zero indexed).

  Note

  This parameter is ignored when used in a <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>ActionRow</code></a> or v2 component.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of this component. This must be unique across the view.

  New in version 2.6.

</dd></dl></dd>
</dl>

### Select Menus ¶

The library provides classes to help create the different types of select menus.

#### Select ¶

Attributes

- [custom\_id](#discord.ui.Select.custom_id)
- [disabled](#discord.ui.Select.disabled)
- [id](#discord.ui.Select.id)
- [max\_values](#discord.ui.Select.max_values)
- [min\_values](#discord.ui.Select.min_values)
- [options](#discord.ui.Select.options)
- [parent](#discord.ui.Select.parent)
- [placeholder](#discord.ui.Select.placeholder)
- [required](#discord.ui.Select.required)
- [type](#discord.ui.Select.type)
- [values](#discord.ui.Select.values)
- [view](#discord.ui.Select.view)

Methods

- def [add\_option](#discord.ui.Select.add_option)
- def [append\_option](#discord.ui.Select.append_option)
- async [callback](#discord.ui.Select.callback)
- async [interaction\_check](#discord.ui.Select.interaction_check)

<dl><dt>*class*discord.ui.Select(***, *custom_id=...*, *placeholder=None*, *min_values=1*, *max_values=1*, *options=...*, *disabled=False*, *required=True*, *row=None*, *id=None*)<a href="#discord.ui.Select" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI select menu with a list of custom options. This is represented to the user as a dropdown menu.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **custom\_id** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The ID of the select menu that gets received during an interaction. If not given then one is generated for you. Can only be up to 100 characters.
- **placeholder** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The placeholder text that is shown if nothing is selected, if any. Can only be up to 150 characters.
- **min\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The minimum number of items that must be chosen for this select menu. Defaults to 1 and must be between 0 and 25.
- **max\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The maximum number of items that must be chosen for this select menu. Defaults to 1 and must be between 1 and 25.
- **options** (List\[<a href="#discord.SelectOption" title="discord.SelectOption"><code>discord.SelectOption</code></a>]) – A list of options that can be selected in this menu. Can only contain up to 25 items.
- **disabled** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the select is disabled or not.
- **required** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the select is required. Only applicable within modals.

  New in version 2.6.
- **row** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The relative row this select menu belongs to. A Discord component can only have 5 rows. By default, items are arranged automatically into those 5 rows. If you’d like to control the relative positioning of the row then passing an index is advised. For example, row=1 will show up before row=2. Defaults to <code>None</code>, which is automatic ordering. The row number must be between 0 and 4 (i.e. zero indexed).

  Note

  This parameter is ignored when used in a <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>ActionRow</code></a> or v2 component.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of the component. This must be unique across the view.

  New in version 2.6.

</dd></dl><dl><dt>*property*values<a href="#discord.ui.Select.values" title="Permalink to this definition">¶</a></dt>
<dd>

A list of values that have been selected by the user.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.ui.Select.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of this component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*options<a href="#discord.ui.Select.options" title="Permalink to this definition">¶</a></dt>
<dd>

A list of options that can be selected in this menu.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.SelectOption" title="discord.SelectOption"><code>discord.SelectOption</code></a>]

</dd></dl></dd>
</dl><dl><dt>add_option(***, *label*, *value=...*, *description=None*, *emoji=None*, *default=False*)<a href="#discord.ui.Select.add_option" title="Permalink to this definition">¶</a></dt>
<dd>

Adds an option to the select menu.

To append a pre-existing <a href="#discord.SelectOption" title="discord.SelectOption"><code>discord.SelectOption</code></a> use the <a href="#discord.ui.Select.append_option" title="discord.ui.Select.append_option"><code>append_option()</code></a> method instead.

<dl><dt>Parameters</dt>
<dd>

- **label** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The label of the option. This is displayed to users. Can only be up to 100 characters.
- **value** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The value of the option. This is not displayed to users. If not given, defaults to the label. Can only be up to 100 characters.
- **description** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – An additional description of the option, if any. Can only be up to 100 characters.
- **emoji** (Optional\[Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>]]) – The emoji of the option, if available. This can either be a string representing the custom or unicode emoji or an instance of <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a> or <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>.
- **default** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this option is selected by default.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The number of options exceeds 25.

</dd></dl></dd>
</dl><dl><dt>append_option(*option*)<a href="#discord.ui.Select.append_option" title="Permalink to this definition">¶</a></dt>
<dd>

Appends an option to the select menu.

<dl><dt>Parameters</dt>
<dd>

**option** (<a href="#discord.SelectOption" title="discord.SelectOption"><code>discord.SelectOption</code></a>) – The option to append to the select menu.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The number of options exceeds 25.

</dd></dl></dd>
</dl><dl><dt>*await* callback(*interaction*)<a href="#discord.ui.Select.callback" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The callback associated with this UI item.

This can be overridden by subclasses.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that triggered this UI item.

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.Select.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the select menu that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*disabled<a href="#discord.ui.Select.disabled" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is disabled or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*id<a href="#discord.ui.Select.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this select.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.Select.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within this item that checks whether the callback should be processed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>View.on_error()</code></a> (or <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>LayoutView.on_error()</code></a>) is called.

For <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> this does not call the <code>on_error</code> handler.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the callback should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*max_values<a href="#discord.ui.Select.max_values" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of items that can be chosen for this select menu.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*min_values<a href="#discord.ui.Select.min_values" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum number of items that must be chosen for this select menu.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.Select.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*placeholder<a href="#discord.ui.Select.placeholder" title="Permalink to this definition">¶</a></dt>
<dd>

The placeholder text that is shown if nothing is selected, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*required<a href="#discord.ui.Select.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is required or not. Only supported in modals.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.Select.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

#### ChannelSelect ¶

Attributes

- [channel\_types](#discord.ui.ChannelSelect.channel_types)
- [custom\_id](#discord.ui.ChannelSelect.custom_id)
- [default\_values](#discord.ui.ChannelSelect.default_values)
- [disabled](#discord.ui.ChannelSelect.disabled)
- [id](#discord.ui.ChannelSelect.id)
- [max\_values](#discord.ui.ChannelSelect.max_values)
- [min\_values](#discord.ui.ChannelSelect.min_values)
- [parent](#discord.ui.ChannelSelect.parent)
- [placeholder](#discord.ui.ChannelSelect.placeholder)
- [required](#discord.ui.ChannelSelect.required)
- [type](#discord.ui.ChannelSelect.type)
- [values](#discord.ui.ChannelSelect.values)
- [view](#discord.ui.ChannelSelect.view)

Methods

- async [callback](#discord.ui.ChannelSelect.callback)
- async [interaction\_check](#discord.ui.ChannelSelect.interaction_check)

<dl><dt>*class*discord.ui.ChannelSelect(***, *custom_id=...*, *channel_types=...*, *placeholder=None*, *min_values=1*, *max_values=1*, *disabled=False*, *required=False*, *row=None*, *default_values=...*, *id=None*)<a href="#discord.ui.ChannelSelect" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI select menu with a list of predefined options with the current channels in the guild.

Please note that if you use this in a private message with a user, no channels will be displayed to the user.

New in version 2.1.

<dl><dt>Parameters</dt>
<dd>

- **custom\_id** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The ID of the select menu that gets received during an interaction. If not given then one is generated for you. Can only be up to 100 characters.
- **channel\_types** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelType" title="discord.ChannelType"><code>ChannelType</code></a>]) – The types of channels to show in the select menu. Defaults to all channels.
- **placeholder** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The placeholder text that is shown if nothing is selected, if any. Can only be up to 150 characters.
- **min\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The minimum number of items that must be chosen for this select menu. Defaults to 1 and must be between 0 and 25.
- **max\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The maximum number of items that must be chosen for this select menu. Defaults to 1 and must be between 1 and 25.
- **disabled** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the select is disabled or not.
- **required** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the select is required. Only applicable within modals.

  New in version 2.6.
- **default\_values** (Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  A list of objects representing the channels that should be selected by default. Number of items must be in range of <code>min_values</code> and <code>max_values</code>.

  New in version 2.4.
- **row** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The relative row this select menu belongs to. A Discord component can only have 5 rows. By default, items are arranged automatically into those 5 rows. If you’d like to control the relative positioning of the row then passing an index is advised. For example, row=1 will show up before row=2. Defaults to <code>None</code>, which is automatic ordering. The row number must be between 0 and 4 (i.e. zero indexed).

  Note

  This parameter is ignored when used in a <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>ActionRow</code></a> or v2 component.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of the component. This must be unique across the view.

  New in version 2.6.

</dd></dl><dl><dt>*await* callback(*interaction*)<a href="#discord.ui.ChannelSelect.callback" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The callback associated with this UI item.

This can be overridden by subclasses.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that triggered this UI item.

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.ChannelSelect.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the select menu that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*disabled<a href="#discord.ui.ChannelSelect.disabled" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is disabled or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*id<a href="#discord.ui.ChannelSelect.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this select.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.ChannelSelect.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within this item that checks whether the callback should be processed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>View.on_error()</code></a> (or <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>LayoutView.on_error()</code></a>) is called.

For <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> this does not call the <code>on_error</code> handler.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the callback should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*max_values<a href="#discord.ui.ChannelSelect.max_values" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of items that can be chosen for this select menu.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*min_values<a href="#discord.ui.ChannelSelect.min_values" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum number of items that must be chosen for this select menu.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.ChannelSelect.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*placeholder<a href="#discord.ui.ChannelSelect.placeholder" title="Permalink to this definition">¶</a></dt>
<dd>

The placeholder text that is shown if nothing is selected, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*required<a href="#discord.ui.ChannelSelect.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is required or not. Only supported in modals.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.ChannelSelect.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.ui.ChannelSelect.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of this component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*channel_types<a href="#discord.ui.ChannelSelect.channel_types" title="Permalink to this definition">¶</a></dt>
<dd>

A list of channel types that can be selected.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelType" title="discord.ChannelType"><code>ChannelType</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*values<a href="#discord.ui.ChannelSelect.values" title="Permalink to this definition">¶</a></dt>
<dd>

A list of channels selected by the user.

<dl><dt>Type</dt>
<dd>

List\[Union\[<a href="#discord.app_commands.AppCommandChannel" title="discord.app_commands.AppCommandChannel"><code>AppCommandChannel</code></a>, <a href="#discord.app_commands.AppCommandThread" title="discord.app_commands.AppCommandThread"><code>AppCommandThread</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*default_values<a href="#discord.ui.ChannelSelect.default_values" title="Permalink to this definition">¶</a></dt>
<dd>

A list of default values for the select menu.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.SelectDefaultValue" title="discord.SelectDefaultValue"><code>discord.SelectDefaultValue</code></a>]

</dd></dl></dd>
</dl></dd>
</dl>

#### RoleSelect ¶

Attributes

- [custom\_id](#discord.ui.RoleSelect.custom_id)
- [default\_values](#discord.ui.RoleSelect.default_values)
- [disabled](#discord.ui.RoleSelect.disabled)
- [id](#discord.ui.RoleSelect.id)
- [max\_values](#discord.ui.RoleSelect.max_values)
- [min\_values](#discord.ui.RoleSelect.min_values)
- [parent](#discord.ui.RoleSelect.parent)
- [placeholder](#discord.ui.RoleSelect.placeholder)
- [required](#discord.ui.RoleSelect.required)
- [type](#discord.ui.RoleSelect.type)
- [values](#discord.ui.RoleSelect.values)
- [view](#discord.ui.RoleSelect.view)

Methods

- async [callback](#discord.ui.RoleSelect.callback)
- async [interaction\_check](#discord.ui.RoleSelect.interaction_check)

<dl><dt>*class*discord.ui.RoleSelect(***, *custom_id=...*, *placeholder=None*, *min_values=1*, *max_values=1*, *disabled=False*, *required=False*, *row=None*, *default_values=...*, *id=None*)<a href="#discord.ui.RoleSelect" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI select menu with a list of predefined options with the current roles of the guild.

Please note that if you use this in a private message with a user, no roles will be displayed to the user.

New in version 2.1.

<dl><dt>Parameters</dt>
<dd>

- **custom\_id** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The ID of the select menu that gets received during an interaction. If not given then one is generated for you. Can only be up to 100 characters.
- **placeholder** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The placeholder text that is shown if nothing is selected, if any. Can only be up to 150 characters.
- **min\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The minimum number of items that must be chosen for this select menu. Defaults to 1 and must be between 0 and 25.
- **max\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The maximum number of items that must be chosen for this select menu. Defaults to 1 and must be between 1 and 25.
- **disabled** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the select is disabled or not.
- **required** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the select is required. Only applicable within modals.

  New in version 2.6.
- **default\_values** (Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  A list of objects representing the roles that should be selected by default. Number of items must be in range of <code>min_values</code> and <code>max_values</code>.

  New in version 2.4.
- **row** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The relative row this select menu belongs to. A Discord component can only have 5 rows. By default, items are arranged automatically into those 5 rows. If you’d like to control the relative positioning of the row then passing an index is advised. For example, row=1 will show up before row=2. Defaults to <code>None</code>, which is automatic ordering. The row number must be between 0 and 4 (i.e. zero indexed).

  Note

  This parameter is ignored when used in a <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>ActionRow</code></a> or v2 component.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of the component. This must be unique across the view.

  New in version 2.6.

</dd></dl><dl><dt>*property*type<a href="#discord.ui.RoleSelect.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of this component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*values<a href="#discord.ui.RoleSelect.values" title="Permalink to this definition">¶</a></dt>
<dd>

A list of roles that have been selected by the user.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Role" title="discord.Role"><code>discord.Role</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*default_values<a href="#discord.ui.RoleSelect.default_values" title="Permalink to this definition">¶</a></dt>
<dd>

A list of default values for the select menu.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.SelectDefaultValue" title="discord.SelectDefaultValue"><code>discord.SelectDefaultValue</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* callback(*interaction*)<a href="#discord.ui.RoleSelect.callback" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The callback associated with this UI item.

This can be overridden by subclasses.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that triggered this UI item.

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.RoleSelect.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the select menu that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*disabled<a href="#discord.ui.RoleSelect.disabled" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is disabled or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*id<a href="#discord.ui.RoleSelect.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this select.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.RoleSelect.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within this item that checks whether the callback should be processed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>View.on_error()</code></a> (or <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>LayoutView.on_error()</code></a>) is called.

For <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> this does not call the <code>on_error</code> handler.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the callback should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*max_values<a href="#discord.ui.RoleSelect.max_values" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of items that can be chosen for this select menu.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*min_values<a href="#discord.ui.RoleSelect.min_values" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum number of items that must be chosen for this select menu.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.RoleSelect.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*placeholder<a href="#discord.ui.RoleSelect.placeholder" title="Permalink to this definition">¶</a></dt>
<dd>

The placeholder text that is shown if nothing is selected, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*required<a href="#discord.ui.RoleSelect.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is required or not. Only supported in modals.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.RoleSelect.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

#### MentionableSelect ¶

Attributes

- [custom\_id](#discord.ui.MentionableSelect.custom_id)
- [default\_values](#discord.ui.MentionableSelect.default_values)
- [disabled](#discord.ui.MentionableSelect.disabled)
- [id](#discord.ui.MentionableSelect.id)
- [max\_values](#discord.ui.MentionableSelect.max_values)
- [min\_values](#discord.ui.MentionableSelect.min_values)
- [parent](#discord.ui.MentionableSelect.parent)
- [placeholder](#discord.ui.MentionableSelect.placeholder)
- [required](#discord.ui.MentionableSelect.required)
- [type](#discord.ui.MentionableSelect.type)
- [values](#discord.ui.MentionableSelect.values)
- [view](#discord.ui.MentionableSelect.view)

Methods

- async [callback](#discord.ui.MentionableSelect.callback)
- async [interaction\_check](#discord.ui.MentionableSelect.interaction_check)

<dl><dt>*class*discord.ui.MentionableSelect(***, *custom_id=...*, *placeholder=None*, *min_values=1*, *max_values=1*, *disabled=False*, *required=False*, *row=None*, *default_values=...*, *id=None*)<a href="#discord.ui.MentionableSelect" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI select menu with a list of predefined options with the current members and roles in the guild.

If this is sent in a private message, it will only allow the user to select the client or themselves. Every selected option in a private message will resolve to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>discord.User</code></a>. It will not give the user any roles to select.

New in version 2.1.

<dl><dt>Parameters</dt>
<dd>

- **custom\_id** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The ID of the select menu that gets received during an interaction. If not given then one is generated for you. Can only be up to 100 characters.
- **placeholder** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The placeholder text that is shown if nothing is selected, if any. Can only be up to 150 characters.
- **min\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The minimum number of items that must be chosen for this select menu. Defaults to 1 and must be between 0 and 25.
- **max\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The maximum number of items that must be chosen for this select menu. Defaults to 1 and must be between 1 and 25.
- **disabled** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the select is disabled or not.
- **required** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the select is required. Only applicable within modals.

  New in version 2.6.
- **default\_values** (Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  A list of objects representing the users/roles that should be selected by default. if <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Object" title="discord.Object"><code>Object</code></a> is passed, then the type must be specified in the constructor. Number of items must be in range of <code>min_values</code> and <code>max_values</code>.

  New in version 2.4.
- **row** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The relative row this select menu belongs to. A Discord component can only have 5 rows. By default, items are arranged automatically into those 5 rows. If you’d like to control the relative positioning of the row then passing an index is advised. For example, row=1 will show up before row=2. Defaults to <code>None</code>, which is automatic ordering. The row number must be between 0 and 4 (i.e. zero indexed).

  Note

  This parameter is ignored when used in a <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>ActionRow</code></a> or v2 component.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of the component. This must be unique across the view.

  New in version 2.6.

</dd></dl><dl><dt>*property*type<a href="#discord.ui.MentionableSelect.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of this component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* callback(*interaction*)<a href="#discord.ui.MentionableSelect.callback" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The callback associated with this UI item.

This can be overridden by subclasses.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that triggered this UI item.

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.MentionableSelect.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the select menu that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*disabled<a href="#discord.ui.MentionableSelect.disabled" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is disabled or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*id<a href="#discord.ui.MentionableSelect.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this select.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.MentionableSelect.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within this item that checks whether the callback should be processed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>View.on_error()</code></a> (or <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>LayoutView.on_error()</code></a>) is called.

For <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> this does not call the <code>on_error</code> handler.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the callback should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*max_values<a href="#discord.ui.MentionableSelect.max_values" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of items that can be chosen for this select menu.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*min_values<a href="#discord.ui.MentionableSelect.min_values" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum number of items that must be chosen for this select menu.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.MentionableSelect.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*placeholder<a href="#discord.ui.MentionableSelect.placeholder" title="Permalink to this definition">¶</a></dt>
<dd>

The placeholder text that is shown if nothing is selected, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*required<a href="#discord.ui.MentionableSelect.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is required or not. Only supported in modals.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*values<a href="#discord.ui.MentionableSelect.values" title="Permalink to this definition">¶</a></dt>
<dd>

A list of roles, members, and users that have been selected by the user.

If this is sent a private message, it will only allow the user to select the client or themselves. Every selected option in a private message will resolve to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>discord.User</code></a>.

If invoked in a guild, the values will always resolve to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>discord.Member</code></a>.

<dl><dt>Type</dt>
<dd>

List\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Role" title="discord.Role"><code>discord.Role</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>discord.Member</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>discord.User</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.MentionableSelect.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*default_values<a href="#discord.ui.MentionableSelect.default_values" title="Permalink to this definition">¶</a></dt>
<dd>

A list of default values for the select menu.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.SelectDefaultValue" title="discord.SelectDefaultValue"><code>discord.SelectDefaultValue</code></a>]

</dd></dl></dd>
</dl></dd>
</dl>

#### UserSelect ¶

Attributes

- [custom\_id](#discord.ui.UserSelect.custom_id)
- [default\_values](#discord.ui.UserSelect.default_values)
- [disabled](#discord.ui.UserSelect.disabled)
- [id](#discord.ui.UserSelect.id)
- [max\_values](#discord.ui.UserSelect.max_values)
- [min\_values](#discord.ui.UserSelect.min_values)
- [parent](#discord.ui.UserSelect.parent)
- [placeholder](#discord.ui.UserSelect.placeholder)
- [required](#discord.ui.UserSelect.required)
- [type](#discord.ui.UserSelect.type)
- [values](#discord.ui.UserSelect.values)
- [view](#discord.ui.UserSelect.view)

Methods

- async [callback](#discord.ui.UserSelect.callback)
- async [interaction\_check](#discord.ui.UserSelect.interaction_check)

<dl><dt>*class*discord.ui.UserSelect(***, *custom_id=...*, *placeholder=None*, *min_values=1*, *max_values=1*, *disabled=False*, *required=False*, *row=None*, *default_values=...*, *id=None*)<a href="#discord.ui.UserSelect" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI select menu with a list of predefined options with the current members of the guild.

If this is sent a private message, it will only allow the user to select the client or themselves. Every selected option in a private message will resolve to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>discord.User</code></a>.

New in version 2.1.

<dl><dt>Parameters</dt>
<dd>

- **custom\_id** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The ID of the select menu that gets received during an interaction. If not given then one is generated for you. Can only be up to 100 characters.
- **placeholder** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The placeholder text that is shown if nothing is selected, if any. Can only be up to 150 characters.
- **min\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The minimum number of items that must be chosen for this select menu. Defaults to 1 and must be between 0 and 25.
- **max\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The maximum number of items that must be chosen for this select menu. Defaults to 1 and must be between 1 and 25.
- **disabled** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the select is disabled or not.
- **required** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the select is required. Only applicable within modals.

  New in version 2.6.
- **default\_values** (Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  A list of objects representing the users that should be selected by default. Number of items must be in range of <code>min_values</code> and <code>max_values</code>.

  New in version 2.4.
- **row** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The relative row this select menu belongs to. A Discord component can only have 5 rows. By default, items are arranged automatically into those 5 rows. If you’d like to control the relative positioning of the row then passing an index is advised. For example, row=1 will show up before row=2. Defaults to <code>None</code>, which is automatic ordering. The row number must be between 0 and 4 (i.e. zero indexed).

  Note

  This parameter is ignored when used in a <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>ActionRow</code></a> or v2 component.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of the component. This must be unique across the view.

  New in version 2.6.

</dd></dl><dl><dt>*property*type<a href="#discord.ui.UserSelect.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of this component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*values<a href="#discord.ui.UserSelect.values" title="Permalink to this definition">¶</a></dt>
<dd>

A list of members and users that have been selected by the user.

If this is sent a private message, it will only allow the user to select the client or themselves. Every selected option in a private message will resolve to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>discord.User</code></a>.

If invoked in a guild, the values will always resolve to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>discord.Member</code></a>.

<dl><dt>Type</dt>
<dd>

List\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>discord.Member</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>discord.User</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*default_values<a href="#discord.ui.UserSelect.default_values" title="Permalink to this definition">¶</a></dt>
<dd>

A list of default values for the select menu.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.SelectDefaultValue" title="discord.SelectDefaultValue"><code>discord.SelectDefaultValue</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* callback(*interaction*)<a href="#discord.ui.UserSelect.callback" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The callback associated with this UI item.

This can be overridden by subclasses.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that triggered this UI item.

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.UserSelect.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the select menu that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*disabled<a href="#discord.ui.UserSelect.disabled" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is disabled or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*id<a href="#discord.ui.UserSelect.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this select.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.UserSelect.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within this item that checks whether the callback should be processed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>View.on_error()</code></a> (or <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>LayoutView.on_error()</code></a>) is called.

For <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> this does not call the <code>on_error</code> handler.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the callback should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*max_values<a href="#discord.ui.UserSelect.max_values" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of items that can be chosen for this select menu.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*min_values<a href="#discord.ui.UserSelect.min_values" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum number of items that must be chosen for this select menu.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.UserSelect.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*placeholder<a href="#discord.ui.UserSelect.placeholder" title="Permalink to this definition">¶</a></dt>
<dd>

The placeholder text that is shown if nothing is selected, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*required<a href="#discord.ui.UserSelect.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the select is required or not. Only supported in modals.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.UserSelect.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

#### select ¶

<dl><dt>@discord.ui.select(***, *cls=discord.ui.select.Select[typing.Any]*, *options=...*, *channel_types=...*, *placeholder=None*, *custom_id=...*, *min_values=1*, *max_values=1*, *disabled=False*, *default_values=...*, *row=None*, *id=None*)<a href="#discord.ui.select" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that attaches a select menu to a component.

The function being decorated should have three parameters, <code>self</code> representing the <a href="#discord.ui.View" title="discord.ui.View"><code>discord.ui.View</code></a>, the <a href="#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a> you receive and the chosen select class.

To obtain the selected values inside the callback, you can use the <code>values</code> attribute of the chosen class in the callback. The list of values will depend on the type of select menu used. View the table below for more information.

| Select Type | Resolved Values |
| --- | --- |
| <a href="#discord.ui.Select" title="discord.ui.Select"><code>discord.ui.Select</code></a> | List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>] |
| <a href="#discord.ui.UserSelect" title="discord.ui.UserSelect"><code>discord.ui.UserSelect</code></a> | List\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>discord.Member</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>discord.User</code></a>]] |
| <a href="#discord.ui.RoleSelect" title="discord.ui.RoleSelect"><code>discord.ui.RoleSelect</code></a> | List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Role" title="discord.Role"><code>discord.Role</code></a>] |
| <a href="#discord.ui.MentionableSelect" title="discord.ui.MentionableSelect"><code>discord.ui.MentionableSelect</code></a> | List\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Role" title="discord.Role"><code>discord.Role</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>discord.Member</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>discord.User</code></a>]] |
| <a href="#discord.ui.ChannelSelect" title="discord.ui.ChannelSelect"><code>discord.ui.ChannelSelect</code></a> | List\[Union\[<a href="#discord.app_commands.AppCommandChannel" title="discord.app_commands.AppCommandChannel"><code>AppCommandChannel</code></a>, <a href="#discord.app_commands.AppCommandThread" title="discord.app_commands.AppCommandThread"><code>AppCommandThread</code></a>]] |

Changed in version 2.1: Added the following keyword-arguments: <code>cls</code>, <code>channel_types</code>

Example

```
class View(discord.ui.View):

    @discord.ui.select(cls=ChannelSelect, channel_types=[discord.ChannelType.text])
    async def select_channels(self, interaction: discord.Interaction, select: ChannelSelect):
        return await interaction.response.send_message(f'You selected {select.values[0].mention}')

```

<dl><dt>Parameters</dt>
<dd>

- **cls** (Union\[Type\[<a href="#discord.ui.Select" title="discord.ui.Select"><code>discord.ui.Select</code></a>], Type\[<a href="#discord.ui.UserSelect" title="discord.ui.UserSelect"><code>discord.ui.UserSelect</code></a>], Type\[<a href="#discord.ui.RoleSelect" title="discord.ui.RoleSelect"><code>discord.ui.RoleSelect</code></a>], Type\[<a href="#discord.ui.MentionableSelect" title="discord.ui.MentionableSelect"><code>discord.ui.MentionableSelect</code></a>], Type\[<a href="#discord.ui.ChannelSelect" title="discord.ui.ChannelSelect"><code>discord.ui.ChannelSelect</code></a>]]) – The class to use for the select menu. Defaults to <a href="#discord.ui.Select" title="discord.ui.Select"><code>discord.ui.Select</code></a>. You can use other select types to display different select menus to the user. See the table above for the different values you can get from each select type. Subclasses work as well, however the callback in the subclass will get overridden.
- **placeholder** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The placeholder text that is shown if nothing is selected, if any. Can only be up to 150 characters.
- **custom\_id** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The ID of the select menu that gets received during an interaction. It is recommended not to set this parameter to prevent conflicts. Can only be up to 100 characters.
- **row** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The relative row this select menu belongs to. A Discord component can only have 5 rows. By default, items are arranged automatically into those 5 rows. If you’d like to control the relative positioning of the row then passing an index is advised. For example, row=1 will show up before row=2. Defaults to <code>None</code>, which is automatic ordering. The row number must be between 0 and 4 (i.e. zero indexed).

  Note

  This parameter is ignored when used in a <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>ActionRow</code></a> or v2 component.
- **min\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The minimum number of items that must be chosen for this select menu. Defaults to 1 and must be between 0 and 25.
- **max\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The maximum number of items that must be chosen for this select menu. Defaults to 1 and must be between 1 and 25.
- **options** (List\[<a href="#discord.SelectOption" title="discord.SelectOption"><code>discord.SelectOption</code></a>]) – A list of options that can be selected in this menu. This can only be used with <a href="#discord.ui.Select" title="discord.ui.Select"><code>Select</code></a> instances. Can only contain up to 25 items.
- **channel\_types** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelType" title="discord.ChannelType"><code>ChannelType</code></a>]) – The types of channels to show in the select menu. Defaults to all channels. This can only be used with <a href="#discord.ui.ChannelSelect" title="discord.ui.ChannelSelect"><code>ChannelSelect</code></a> instances.
- **disabled** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the select is disabled or not. Defaults to <code>False</code>.
- **default\_values** (Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  A list of objects representing the default values for the select menu. This cannot be used with regular <a href="#discord.ui.Select" title="discord.ui.Select"><code>Select</code></a> instances. If <code>cls</code> is <a href="#discord.ui.MentionableSelect" title="discord.ui.MentionableSelect"><code>MentionableSelect</code></a> and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Object" title="discord.Object"><code>Object</code></a> is passed, then the type must be specified in the constructor. Number of items must be in range of <code>min_values</code> and <code>max_values</code>.

  New in version 2.4.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of the component. This must be unique across the view.

  New in version 2.6.

</dd></dl></dd>
</dl>

### TextInput ¶

Attributes

- [custom\_id](#discord.ui.TextInput.custom_id)
- [default](#discord.ui.TextInput.default)
- [id](#discord.ui.TextInput.id)
- [label](#discord.ui.TextInput.label)
- [max\_length](#discord.ui.TextInput.max_length)
- [min\_length](#discord.ui.TextInput.min_length)
- [parent](#discord.ui.TextInput.parent)
- [placeholder](#discord.ui.TextInput.placeholder)
- [required](#discord.ui.TextInput.required)
- [style](#discord.ui.TextInput.style)
- [value](#discord.ui.TextInput.value)
- [view](#discord.ui.TextInput.view)

<dl><dt>*class*discord.ui.TextInput(***, *label=None*, *style=&lt;TextStyle.short: 1&gt;*, *custom_id=...*, *placeholder=None*, *default=None*, *required=True*, *min_length=None*, *max_length=None*, *row=None*, *id=None*)<a href="#discord.ui.TextInput" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI text input.

This a top-level layout component that can only be used in <a href="#discord.ui.Label" title="discord.ui.Label"><code>Label</code></a>.

<dl><dt>str(x)</dt>
<dd>

Returns the value of the text input or an empty string if the value is <code>None</code>.

</dd></dl>

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **label** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) –

  The label to display above the text input. Can only be up to 45 characters.

  Deprecated since version 2.6: This parameter is deprecated, use <a href="#discord.ui.Label" title="discord.ui.Label"><code>discord.ui.Label</code></a> instead.

  Changed in version 2.6: This parameter is now optional and defaults to <code>None</code>.
- **custom\_id** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The ID of the text input that gets received during an interaction. If not given then one is generated for you. Can only be up to 100 characters.
- **style** (<a href="#discord.TextStyle" title="discord.TextStyle"><code>discord.TextStyle</code></a>) – The style of the text input.
- **placeholder** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The placeholder text to display when the text input is empty. Can only be up to 100 characters.
- **default** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The default value of the text input. Can only be up to 4000 characters.
- **required** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the text input is required.
- **min\_length** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The minimum length of the text input. Must be between 0 and 4000.
- **max\_length** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The maximum length of the text input. Must be between 1 and 4000.
- **row** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The relative row this text input belongs to. A Discord component can only have 5 rows. By default, items are arranged automatically into those 5 rows. If you’d like to control the relative positioning of the row then passing an index is advised. For example, row=1 will show up before row=2. Defaults to <code>None</code>, which is automatic ordering. The row number must be between 0 and 4 (i.e. zero indexed).
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of the component. This must be unique across the view.

  New in version 2.6.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.TextInput.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this text input.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.TextInput.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the text input that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*value<a href="#discord.ui.TextInput.value" title="Permalink to this definition">¶</a></dt>
<dd>

The value of the text input.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*label<a href="#discord.ui.TextInput.label" title="Permalink to this definition">¶</a></dt>
<dd>

The label of the text input.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*placeholder<a href="#discord.ui.TextInput.placeholder" title="Permalink to this definition">¶</a></dt>
<dd>

The placeholder text to display when the text input is empty.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*required<a href="#discord.ui.TextInput.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the text input is required.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*min_length<a href="#discord.ui.TextInput.min_length" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum length of the text input.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*max_length<a href="#discord.ui.TextInput.max_length" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum length of the text input.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.TextInput.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*style<a href="#discord.ui.TextInput.style" title="Permalink to this definition">¶</a></dt>
<dd>

The style of the text input.

<dl><dt>Type</dt>
<dd>

<a href="#discord.TextStyle" title="discord.TextStyle"><code>discord.TextStyle</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.TextInput.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*default<a href="#discord.ui.TextInput.default" title="Permalink to this definition">¶</a></dt>
<dd>

The default value of the text input.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### Container ¶

Attributes

- [accent\_color](#discord.ui.Container.accent_color)
- [accent\_colour](#discord.ui.Container.accent_colour)
- [children](#discord.ui.Container.children)
- [id](#discord.ui.Container.id)
- [parent](#discord.ui.Container.parent)
- [view](#discord.ui.Container.view)

Methods

- def [add\_item](#discord.ui.Container.add_item)
- def [clear\_items](#discord.ui.Container.clear_items)
- def [content\_length](#discord.ui.Container.content_length)
- def [find\_item](#discord.ui.Container.find_item)
- async [interaction\_check](#discord.ui.Container.interaction_check)
- def [remove\_item](#discord.ui.Container.remove_item)
- def [walk\_children](#discord.ui.Container.walk_children)

<dl><dt>*class*discord.ui.Container(**children*, *accent_colour=None*, *accent_color=None*, *spoiler=False*, *id=None*)<a href="#discord.ui.Container" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI container.

This is a top-level layout component that can only be used on <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a> and can contain <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>ActionRow</code></a>s, <a href="#discord.ui.TextDisplay" title="discord.ui.TextDisplay"><code>TextDisplay</code></a>s, <a href="#discord.ui.Section" title="discord.ui.Section"><code>Section</code></a>s, <a href="#discord.ui.MediaGallery" title="discord.ui.MediaGallery"><code>MediaGallery</code></a>s, <a href="#discord.ui.File" title="discord.ui.File"><code>File</code></a>s, and <a href="#discord.ui.Separator" title="discord.ui.Separator"><code>Separator</code></a>s in it.

This can be inherited.

New in version 2.6.

Examples

```
import discord
from discord import ui

# you can subclass it and add components as you would add them
# in a LayoutView
class MyContainer(ui.Container):
    action_row = ui.ActionRow()

    @action_row.button(label='A button in a container!')
    async def a_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You clicked a button!')

# or use it directly on LayoutView
class MyView(ui.LayoutView):
    container = ui.Container(ui.TextDisplay('I am a text display on a container!'))
    # or you can use your subclass:
    # container = MyContainer()

```

<dl><dt>Parameters</dt>
<dd>

- **\*children** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The initial children of this container.
- **accent\_colour** (Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Colour" title="discord.Colour"><code>Colour</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]]) – The colour of the container. Defaults to <code>None</code>.
- **accent\_color** (Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Colour" title="discord.Colour"><code>Colour</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]]) – The color of the container. Defaults to <code>None</code>.
- **spoiler** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to flag this container as a spoiler. Defaults to <code>False</code>.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of this component. This must be unique across the view.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.Container.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*children<a href="#discord.ui.Container.children" title="Permalink to this definition">¶</a></dt>
<dd>

The children of this container.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*accent_colour<a href="#discord.ui.Container.accent_colour" title="Permalink to this definition">¶</a></dt>
<dd>

The colour of the container, or <code>None</code>.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Colour" title="discord.Colour"><code>discord.Colour</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*accent_color<a href="#discord.ui.Container.accent_color" title="Permalink to this definition">¶</a></dt>
<dd>

The colour of the container, or <code>None</code>.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Colour" title="discord.Colour"><code>discord.Colour</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*for ... in* walk_children()<a href="#discord.ui.Container.walk_children" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all the children of this container and its children, if applicable.

<dl><dt>Yields</dt>
<dd>

<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> – An item in the container.

</dd></dl></dd>
</dl><dl><dt>content_length()<a href="#discord.ui.Container.content_length" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>: Returns the total length of all text content in this container.

</dd></dl><dl><dt>add_item(*item*)<a href="#discord.ui.Container.add_item" title="Permalink to this definition">¶</a></dt>
<dd>

Adds an item to this container.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to append.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – An <a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> was not passed.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – Maximum number of children has been exceeded (40) for the entire view.

</dd></dl></dd>
</dl><dl><dt>remove_item(*item*)<a href="#discord.ui.Container.remove_item" title="Permalink to this definition">¶</a></dt>
<dd>

Removes an item from this container.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to remove from the container.

</dd></dl></dd>
</dl><dl><dt>find_item(*id*, */*)<a href="#discord.ui.Container.find_item" title="Permalink to this definition">¶</a></dt>
<dd>

Gets an item with <a href="#discord.ui.Item.id" title="discord.ui.Item.id"><code>Item.id</code></a> set as <code>id</code>, or <code>None</code> if not found.

Warning

This is **not the same** as <code>custom_id</code>.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID of the component.

</dd><dt>Returns</dt>
<dd>

The item found, or <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>clear_items()<a href="#discord.ui.Container.clear_items" title="Permalink to this definition">¶</a></dt>
<dd>

Removes all the items from the container.

This function returns the class instance to allow for fluent-style chaining.

</dd></dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.Container.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within this item that checks whether the callback should be processed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>View.on_error()</code></a> (or <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>LayoutView.on_error()</code></a>) is called.

For <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> this does not call the <code>on_error</code> handler.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the callback should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.Container.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.Container.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

### File ¶

Attributes

- [id](#discord.ui.File.id)
- [media](#discord.ui.File.media)
- [parent](#discord.ui.File.parent)
- [spoiler](#discord.ui.File.spoiler)
- [url](#discord.ui.File.url)
- [view](#discord.ui.File.view)

<dl><dt>*class*discord.ui.File(*media*, ***, *spoiler=...*, *id=None*)<a href="#discord.ui.File" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI file component.

This is a top-level layout component that can only be used on <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>.

New in version 2.6.

Example

```
import discord
from discord import ui

class MyView(ui.LayoutView):
    file = ui.File('attachment://file.txt')
    # attachment://file.txt points to an attachment uploaded alongside this view

```

<dl><dt>Parameters</dt>
<dd>

- **media** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.UnfurledMediaItem" title="discord.UnfurledMediaItem"><code>UnfurledMediaItem</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>discord.File</code></a>]) – This file’s media. If this is a string it must point to a local file uploaded within the parent view of this item, and must meet the <code>attachment://&lt;filename&gt;</code> format.
- **spoiler** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to flag this file as a spoiler. Defaults to <code>False</code>.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of this component. This must be unique across the view.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.File.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this file component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*media<a href="#discord.ui.File.media" title="Permalink to this definition">¶</a></dt>
<dd>

Returns this file media.

<dl><dt>Type</dt>
<dd>

<a href="#discord.UnfurledMediaItem" title="discord.UnfurledMediaItem"><code>UnfurledMediaItem</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.File.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*url<a href="#discord.ui.File.url" title="Permalink to this definition">¶</a></dt>
<dd>

Returns this file’s url.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.File.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*spoiler<a href="#discord.ui.File.spoiler" title="Permalink to this definition">¶</a></dt>
<dd>

Returns whether this file should be flagged as a spoiler.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### Label ¶

Attributes

- [component](#discord.ui.Label.component)
- [description](#discord.ui.Label.description)
- [id](#discord.ui.Label.id)
- [parent](#discord.ui.Label.parent)
- [text](#discord.ui.Label.text)
- [view](#discord.ui.Label.view)

<dl><dt>*class*discord.ui.Label(***, *text*, *component*, *description=None*, *id=None*)<a href="#discord.ui.Label" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI label within a modal.

This is a top-level layout component that can only be used on <a href="#discord.ui.Modal" title="discord.ui.Modal"><code>Modal</code></a>.

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

- **text** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The text to display above the input field. Can only be up to 45 characters.
- **description** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The description text to display right below the label text. Can only be up to 100 characters.
- **component** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The component to display below the label.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of the component. This must be unique across the view.

</dd></dl><dl><dt>text<a href="#discord.ui.Label.text" title="Permalink to this definition">¶</a></dt>
<dd>

The text to display above the input field. Can only be up to 45 characters.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.ui.Label.description" title="Permalink to this definition">¶</a></dt>
<dd>

The description text to display right below the label text. Can only be up to 100 characters.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>component<a href="#discord.ui.Label.component" title="Permalink to this definition">¶</a></dt>
<dd>

The component to display below the label.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*id<a href="#discord.ui.Label.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.Label.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.Label.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

### MediaGallery ¶

Attributes

- [id](#discord.ui.MediaGallery.id)
- [items](#discord.ui.MediaGallery.items)
- [parent](#discord.ui.MediaGallery.parent)
- [view](#discord.ui.MediaGallery.view)

Methods

- def [add\_item](#discord.ui.MediaGallery.add_item)
- def [append\_item](#discord.ui.MediaGallery.append_item)
- def [clear\_items](#discord.ui.MediaGallery.clear_items)
- def [insert\_item\_at](#discord.ui.MediaGallery.insert_item_at)
- def [remove\_item](#discord.ui.MediaGallery.remove_item)

<dl><dt>*class*discord.ui.MediaGallery(**items*, *id=None*)<a href="#discord.ui.MediaGallery" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI media gallery.

Can contain up to 10 <a href="#discord.MediaGalleryItem" title="discord.MediaGalleryItem"><code>MediaGalleryItem</code></a>s.

This is a top-level layout component that can only be used on <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>.

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

- **\*items** (<a href="#discord.MediaGalleryItem" title="discord.MediaGalleryItem"><code>MediaGalleryItem</code></a>) – The initial items of this gallery.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of this component. This must be unique across the view.

</dd></dl><dl><dt>*property*items<a href="#discord.ui.MediaGallery.items" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a read-only list of this gallery’s items.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.MediaGalleryItem" title="discord.MediaGalleryItem"><code>MediaGalleryItem</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*id<a href="#discord.ui.MediaGallery.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>add_item(***, *media*, *description=...*, *spoiler=...*)<a href="#discord.ui.MediaGallery.add_item" title="Permalink to this definition">¶</a></dt>
<dd>

Adds an item to this gallery.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

- **media** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>discord.File</code></a>, <a href="#discord.UnfurledMediaItem" title="discord.UnfurledMediaItem"><code>UnfurledMediaItem</code></a>]) – The media item data. This can be a string representing a local file uploaded as an attachment in the message, which can be accessed using the <code>attachment://&lt;filename&gt;</code> format, or an arbitrary url.
- **description** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The description to show within this item. Up to 256 characters. Defaults to <code>None</code>.
- **spoiler** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this item should be flagged as a spoiler. Defaults to <code>False</code>.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – Maximum number of items has been exceeded (10).

</dd></dl></dd>
</dl><dl><dt>append_item(*item*)<a href="#discord.ui.MediaGallery.append_item" title="Permalink to this definition">¶</a></dt>
<dd>

Appends an item to this gallery.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.MediaGalleryItem" title="discord.MediaGalleryItem"><code>MediaGalleryItem</code></a>) – The item to add to the gallery.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – A <a href="#discord.MediaGalleryItem" title="discord.MediaGalleryItem"><code>MediaGalleryItem</code></a> was not passed.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – Maximum number of items has been exceeded (10).

</dd></dl></dd>
</dl><dl><dt>insert_item_at(*index*, ***, *media*, *description=...*, *spoiler=...*)<a href="#discord.ui.MediaGallery.insert_item_at" title="Permalink to this definition">¶</a></dt>
<dd>

Inserts an item before a specified index to the media gallery.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

- **index** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The index of where to insert the field.
- **media** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>discord.File</code></a>, <a href="#discord.UnfurledMediaItem" title="discord.UnfurledMediaItem"><code>UnfurledMediaItem</code></a>]) – The media item data. This can be a string representing a local file uploaded as an attachment in the message, which can be accessed using the <code>attachment://&lt;filename&gt;</code> format, or an arbitrary url.
- **description** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The description to show within this item. Up to 256 characters. Defaults to <code>None</code>.
- **spoiler** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this item should be flagged as a spoiler. Defaults to <code>False</code>.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – Maximum number of items has been exceeded (10).

</dd></dl></dd>
</dl><dl><dt>remove_item(*item*)<a href="#discord.ui.MediaGallery.remove_item" title="Permalink to this definition">¶</a></dt>
<dd>

Removes an item from the gallery.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.MediaGalleryItem" title="discord.MediaGalleryItem"><code>MediaGalleryItem</code></a>) – The item to remove from the gallery.

</dd></dl></dd>
</dl><dl><dt>clear_items()<a href="#discord.ui.MediaGallery.clear_items" title="Permalink to this definition">¶</a></dt>
<dd>

Removes all items from the gallery.

This function returns the class instance to allow for fluent-style chaining.

</dd></dl><dl><dt>*property*parent<a href="#discord.ui.MediaGallery.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.MediaGallery.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

### Section ¶

Attributes

- [accessory](#discord.ui.Section.accessory)
- [children](#discord.ui.Section.children)
- [id](#discord.ui.Section.id)
- [parent](#discord.ui.Section.parent)
- [view](#discord.ui.Section.view)

Methods

- def [add\_item](#discord.ui.Section.add_item)
- def [clear\_items](#discord.ui.Section.clear_items)
- def [content\_length](#discord.ui.Section.content_length)
- def [find\_item](#discord.ui.Section.find_item)
- async [interaction\_check](#discord.ui.Section.interaction_check)
- def [remove\_item](#discord.ui.Section.remove_item)
- def [walk\_children](#discord.ui.Section.walk_children)

<dl><dt>*class*discord.ui.Section(**children*, *accessory*, *id=None*)<a href="#discord.ui.Section" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI section.

This is a top-level layout component that can only be used on <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>.

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

- **\*children** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.ui.TextDisplay" title="discord.ui.TextDisplay"><code>TextDisplay</code></a>]) – The text displays of this section. Up to 3.
- **accessory** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The section accessory. This is usually either a <a href="#discord.ui.Button" title="discord.ui.Button"><code>Button</code></a> or <a href="#discord.ui.Thumbnail" title="discord.ui.Thumbnail"><code>Thumbnail</code></a>.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of this component. This must be unique across the view.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.Section.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*children<a href="#discord.ui.Section.children" title="Permalink to this definition">¶</a></dt>
<dd>

The list of children attached to this section.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*accessory<a href="#discord.ui.Section.accessory" title="Permalink to this definition">¶</a></dt>
<dd>

The section’s accessory.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>

</dd></dl></dd>
</dl><dl><dt>*for ... in* walk_children()<a href="#discord.ui.Section.walk_children" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all the children of this section and its children, if applicable. This includes the *accessory*.

<dl><dt>Yields</dt>
<dd>

<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> – An item in this section.

</dd></dl></dd>
</dl><dl><dt>content_length()<a href="#discord.ui.Section.content_length" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>: Returns the total length of all text content in this section.

</dd></dl><dl><dt>add_item(*item*)<a href="#discord.ui.Section.add_item" title="Permalink to this definition">¶</a></dt>
<dd>

Adds an item to this section.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]) – The item to append, if it is a string it automatically wrapped around <a href="#discord.ui.TextDisplay" title="discord.ui.TextDisplay"><code>TextDisplay</code></a>.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – An <a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> or <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a> was not passed.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – Maximum number of children has been exceeded (3) or (40) for the entire view.

</dd></dl></dd>
</dl><dl><dt>remove_item(*item*)<a href="#discord.ui.Section.remove_item" title="Permalink to this definition">¶</a></dt>
<dd>

Removes an item from this section.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to remove from the section.

</dd></dl></dd>
</dl><dl><dt>find_item(*id*, */*)<a href="#discord.ui.Section.find_item" title="Permalink to this definition">¶</a></dt>
<dd>

Gets an item with <a href="#discord.ui.Item.id" title="discord.ui.Item.id"><code>Item.id</code></a> set as <code>id</code>, or <code>None</code> if not found.

Warning

This is **not the same** as <code>custom_id</code>.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID of the component.

</dd><dt>Returns</dt>
<dd>

The item found, or <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>clear_items()<a href="#discord.ui.Section.clear_items" title="Permalink to this definition">¶</a></dt>
<dd>

Removes all the items from the section.

This function returns the class instance to allow for fluent-style chaining.

</dd></dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.Section.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within this item that checks whether the callback should be processed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>View.on_error()</code></a> (or <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>LayoutView.on_error()</code></a>) is called.

For <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> this does not call the <code>on_error</code> handler.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the callback should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.Section.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.Section.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

### Separator ¶

Attributes

- [id](#discord.ui.Separator.id)
- [parent](#discord.ui.Separator.parent)
- [spacing](#discord.ui.Separator.spacing)
- [view](#discord.ui.Separator.view)
- [visible](#discord.ui.Separator.visible)

<dl><dt>*class*discord.ui.Separator(***, *visible=True*, *spacing=&lt;SeparatorSpacing.small: 1&gt;*, *id=None*)<a href="#discord.ui.Separator" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI separator.

This is a top-level layout component that can only be used on <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>.

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

- **visible** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this separator is visible. On the client side this is whether a divider line should be shown or not.
- **spacing** (<a href="#discord.SeparatorSpacing" title="discord.SeparatorSpacing"><code>SeparatorSpacing</code></a>) – The spacing of this separator.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of this component. This must be unique across the view.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.Separator.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this separator.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*visible<a href="#discord.ui.Separator.visible" title="Permalink to this definition">¶</a></dt>
<dd>

Whether this separator is visible.

On the client side this is whether a divider line should be shown or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*spacing<a href="#discord.ui.Separator.spacing" title="Permalink to this definition">¶</a></dt>
<dd>

The spacing of this separator.

<dl><dt>Type</dt>
<dd>

<a href="#discord.SeparatorSpacing" title="discord.SeparatorSpacing"><code>SeparatorSpacing</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.Separator.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.Separator.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

### TextDisplay ¶

Attributes

- [id](#discord.ui.TextDisplay.id)
- [parent](#discord.ui.TextDisplay.parent)
- [view](#discord.ui.TextDisplay.view)

<dl><dt>*class*discord.ui.TextDisplay(*content*, ***, *id=None*)<a href="#discord.ui.TextDisplay" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI text display.

This is a top-level layout component that can only be used on <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>, <a href="#discord.ui.Section" title="discord.ui.Section"><code>Section</code></a>, <a href="#discord.ui.Container" title="discord.ui.Container"><code>Container</code></a>, or <a href="#discord.ui.Modal" title="discord.ui.Modal"><code>Modal</code></a>.

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

- **content** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The content of this text display. Up to 4000 characters.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of this component. This must be unique across the view.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.TextDisplay.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.TextDisplay.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.TextDisplay.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

### Thumbnail ¶

Attributes

- [id](#discord.ui.Thumbnail.id)
- [media](#discord.ui.Thumbnail.media)
- [parent](#discord.ui.Thumbnail.parent)
- [view](#discord.ui.Thumbnail.view)

<dl><dt>*class*discord.ui.Thumbnail(*media*, ***, *description=...*, *spoiler=...*, *id=None*)<a href="#discord.ui.Thumbnail" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI Thumbnail. This currently can only be used as a <a href="#discord.ui.Section" title="discord.ui.Section"><code>Section</code></a>’s accessory.

New in version 2.6.

<dl><dt>Parameters</dt>
<dd>

- **media** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>discord.File</code></a>, <a href="#discord.UnfurledMediaItem" title="discord.UnfurledMediaItem"><code>discord.UnfurledMediaItem</code></a>]) – The media of the thumbnail. This can be a URL or a reference to an attachment that matches the <code>attachment://filename.extension</code> structure.
- **description** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The description of this thumbnail. Up to 256 characters. Defaults to <code>None</code>.
- **spoiler** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to flag this thumbnail as a spoiler. Defaults to <code>False</code>.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of this component. This must be unique across the view.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.Thumbnail.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*media<a href="#discord.ui.Thumbnail.media" title="Permalink to this definition">¶</a></dt>
<dd>

This thumbnail unfurled media data.

<dl><dt>Type</dt>
<dd>

<a href="#discord.UnfurledMediaItem" title="discord.UnfurledMediaItem"><code>discord.UnfurledMediaItem</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.Thumbnail.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.Thumbnail.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

### ActionRow ¶

Attributes

- [children](#discord.ui.ActionRow.children)
- [id](#discord.ui.ActionRow.id)
- [parent](#discord.ui.ActionRow.parent)
- [view](#discord.ui.ActionRow.view)

Methods

- def [add\_item](#discord.ui.ActionRow.add_item)
- @ [button](#discord.ui.ActionRow.button)
- def [clear\_items](#discord.ui.ActionRow.clear_items)
- def [content\_length](#discord.ui.ActionRow.content_length)
- def [find\_item](#discord.ui.ActionRow.find_item)
- async [interaction\_check](#discord.ui.ActionRow.interaction_check)
- def [remove\_item](#discord.ui.ActionRow.remove_item)
- @ [select](#discord.ui.ActionRow.select)
- def [walk\_children](#discord.ui.ActionRow.walk_children)

<dl><dt>*class*discord.ui.ActionRow(**children*, *id=None*)<a href="#discord.ui.ActionRow" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a UI action row.

This is a top-level layout component that can only be used on <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a> and can contain <a href="#discord.ui.Button" title="discord.ui.Button"><code>Button</code></a>s and <a href="#discord.ui.Select" title="discord.ui.Select"><code>Select</code></a>s in it.

Action rows can only have 5 children. This can be inherited.

New in version 2.6.

Examples

```
import discord
from discord import ui

# you can subclass it and add components with the decorators
class MyActionRow(ui.ActionRow):
    @ui.button(label='Click Me!')
    async def click_me(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You clicked me!')

# or use it directly on LayoutView
class MyView(ui.LayoutView):
    row = ui.ActionRow()
    # or you can use your subclass:
    # row = MyActionRow()

    # you can add items with row.button and row.select
    @row.button(label='A button!')
    async def row_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('You clicked a button!')

```

<dl><dt>Parameters</dt>
<dd>

- **\*children** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The initial children of this action row.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of this component. This must be unique across the view.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.ActionRow.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*children<a href="#discord.ui.ActionRow.children" title="Permalink to this definition">¶</a></dt>
<dd>

The list of children attached to this action row.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*for ... in* walk_children()<a href="#discord.ui.ActionRow.walk_children" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all the children of this action row and its children, if applicable.

<dl><dt>Yields</dt>
<dd>

<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> – An item in the action row.

</dd></dl></dd>
</dl><dl><dt>content_length()<a href="#discord.ui.ActionRow.content_length" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>: Returns the total length of all text content in this action row.

</dd></dl><dl><dt>add_item(*item*)<a href="#discord.ui.ActionRow.add_item" title="Permalink to this definition">¶</a></dt>
<dd>

Adds an item to this action row.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to add to the action row.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – An <a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a> was not passed.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – Maximum number of children has been exceeded (5) or (40) for the entire view.

</dd></dl></dd>
</dl><dl><dt>remove_item(*item*)<a href="#discord.ui.ActionRow.remove_item" title="Permalink to this definition">¶</a></dt>
<dd>

Removes an item from the action row.

This function returns the class instance to allow for fluent-style chaining.

<dl><dt>Parameters</dt>
<dd>

**item** (<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>) – The item to remove from the action row.

</dd></dl></dd>
</dl><dl><dt>find_item(*id*, */*)<a href="#discord.ui.ActionRow.find_item" title="Permalink to this definition">¶</a></dt>
<dd>

Gets an item with <a href="#discord.ui.Item.id" title="discord.ui.Item.id"><code>Item.id</code></a> set as <code>id</code>, or <code>None</code> if not found.

Warning

This is **not the same** as <code>custom_id</code>.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID of the component.

</dd><dt>Returns</dt>
<dd>

The item found, or <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>clear_items()<a href="#discord.ui.ActionRow.clear_items" title="Permalink to this definition">¶</a></dt>
<dd>

Removes all items from the action row.

This function returns the class instance to allow for fluent-style chaining.

</dd></dl><dl><dt>button(***, *label=None*, *custom_id=None*, *disabled=False*, *style=&lt;ButtonStyle.secondary: 2&gt;*, *emoji=None*, *id=None*)<a href="#discord.ui.ActionRow.button" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that attaches a button to the action row.

The function being decorated should have three parameters, <code>self</code> representing the <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>discord.ui.ActionRow</code></a>, the <a href="#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a> you receive and the <a href="#discord.ui.Button" title="discord.ui.Button"><code>discord.ui.Button</code></a> being pressed.

Note

Buttons with a URL or a SKU cannot be created with this function. Consider creating a <a href="#discord.ui.Button" title="discord.ui.Button"><code>Button</code></a> manually and adding it via <a href="#discord.ui.ActionRow.add_item" title="discord.ui.ActionRow.add_item"><code>ActionRow.add_item()</code></a> instead. This is beacuse these buttons cannot have a callback associated with them since Discord does not do any processing with them.

<dl><dt>Parameters</dt>
<dd>

- **label** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The label of the button, if any. Can only be up to 80 characters.
- **custom\_id** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The ID of the button that gets received during an interaction. It is recommended to not set this parameters to prevent conflicts. Can only be up to 100 characters.
- **style** (<a href="#discord.ButtonStyle" title="discord.ButtonStyle"><code>ButtonStyle</code></a>) – The style of the button. Defaults to <a href="#discord.ButtonStyle.grey" title="discord.ButtonStyle.grey"><code>ButtonStyle.grey</code></a>.
- **disabled** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the button is disabled or not. Defaults to <code>False</code>.
- **emoji** (Optional\[Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>]]) – The emoji of the button. This can be in string form or a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a> or a full <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of the component. This must be unique across the view.

  New in version 2.6.

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.ui.ActionRow.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within this item that checks whether the callback should be processed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and <a href="#discord.ui.View.on_error" title="discord.ui.View.on_error"><code>View.on_error()</code></a> (or <a href="#discord.ui.LayoutView.on_error" title="discord.ui.LayoutView.on_error"><code>LayoutView.on_error()</code></a>) is called.

For <a href="#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> this does not call the <code>on_error</code> handler.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the callback should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.ActionRow.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.ActionRow.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl><dl><dt>select(***, *cls=discord.ui.select.Select[typing.Any]*, *options=...*, *channel_types=...*, *placeholder=None*, *custom_id=...*, *min_values=1*, *max_values=1*, *disabled=False*, *default_values=...*, *id=None*)<a href="#discord.ui.ActionRow.select" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that attaches a select menu to the action row.

The function being decorated should have three parameters, <code>self</code> representing the <a href="#discord.ui.ActionRow" title="discord.ui.ActionRow"><code>discord.ui.ActionRow</code></a>, the <a href="#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a> you receive and the chosen select class.

To obtain the selected values inside the callback, you can use the <code>values</code> attribute of the chosen class in the callback. The list of values will depend on the type of select menu used. View the table below for more information.

| Select Type | Resolved Values |
| --- | --- |
| <a href="#discord.ui.Select" title="discord.ui.Select"><code>discord.ui.Select</code></a> | List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>] |
| <a href="#discord.ui.UserSelect" title="discord.ui.UserSelect"><code>discord.ui.UserSelect</code></a> | List\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>discord.Member</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>discord.User</code></a>]] |
| <a href="#discord.ui.RoleSelect" title="discord.ui.RoleSelect"><code>discord.ui.RoleSelect</code></a> | List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Role" title="discord.Role"><code>discord.Role</code></a>] |
| <a href="#discord.ui.MentionableSelect" title="discord.ui.MentionableSelect"><code>discord.ui.MentionableSelect</code></a> | List\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Role" title="discord.Role"><code>discord.Role</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>discord.Member</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>discord.User</code></a>]] |
| <a href="#discord.ui.ChannelSelect" title="discord.ui.ChannelSelect"><code>discord.ui.ChannelSelect</code></a> | List\[Union\[<a href="#discord.app_commands.AppCommandChannel" title="discord.app_commands.AppCommandChannel"><code>AppCommandChannel</code></a>, <a href="#discord.app_commands.AppCommandThread" title="discord.app_commands.AppCommandThread"><code>AppCommandThread</code></a>]] |

Example

```
class MyView(discord.ui.LayoutView):
    action_row = discord.ui.ActionRow()

    @action_row.select(cls=ChannelSelect, channel_types=[discord.ChannelType.text])
    async def select_channels(self, interaction: discord.Interaction, select: ChannelSelect):
        return await interaction.response.send_message(f'You selected {select.values[0].mention}')

```

<dl><dt>Parameters</dt>
<dd>

- **cls** (Union\[Type\[<a href="#discord.ui.Select" title="discord.ui.Select"><code>discord.ui.Select</code></a>], Type\[<a href="#discord.ui.UserSelect" title="discord.ui.UserSelect"><code>discord.ui.UserSelect</code></a>], Type\[<a href="#discord.ui.RoleSelect" title="discord.ui.RoleSelect"><code>discord.ui.RoleSelect</code></a>], Type\[<a href="#discord.ui.MentionableSelect" title="discord.ui.MentionableSelect"><code>discord.ui.MentionableSelect</code></a>], Type\[<a href="#discord.ui.ChannelSelect" title="discord.ui.ChannelSelect"><code>discord.ui.ChannelSelect</code></a>]]) – The class to use for the select menu. Defaults to <a href="#discord.ui.Select" title="discord.ui.Select"><code>discord.ui.Select</code></a>. You can use other select types to display different select menus to the user. See the table above for the different values you can get from each select type. Subclasses work as well, however the callback in the subclass will get overridden.
- **placeholder** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The placeholder text that is shown if nothing is selected, if any. Can only be up to 150 characters.
- **custom\_id** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The ID of the select menu that gets received during an interaction. It is recommended not to set this parameter to prevent conflicts. Can only be up to 100 characters.
- **min\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The minimum number of items that must be chosen for this select menu. Defaults to 1 and must be between 0 and 25.
- **max\_values** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The maximum number of items that must be chosen for this select menu. Defaults to 1 and must be between 1 and 25.
- **options** (List\[<a href="#discord.SelectOption" title="discord.SelectOption"><code>discord.SelectOption</code></a>]) – A list of options that can be selected in this menu. This can only be used with <a href="#discord.ui.Select" title="discord.ui.Select"><code>Select</code></a> instances. Can only contain up to 25 items.
- **channel\_types** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelType" title="discord.ChannelType"><code>ChannelType</code></a>]) – The types of channels to show in the select menu. Defaults to all channels. This can only be used with <a href="#discord.ui.ChannelSelect" title="discord.ui.ChannelSelect"><code>ChannelSelect</code></a> instances.
- **disabled** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the select is disabled or not. Defaults to <code>False</code>.
- **default\_values** (Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – A list of objects representing the default values for the select menu. This cannot be used with regular <a href="#discord.ui.Select" title="discord.ui.Select"><code>Select</code></a> instances. If <code>cls</code> is <a href="#discord.ui.MentionableSelect" title="discord.ui.MentionableSelect"><code>MentionableSelect</code></a> and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Object" title="discord.Object"><code>Object</code></a> is passed, then the type must be specified in the constructor. Number of items must be in range of <code>min_values</code> and <code>max_values</code>.
- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of the component. This must be unique across the view.

  New in version 2.6.

</dd></dl></dd>
</dl></dd>
</dl>

### FileUpload ¶

Attributes

- [custom\_id](#discord.ui.FileUpload.custom_id)
- [id](#discord.ui.FileUpload.id)
- [max\_values](#discord.ui.FileUpload.max_values)
- [min\_values](#discord.ui.FileUpload.min_values)
- [parent](#discord.ui.FileUpload.parent)
- [required](#discord.ui.FileUpload.required)
- [values](#discord.ui.FileUpload.values)
- [view](#discord.ui.FileUpload.view)

<dl><dt>*class*discord.ui.FileUpload(***, *custom_id=...*, *required=True*, *min_values=None*, *max_values=None*, *id=None*)<a href="#discord.ui.FileUpload" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a file upload component within a modal.

New in version 2.7.

<dl><dt>Parameters</dt>
<dd>

- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of the component. This must be unique across the view.
- **custom\_id** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The custom ID of the file upload component.
- **max\_values** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The maximum number of files that can be uploaded in this component. Must be between 1 and 10. Defaults to 1.
- **min\_values** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The minimum number of files that must be uploaded in this component. Must be between 0 and 10. Defaults to 0.
- **required** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this component is required to be filled before submitting the modal. Defaults to <code>True</code>.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.FileUpload.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*values<a href="#discord.ui.FileUpload.values" title="Permalink to this definition">¶</a></dt>
<dd>

The list of attachments uploaded by the user.

You can call <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Attachment.to_file" title="discord.Attachment.to_file"><code>to_file()</code></a> on each attachment to get a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>File</code></a> for sending.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Attachment" title="discord.Attachment"><code>discord.Attachment</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.FileUpload.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the component that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*min_values<a href="#discord.ui.FileUpload.min_values" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum number of files that must be user upload before submitting the modal.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*max_values<a href="#discord.ui.FileUpload.max_values" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of files that the user must upload before submitting the modal.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*required<a href="#discord.ui.FileUpload.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the component is required or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.FileUpload.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.FileUpload.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

### RadioGroup ¶

Attributes

- [custom\_id](#discord.ui.RadioGroup.custom_id)
- [id](#discord.ui.RadioGroup.id)
- [options](#discord.ui.RadioGroup.options)
- [parent](#discord.ui.RadioGroup.parent)
- [required](#discord.ui.RadioGroup.required)
- [type](#discord.ui.RadioGroup.type)
- [value](#discord.ui.RadioGroup.value)
- [view](#discord.ui.RadioGroup.view)

Methods

- def [add\_option](#discord.ui.RadioGroup.add_option)
- def [append\_option](#discord.ui.RadioGroup.append_option)

<dl><dt>*class*discord.ui.RadioGroup(***, *custom_id=...*, *required=True*, *options=...*, *id=None*)<a href="#discord.ui.RadioGroup" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a radio group component within a modal.

New in version 2.7.

<dl><dt>Parameters</dt>
<dd>

- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of the component. This must be unique across the view.
- **custom\_id** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The custom ID of the component.
- **options** (List\[<a href="#discord.RadioGroupOption" title="discord.RadioGroupOption"><code>discord.RadioGroupOption</code></a>]) – A list of options that can be selected in this radio group. Can contain between 2 and 10 items.
- **required** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this component is required to be filled before submitting the modal. Defaults to <code>True</code>.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.RadioGroup.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*value<a href="#discord.ui.RadioGroup.value" title="Permalink to this definition">¶</a></dt>
<dd>

The value have been selected by the user, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.RadioGroup.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the component that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.ui.RadioGroup.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of this component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*options<a href="#discord.ui.RadioGroup.options" title="Permalink to this definition">¶</a></dt>
<dd>

A list of options that can be selected in this radio group.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.RadioGroupOption" title="discord.RadioGroupOption"><code>discord.RadioGroupOption</code></a>]

</dd></dl></dd>
</dl><dl><dt>add_option(***, *label*, *value=...*, *description=None*, *default=False*)<a href="#discord.ui.RadioGroup.add_option" title="Permalink to this definition">¶</a></dt>
<dd>

Adds an option to the group.

To append a pre-existing <a href="#discord.RadioGroupOption" title="discord.RadioGroupOption"><code>discord.RadioGroupOption</code></a> use the <a href="#discord.ui.RadioGroup.append_option" title="discord.ui.RadioGroup.append_option"><code>append_option()</code></a> method instead.

<dl><dt>Parameters</dt>
<dd>

- **label** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The label of the option. This is displayed to users. Can only be up to 100 characters.
- **value** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The value of the option. This is not displayed to users. If not given, defaults to the label. Can only be up to 100 characters.
- **description** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – An additional description of the option, if any. Can only be up to 100 characters.
- **default** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this option is selected by default.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The number of options exceeds 10.

</dd></dl></dd>
</dl><dl><dt>append_option(*option*)<a href="#discord.ui.RadioGroup.append_option" title="Permalink to this definition">¶</a></dt>
<dd>

Appends an option to the group.

<dl><dt>Parameters</dt>
<dd>

**option** (<a href="#discord.RadioGroupOption" title="discord.RadioGroupOption"><code>discord.RadioGroupOption</code></a>) – The option to append to the group.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The number of options exceeds 10.

</dd></dl></dd>
</dl><dl><dt>*property*required<a href="#discord.ui.RadioGroup.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the component is required or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.RadioGroup.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.RadioGroup.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

### Checkbox ¶

Attributes

- [custom\_id](#discord.ui.Checkbox.custom_id)
- [default](#discord.ui.Checkbox.default)
- [id](#discord.ui.Checkbox.id)
- [parent](#discord.ui.Checkbox.parent)
- [type](#discord.ui.Checkbox.type)
- [value](#discord.ui.Checkbox.value)
- [view](#discord.ui.Checkbox.view)

<dl><dt>*class*discord.ui.Checkbox(***, *custom_id=...*, *default=False*, *id=None*)<a href="#discord.ui.Checkbox" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a checkbox component within a modal.

New in version 2.7.

<dl><dt>Parameters</dt>
<dd>

- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of the component. This must be unique across the view.
- **custom\_id** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The custom ID of the component.
- **default** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this checkbox is selected by default.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.Checkbox.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*value<a href="#discord.ui.Checkbox.value" title="Permalink to this definition">¶</a></dt>
<dd>

<code>True</code> if this checkbox was selected, otherwise <code>False</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.Checkbox.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.Checkbox.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.Checkbox.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the component that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.ui.Checkbox.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of this component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*default<a href="#discord.ui.Checkbox.default" title="Permalink to this definition">¶</a></dt>
<dd>

Whether this checkbox is selected by default.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### CheckboxGroup ¶

Attributes

- [custom\_id](#discord.ui.CheckboxGroup.custom_id)
- [id](#discord.ui.CheckboxGroup.id)
- [max\_values](#discord.ui.CheckboxGroup.max_values)
- [min\_values](#discord.ui.CheckboxGroup.min_values)
- [options](#discord.ui.CheckboxGroup.options)
- [parent](#discord.ui.CheckboxGroup.parent)
- [required](#discord.ui.CheckboxGroup.required)
- [type](#discord.ui.CheckboxGroup.type)
- [values](#discord.ui.CheckboxGroup.values)
- [view](#discord.ui.CheckboxGroup.view)

Methods

- def [add\_option](#discord.ui.CheckboxGroup.add_option)
- def [append\_option](#discord.ui.CheckboxGroup.append_option)

<dl><dt>*class*discord.ui.CheckboxGroup(***, *custom_id=...*, *required=True*, *min_values=None*, *max_values=None*, *options=...*, *id=None*)<a href="#discord.ui.CheckboxGroup" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a checkbox group component within a modal.

New in version 2.7.

<dl><dt>Parameters</dt>
<dd>

- **id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The ID of the component. This must be unique across the view.
- **custom\_id** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The custom ID of the component.
- **options** (List\[<a href="#discord.CheckboxGroupOption" title="discord.CheckboxGroupOption"><code>discord.CheckboxGroupOption</code></a>]) – A list of options that can be selected in this checkbox group. Can only contain up to 10 items.
- **max\_values** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The maximum number of options that can be selected in this component. Must be between 1 and 10. Defaults to 1.
- **min\_values** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The minimum number of options that must be selected in this component. Must be between 0 and 10. Defaults to 0.
- **required** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this component is required to be filled before submitting the modal. Defaults to <code>True</code>.

</dd></dl><dl><dt>*property*id<a href="#discord.ui.CheckboxGroup.id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of this component.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*values<a href="#discord.ui.CheckboxGroup.values" title="Permalink to this definition">¶</a></dt>
<dd>

A list of values that have been selected by the user.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*custom_id<a href="#discord.ui.CheckboxGroup.custom_id" title="Permalink to this definition">¶</a></dt>
<dd>

The ID of the component that gets received during an interaction.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*type<a href="#discord.ui.CheckboxGroup.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of this component.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ComponentType" title="discord.ComponentType"><code>ComponentType</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*options<a href="#discord.ui.CheckboxGroup.options" title="Permalink to this definition">¶</a></dt>
<dd>

A list of options that can be selected in this menu.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.CheckboxGroupOption" title="discord.CheckboxGroupOption"><code>discord.CheckboxGroupOption</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*min_values<a href="#discord.ui.CheckboxGroup.min_values" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum number of options that must be selected before submitting the modal.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*max_values<a href="#discord.ui.CheckboxGroup.max_values" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of options that can be selected before submitting the modal.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>add_option(***, *label*, *value=...*, *description=None*, *default=False*)<a href="#discord.ui.CheckboxGroup.add_option" title="Permalink to this definition">¶</a></dt>
<dd>

Adds an option to the checkbox group.

To append a pre-existing <a href="#discord.CheckboxGroupOption" title="discord.CheckboxGroupOption"><code>discord.CheckboxGroupOption</code></a> use the <a href="#discord.ui.CheckboxGroup.append_option" title="discord.ui.CheckboxGroup.append_option"><code>append_option()</code></a> method instead.

<dl><dt>Parameters</dt>
<dd>

- **label** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The label of the option. This is displayed to users. Can only be up to 100 characters.
- **value** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The value of the option. This is not displayed to users. If not given, defaults to the label. Can only be up to 100 characters.
- **description** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – An additional description of the option, if any. Can only be up to 100 characters.
- **default** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this option is selected by default.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The number of options exceeds 10.

</dd></dl></dd>
</dl><dl><dt>append_option(*option*)<a href="#discord.ui.CheckboxGroup.append_option" title="Permalink to this definition">¶</a></dt>
<dd>

Appends an option to the checkbox group.

<dl><dt>Parameters</dt>
<dd>

**option** (<a href="#discord.CheckboxGroupOption" title="discord.CheckboxGroupOption"><code>discord.CheckboxGroupOption</code></a>) – The option to append to the checkbox group.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The number of options exceeds 10.

</dd></dl></dd>
</dl><dl><dt>*property*required<a href="#discord.ui.CheckboxGroup.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the component is required or not.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parent<a href="#discord.ui.CheckboxGroup.parent" title="Permalink to this definition">¶</a></dt>
<dd>

This item’s parent, if applicable. Only available on items with children.

New in version 2.6.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ui.Item" title="discord.ui.Item"><code>Item</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*view<a href="#discord.ui.CheckboxGroup.view" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying view for this item.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

## Application Commands ¶

The library has helpers to aid in creation of application commands. These are all in the `discord.app_commands` package.

### CommandTree ¶

Attributes

- [translator](#discord.app_commands.CommandTree.translator)

Methods

- def [add\_command](#discord.app_commands.CommandTree.add_command)
- def [clear\_commands](#discord.app_commands.CommandTree.clear_commands)
- @ [command](#discord.app_commands.CommandTree.command)
- @ [context\_menu](#discord.app_commands.CommandTree.context_menu)
- def [copy\_global\_to](#discord.app_commands.CommandTree.copy_global_to)
- @ [error](#discord.app_commands.CommandTree.error)
- async [fetch\_command](#discord.app_commands.CommandTree.fetch_command)
- async [fetch\_commands](#discord.app_commands.CommandTree.fetch_commands)
- def [get\_command](#discord.app_commands.CommandTree.get_command)
- def [get\_commands](#discord.app_commands.CommandTree.get_commands)
- async [interaction\_check](#discord.app_commands.CommandTree.interaction_check)
- async [on\_error](#discord.app_commands.CommandTree.on_error)
- def [remove\_command](#discord.app_commands.CommandTree.remove_command)
- async [set\_translator](#discord.app_commands.CommandTree.set_translator)
- async [sync](#discord.app_commands.CommandTree.sync)
- def [walk\_commands](#discord.app_commands.CommandTree.walk_commands)

<dl><dt>*class*discord.app_commands.CommandTree(*client*, ***, *fallback_to_global=True*, *allowed_contexts=...*, *allowed_installs=...*)<a href="#discord.app_commands.CommandTree" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a container that holds application command information.

<dl><dt>Parameters</dt>
<dd>

- **client** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client" title="discord.Client"><code>Client</code></a>) – The client instance to get application command information from.
- **fallback\_to\_global** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If a guild-specific command is not found when invoked, then try falling back into a global command in the tree. For example, if the tree locally has a <code>/ping</code> command under the global namespace but the guild has a guild-specific <code>/ping</code>, instead of failing to find the guild-specific <code>/ping</code> command it will fall back to the global <code>/ping</code> command. This has the potential to raise more <a href="#discord.app_commands.CommandSignatureMismatch" title="discord.app_commands.CommandSignatureMismatch"><code>CommandSignatureMismatch</code></a> errors than usual. Defaults to <code>True</code>.
- **allowed\_contexts** (<a href="#discord.app_commands.AppCommandContext" title="discord.app_commands.AppCommandContext"><code>AppCommandContext</code></a>) –

  The default allowed contexts that applies to all commands in this tree. Note that you can override this on a per command basis.

  New in version 2.4.
- **allowed\_installs** (<a href="#discord.app_commands.AppInstallationType" title="discord.app_commands.AppInstallationType"><code>AppInstallationType</code></a>) –

  The default allowed install locations that apply to all commands in this tree. Note that you can override this on a per command basis.

  New in version 2.4.

</dd></dl><dl><dt>@command(***, *name=...*, *description=...*, *nsfw=False*, *guild=...*, *guilds=...*, *auto_locale_strings=True*, *extras=...*)<a href="#discord.app_commands.CommandTree.command" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that creates an application command from a regular function directly under this tree.

<dl><dt>Parameters</dt>
<dd>

- **name** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The name of the application command. If not given, it defaults to a lower-case version of the callback name.
- **description** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The description of the application command. This shows up in the UI to describe the application command. If not given, it defaults to the first line of the docstring of the callback shortened to 100 characters.
- **nsfw** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the command is NSFW and should only work in NSFW channels. Defaults to <code>False</code>.

  Due to a Discord limitation, this does not work on subcommands.
- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  The guild to add the command to. If not given or <code>None</code> then it becomes a global command instead.

  Note

  Due to a Discord limitation, this keyword argument cannot be used in conjunction with contexts (e.g. <a href="#discord.app_commands.allowed_contexts" title="discord.app_commands.allowed_contexts"><code>app_commands.allowed_contexts()</code></a>) or installation types (e.g. <a href="#discord.app_commands.allowed_installs" title="discord.app_commands.allowed_installs"><code>app_commands.allowed_installs()</code></a>).
- **guilds** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  The list of guilds to add the command to. This cannot be mixed with the <code>guild</code> parameter. If no guilds are given at all then it becomes a global command instead.

  Note

  Due to a Discord limitation, this keyword argument cannot be used in conjunction with contexts (e.g. <a href="#discord.app_commands.allowed_contexts" title="discord.app_commands.allowed_contexts"><code>app_commands.allowed_contexts()</code></a>) or installation types (e.g. <a href="#discord.app_commands.allowed_installs" title="discord.app_commands.allowed_installs"><code>app_commands.allowed_installs()</code></a>).
- **auto\_locale\_strings** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If this is set to <code>True</code>, then all translatable strings will implicitly be wrapped into <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> rather than <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>. This could avoid some repetition and be more ergonomic for certain defaults such as default command names, command descriptions, and parameter names. Defaults to <code>True</code>.
- **extras** (<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>) – A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.

</dd></dl></dd>
</dl><dl><dt>@context_menu(***, *name=...*, *nsfw=False*, *guild=...*, *guilds=...*, *auto_locale_strings=True*, *extras=...*)<a href="#discord.app_commands.CommandTree.context_menu" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that creates an application command context menu from a regular function directly under this tree.

This function must have a signature of <a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a> as its first parameter and taking either a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a>, or <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>, or a <a href="https://docs.python.org/3/library/typing.html#typing.Union" title="(in Python v3.14)"><code>typing.Union</code></a> of <code>Member</code> and <code>User</code> as its second parameter.

Examples

```
@app_commands.context_menu()
async def react(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message('Very cool message!', ephemeral=True)

@app_commands.context_menu()
async def ban(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(f'Should I actually ban {user}...', ephemeral=True)

```

<dl><dt>Parameters</dt>
<dd>

- **name** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The name of the context menu command. If not given, it defaults to a title-case version of the callback name. Note that unlike regular slash commands this can have spaces and upper case characters in the name.
- **nsfw** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the command is NSFW and should only work in NSFW channels. Defaults to <code>False</code>.

  Due to a Discord limitation, this does not work on subcommands.
- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  The guild to add the command to. If not given or <code>None</code> then it becomes a global command instead.

  Note

  Due to a Discord limitation, this keyword argument cannot be used in conjunction with contexts (e.g. <a href="#discord.app_commands.allowed_contexts" title="discord.app_commands.allowed_contexts"><code>app_commands.allowed_contexts()</code></a>) or installation types (e.g. <a href="#discord.app_commands.allowed_installs" title="discord.app_commands.allowed_installs"><code>app_commands.allowed_installs()</code></a>).
- **guilds** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  The list of guilds to add the command to. This cannot be mixed with the <code>guild</code> parameter. If no guilds are given at all then it becomes a global command instead.

  Note

  Due to a Discord limitation, this keyword argument cannot be used in conjunction with contexts (e.g. <a href="#discord.app_commands.allowed_contexts" title="discord.app_commands.allowed_contexts"><code>app_commands.allowed_contexts()</code></a>) or installation types (e.g. <a href="#discord.app_commands.allowed_installs" title="discord.app_commands.allowed_installs"><code>app_commands.allowed_installs()</code></a>).
- **auto\_locale\_strings** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If this is set to <code>True</code>, then all translatable strings will implicitly be wrapped into <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> rather than <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>. This could avoid some repetition and be more ergonomic for certain defaults such as default command names, command descriptions, and parameter names. Defaults to <code>True</code>.
- **extras** (<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>) – A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.

</dd></dl></dd>
</dl><dl><dt>@error(*coro*)<a href="#discord.app_commands.CommandTree.error" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a local error handler.

This must match the signature of the <a href="#discord.app_commands.CommandTree.on_error" title="discord.app_commands.CommandTree.on_error"><code>on_error()</code></a> callback.

The error passed will be derived from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the local error handler.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine or does not match the signature.

</dd></dl></dd>
</dl><dl><dt>*await* fetch_command(*command_id*, */*, ***, *guild=None*)<a href="#discord.app_commands.CommandTree.fetch_command" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Fetches an application command from the application.

<dl><dt>Parameters</dt>
<dd>

- **command\_id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID of the command to fetch.
- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – The guild to fetch the command from. If not passed then the global command is fetched instead.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Fetching the command failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The application ID could not be found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The application command was not found. This could also be because the command is a guild command and the guild was not specified and vice versa.

</dd><dt>Returns</dt>
<dd>

The application command.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.app_commands.AppCommand" title="discord.app_commands.AppCommand"><code>AppCommand</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_commands(***, *guild=None*)<a href="#discord.app_commands.CommandTree.fetch_commands" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Fetches the application’s current commands.

If no guild is passed then global commands are fetched, otherwise the guild’s commands are fetched instead.

Note

This includes context menu commands.

<dl><dt>Parameters</dt>
<dd>

**guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – The guild to fetch the commands from. If not passed then global commands are fetched instead.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Fetching the commands failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The application ID could not be found.

</dd><dt>Returns</dt>
<dd>

The application’s commands.

</dd><dt>Return type</dt>
<dd>

List\[<a href="#discord.app_commands.AppCommand" title="discord.app_commands.AppCommand"><code>AppCommand</code></a>]

</dd></dl></dd>
</dl><dl><dt>copy_global_to(***, *guild*)<a href="#discord.app_commands.CommandTree.copy_global_to" title="Permalink to this definition">¶</a></dt>
<dd>

Copies all global commands to the specified guild.

This method is mainly available for development purposes, as it allows you to copy your global commands over to a testing guild easily.

Note that this method will *override* pre-existing guild commands that would conflict.

<dl><dt>Parameters</dt>
<dd>

**guild** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>) – The guild to copy the commands to.

</dd><dt>Raises</dt>
<dd>

<a href="#discord.app_commands.CommandLimitReached" title="discord.app_commands.CommandLimitReached">**CommandLimitReached**</a> – The maximum number of commands was reached for that guild. This is currently 100 for slash commands and 5 for context menu commands.

</dd></dl></dd>
</dl><dl><dt>add_command(*command*, */*, ***, *guild=...*, *guilds=...*, *override=False*)<a href="#discord.app_commands.CommandTree.add_command" title="Permalink to this definition">¶</a></dt>
<dd>

Adds an application command to the tree.

This only adds the command locally – in order to sync the commands and enable them in the client, <a href="#discord.app_commands.CommandTree.sync" title="discord.app_commands.CommandTree.sync"><code>sync()</code></a> must be called.

The root parent of the command is added regardless of the type passed.

<dl><dt>Parameters</dt>
<dd>

- **command** (Union\[<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]) – The application command or group to add.
- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  The guild to add the command to. If not given or <code>None</code> then it becomes a global command instead.

  Note

  Due to a Discord limitation, this keyword argument cannot be used in conjunction with contexts (e.g. <a href="#discord.app_commands.allowed_contexts" title="discord.app_commands.allowed_contexts"><code>app_commands.allowed_contexts()</code></a>) or installation types (e.g. <a href="#discord.app_commands.allowed_installs" title="discord.app_commands.allowed_installs"><code>app_commands.allowed_installs()</code></a>).
- **guilds** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  The list of guilds to add the command to. This cannot be mixed with the <code>guild</code> parameter. If no guilds are given at all then it becomes a global command instead.

  Note

  Due to a Discord limitation, this keyword argument cannot be used in conjunction with contexts (e.g. <a href="#discord.app_commands.allowed_contexts" title="discord.app_commands.allowed_contexts"><code>app_commands.allowed_contexts()</code></a>) or installation types (e.g. <a href="#discord.app_commands.allowed_installs" title="discord.app_commands.allowed_installs"><code>app_commands.allowed_installs()</code></a>).
- **override** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to override a command with the same name. If <code>False</code> an exception is raised. Default is <code>False</code>.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.app_commands.CommandAlreadyRegistered" title="discord.app_commands.CommandAlreadyRegistered">**CommandAlreadyRegistered**</a> – The command was already registered and no override was specified.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The application command passed is not a valid application command. Or, <code>guild</code> and <code>guilds</code> were both given.
- <a href="#discord.app_commands.CommandLimitReached" title="discord.app_commands.CommandLimitReached">**CommandLimitReached**</a> – The maximum number of commands was reached globally or for that guild. This is currently 100 for slash commands and 5 for context menu commands.

</dd></dl></dd>
</dl><dl><dt>remove_command(*command*, */*, ***, *guild=None*, *type=&lt;AppCommandType.chat_input: 1&gt;*)<a href="#discord.app_commands.CommandTree.remove_command" title="Permalink to this definition">¶</a></dt>
<dd>

Removes an application command from the tree.

This only removes the command locally – in order to sync the commands and remove them in the client, <a href="#discord.app_commands.CommandTree.sync" title="discord.app_commands.CommandTree.sync"><code>sync()</code></a> must be called.

<dl><dt>Parameters</dt>
<dd>

- **command** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the root command to remove.
- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – The guild to remove the command from. If not given or <code>None</code> then it removes a global command instead.
- **type** (<a href="#discord.AppCommandType" title="discord.AppCommandType"><code>AppCommandType</code></a>) – The type of command to remove. Defaults to <a href="#discord.AppCommandType.chat_input" title="discord.AppCommandType.chat_input"><code>chat_input</code></a>, i.e. slash commands.

</dd><dt>Returns</dt>
<dd>

The application command that got removed. If nothing was removed then <code>None</code> is returned instead.

</dd><dt>Return type</dt>
<dd>

Optional\[Union\[<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.ContextMenu" title="discord.app_commands.ContextMenu"><code>ContextMenu</code></a>, <a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]]

</dd></dl></dd>
</dl><dl><dt>clear_commands(***, *guild*, *type=None*)<a href="#discord.app_commands.CommandTree.clear_commands" title="Permalink to this definition">¶</a></dt>
<dd>

Clears all application commands from the tree.

This only removes the commands locally – in order to sync the commands and remove them in the client, <a href="#discord.app_commands.CommandTree.sync" title="discord.app_commands.CommandTree.sync"><code>sync()</code></a> must be called.

<dl><dt>Parameters</dt>
<dd>

- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – The guild to remove the commands from. If <code>None</code> then it removes all global commands instead.
- **type** (<a href="#discord.AppCommandType" title="discord.AppCommandType"><code>AppCommandType</code></a>) – The type of command to clear. If not given or <code>None</code> then it removes all commands regardless of the type.

</dd></dl></dd>
</dl><dl><dt>get_command(*command*, */*, ***, *guild=None*, *type=&lt;AppCommandType.chat_input: 1&gt;*)<a href="#discord.app_commands.CommandTree.get_command" title="Permalink to this definition">¶</a></dt>
<dd>

Gets an application command from the tree.

<dl><dt>Parameters</dt>
<dd>

- **command** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the root command to get.
- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – The guild to get the command from. If not given or <code>None</code> then it gets a global command instead.
- **type** (<a href="#discord.AppCommandType" title="discord.AppCommandType"><code>AppCommandType</code></a>) – The type of command to get. Defaults to <a href="#discord.AppCommandType.chat_input" title="discord.AppCommandType.chat_input"><code>chat_input</code></a>, i.e. slash commands.

</dd><dt>Returns</dt>
<dd>

The application command that was found. If nothing was found then <code>None</code> is returned instead.

</dd><dt>Return type</dt>
<dd>

Optional\[Union\[<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.ContextMenu" title="discord.app_commands.ContextMenu"><code>ContextMenu</code></a>, <a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]]

</dd></dl></dd>
</dl><dl><dt>get_commands(***, *guild=None*, *type=None*)<a href="#discord.app_commands.CommandTree.get_commands" title="Permalink to this definition">¶</a></dt>
<dd>

Gets all application commands from the tree.

<dl><dt>Parameters</dt>
<dd>

- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – The guild to get the commands from, not including global commands. If not given or <code>None</code> then only global commands are returned.
- **type** (Optional\[<a href="#discord.AppCommandType" title="discord.AppCommandType"><code>AppCommandType</code></a>]) – The type of commands to get. When not given or <code>None</code>, then all command types are returned.

</dd><dt>Returns</dt>
<dd>

The application commands from the tree.

</dd><dt>Return type</dt>
<dd>

List\[Union\[<a href="#discord.app_commands.ContextMenu" title="discord.app_commands.ContextMenu"><code>ContextMenu</code></a>, <a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*for ... in* walk_commands(***, *guild=None*, *type=&lt;AppCommandType.chat_input: 1&gt;*)<a href="#discord.app_commands.CommandTree.walk_commands" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all application commands and child commands from the tree.

<dl><dt>Parameters</dt>
<dd>

- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – The guild to iterate the commands from, not including global commands. If not given or <code>None</code> then only global commands are iterated.
- **type** (<a href="#discord.AppCommandType" title="discord.AppCommandType"><code>AppCommandType</code></a>) – The type of commands to iterate over. Defaults to <a href="#discord.AppCommandType.chat_input" title="discord.AppCommandType.chat_input"><code>chat_input</code></a>, i.e. slash commands.

</dd><dt>Yields</dt>
<dd>

Union\[<a href="#discord.app_commands.ContextMenu" title="discord.app_commands.ContextMenu"><code>ContextMenu</code></a>, <a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>] – The application commands from the tree.

</dd></dl></dd>
</dl><dl><dt>*await* on_error(*interaction*, *error*, */*)<a href="#discord.app_commands.CommandTree.on_error" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when any command raises an <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

The default implementation logs the exception using the library logger if the command does not have any error handlers attached to it.

To get the command that failed, <a href="#discord.Interaction.command" title="discord.Interaction.command"><code>discord.Interaction.command</code></a> should be used.

<dl><dt>Parameters</dt>
<dd>

- **interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that is being handled.
- **error** (<a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>) – The exception that was raised.

</dd></dl></dd>
</dl><dl><dt>*property*translator<a href="#discord.app_commands.CommandTree.translator" title="Permalink to this definition">¶</a></dt>
<dd>

The translator, if any, responsible for handling translation of commands.

To change the translator, use <a href="#discord.app_commands.CommandTree.set_translator" title="discord.app_commands.CommandTree.set_translator"><code>set_translator()</code></a>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.Translator" title="discord.app_commands.Translator"><code>Translator</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* set_translator(*translator*)<a href="#discord.app_commands.CommandTree.set_translator" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Sets the translator to use for translating commands.

If a translator was previously set, it will be unloaded using its <a href="#discord.app_commands.Translator.unload" title="discord.app_commands.Translator.unload"><code>Translator.unload()</code></a> method.

When a translator is set, it will be loaded using its <a href="#discord.app_commands.Translator.load" title="discord.app_commands.Translator.load"><code>Translator.load()</code></a> method.

<dl><dt>Parameters</dt>
<dd>

**translator** (Optional\[<a href="#discord.app_commands.Translator" title="discord.app_commands.Translator"><code>Translator</code></a>]) – The translator to use. If <code>None</code> then the translator is just removed and unloaded.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The translator was not <code>None</code> or a <a href="#discord.app_commands.Translator" title="discord.app_commands.Translator"><code>Translator</code></a> instance.

</dd></dl></dd>
</dl><dl><dt>*await* sync(***, *guild=None*)<a href="#discord.app_commands.CommandTree.sync" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Syncs the application commands to Discord.

This also runs the translator to get the translated strings necessary for feeding back into Discord.

This must be called for the application commands to show up.

<dl><dt>Parameters</dt>
<dd>

**guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – The guild to sync the commands to. If <code>None</code> then it syncs all global commands instead.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Syncing the commands failed.
- <a href="#discord.app_commands.CommandSyncFailure" title="discord.app_commands.CommandSyncFailure">**CommandSyncFailure**</a> – Syncing the commands failed due to a user related error, typically because the command has invalid data. This is equivalent to an HTTP status code of 400.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – The client does not have the <code>applications.commands</code> scope in the guild.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The client does not have an application ID.
- <a href="#discord.app_commands.TranslationError" title="discord.app_commands.TranslationError">**TranslationError**</a> – An error occurred while translating the commands.

</dd><dt>Returns</dt>
<dd>

The application’s commands that got synced.

</dd><dt>Return type</dt>
<dd>

List\[<a href="#discord.app_commands.AppCommand" title="discord.app_commands.AppCommand"><code>AppCommand</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.app_commands.CommandTree.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A global check to determine if an <a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a> should be processed by the tree.

The default implementation returns True (all interactions are processed), but can be overridden if custom behaviour is desired.

</dd></dl></dd>
</dl>

### Commands ¶

#### Command ¶

Attributes

- [allowed\_contexts](#discord.app_commands.Command.allowed_contexts)
- [allowed\_installs](#discord.app_commands.Command.allowed_installs)
- [callback](#discord.app_commands.Command.callback)
- [checks](#discord.app_commands.Command.checks)
- [default\_permissions](#discord.app_commands.Command.default_permissions)
- [description](#discord.app_commands.Command.description)
- [extras](#discord.app_commands.Command.extras)
- [guild\_only](#discord.app_commands.Command.guild_only)
- [name](#discord.app_commands.Command.name)
- [nsfw](#discord.app_commands.Command.nsfw)
- [parameters](#discord.app_commands.Command.parameters)
- [parent](#discord.app_commands.Command.parent)
- [qualified\_name](#discord.app_commands.Command.qualified_name)
- [root\_parent](#discord.app_commands.Command.root_parent)

Methods

- def [add\_check](#discord.app_commands.Command.add_check)
- @ [autocomplete](#discord.app_commands.Command.autocomplete)
- @ [error](#discord.app_commands.Command.error)
- def [get\_parameter](#discord.app_commands.Command.get_parameter)
- def [remove\_check](#discord.app_commands.Command.remove_check)

<dl><dt>*class*discord.app_commands.Command(***, *name*, *description*, *callback*, *nsfw=False*, *parent=None*, *guild_ids=None*, *allowed_contexts=None*, *allowed_installs=None*, *auto_locale_strings=True*, *extras=...*)<a href="#discord.app_commands.Command" title="Permalink to this definition">¶</a></dt>
<dd>

A class that implements an application command.

These are usually not created manually, instead they are created using one of the following decorators:

- <a href="#discord.app_commands.command" title="discord.app_commands.command"><code>command()</code></a>
- <a href="#discord.app_commands.Group.command" title="discord.app_commands.Group.command"><code>Group.command</code></a>
- <a href="#discord.app_commands.CommandTree.command" title="discord.app_commands.CommandTree.command"><code>CommandTree.command</code></a>

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **name** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The name of the application command.
- **description** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The description of the application command. This shows up in the UI to describe the application command.
- **callback** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine that is executed when the command is called.
- **auto\_locale\_strings** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If this is set to <code>True</code>, then all translatable strings will implicitly be wrapped into <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> rather than <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>. This could avoid some repetition and be more ergonomic for certain defaults such as default command names, command descriptions, and parameter names. Defaults to <code>True</code>.
- **nsfw** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the command is NSFW and should only work in NSFW channels. Defaults to <code>False</code>.

  Due to a Discord limitation, this does not work on subcommands.
- **parent** (Optional\[<a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]) – The parent application command. <code>None</code> if there isn’t one.
- **extras** (<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>) – A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.

</dd></dl><dl><dt>name<a href="#discord.app_commands.Command.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the application command.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.app_commands.Command.description" title="Permalink to this definition">¶</a></dt>
<dd>

The description of the application command. This shows up in the UI to describe the application command.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>checks<a href="#discord.app_commands.Command.checks" title="Permalink to this definition">¶</a></dt>
<dd>

A list of predicates that take a <a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a> parameter to indicate whether the command callback should be executed. If an exception is necessary to be thrown to signal failure, then one inherited from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a> should be used. If all the checks fail without propagating an exception, <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a> is raised.

</dd></dl><dl><dt>default_permissions<a href="#discord.app_commands.Command.default_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The default permissions that can execute this command on Discord. Note that server administrators can override this value in the client. Setting an empty permissions field will disallow anyone except server administrators from using the command in a guild.

Due to a Discord limitation, this does not work on subcommands.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>]

</dd></dl></dd>
</dl><dl><dt>guild_only<a href="#discord.app_commands.Command.guild_only" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the command should only be usable in guild contexts.

Due to a Discord limitation, this does not work on subcommands.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>allowed_contexts<a href="#discord.app_commands.Command.allowed_contexts" title="Permalink to this definition">¶</a></dt>
<dd>

The contexts that the command is allowed to be used in. Overrides <code>guild_only</code> if this is set.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.AppCommandContext" title="discord.app_commands.AppCommandContext"><code>AppCommandContext</code></a>]

</dd></dl></dd>
</dl><dl><dt>allowed_installs<a href="#discord.app_commands.Command.allowed_installs" title="Permalink to this definition">¶</a></dt>
<dd>

The installation contexts that the command is allowed to be installed on.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.AppInstallationType" title="discord.app_commands.AppInstallationType"><code>AppInstallationType</code></a>]

</dd></dl></dd>
</dl><dl><dt>nsfw<a href="#discord.app_commands.Command.nsfw" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the command is NSFW and should only work in NSFW channels.

Due to a Discord limitation, this does not work on subcommands.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>parent<a href="#discord.app_commands.Command.parent" title="Permalink to this definition">¶</a></dt>
<dd>

The parent application command. <code>None</code> if there isn’t one.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>extras<a href="#discord.app_commands.Command.extras" title="Permalink to this definition">¶</a></dt>
<dd>

A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

</dd></dl></dd>
</dl><dl><dt>@autocomplete(*name*)<a href="#discord.app_commands.Command.autocomplete" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as an autocomplete prompt for a parameter.

The coroutine callback must have 2 parameters, the <a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>, and the current value by the user (the string currently being typed by the user).

To get the values from other parameters that may be filled in, accessing <a href="#discord.Interaction.namespace" title="discord.Interaction.namespace"><code>Interaction.namespace</code></a> will give a <a href="#discord.app_commands.Namespace" title="discord.app_commands.Namespace"><code>Namespace</code></a> object with those values.

Parent <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>checks</code></a> are ignored within an autocomplete. However, checks can be added to the autocomplete callback and the ones added will be called. If the checks fail for any reason then an empty list is sent as the interaction response.

The coroutine decorator **must** return a list of <a href="#discord.app_commands.Choice" title="discord.app_commands.Choice"><code>Choice</code></a> objects. Only up to 25 objects are supported.

Warning

The choices returned from this coroutine are suggestions. The user may ignore them and input their own value.

Example:

```
@app_commands.command()
async def fruits(interaction: discord.Interaction, fruit: str):
    await interaction.response.send_message(f'Your favourite fruit seems to be {fruit}')

@fruits.autocomplete('fruit')
async def fruits_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    fruits = ['Banana', 'Pineapple', 'Apple', 'Watermelon', 'Melon', 'Cherry']
    return [
        app_commands.Choice(name=fruit, value=fruit)
        for fruit in fruits if current.lower() in fruit.lower()
    ]

```

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The parameter name to register as autocomplete.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine or the parameter is not found or of an invalid type.

</dd></dl></dd>
</dl><dl><dt>@error(*coro*)<a href="#discord.app_commands.Command.error" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a local error handler.

The local error handler is called whenever an exception is raised in the body of the command or during handling of the command. The error handler must take 2 parameters, the interaction and the error.

The error passed will be derived from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the local error handler.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>*property*callback<a href="#discord.app_commands.Command.callback" title="Permalink to this definition">¶</a></dt>
<dd>

The coroutine that is executed when the command is called.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>

</dd></dl></dd>
</dl><dl><dt>*property*parameters<a href="#discord.app_commands.Command.parameters" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a list of parameters for this command.

This does not include the <code>self</code> or <code>interaction</code> parameters.

<dl><dt>Returns</dt>
<dd>

The parameters of this command.

</dd><dt>Return type</dt>
<dd>

List\[<a href="#discord.app_commands.Parameter" title="discord.app_commands.Parameter"><code>Parameter</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_parameter(*name*)<a href="#discord.app_commands.Command.get_parameter" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves a parameter by its name.

The name must be the Python identifier rather than the renamed one for display on Discord.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The parameter name in the callback function.

</dd><dt>Returns</dt>
<dd>

The parameter or <code>None</code> if not found.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.app_commands.Parameter" title="discord.app_commands.Parameter"><code>Parameter</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*root_parent<a href="#discord.app_commands.Command.root_parent" title="Permalink to this definition">¶</a></dt>
<dd>

The root parent of this command.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*qualified_name<a href="#discord.app_commands.Command.qualified_name" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the fully qualified command name.

The qualified name includes the parent name as well. For example, in a command like <code>/foo bar</code> the qualified name is <code>foo bar</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>add_check(*func*, */*)<a href="#discord.app_commands.Command.add_check" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a check to the command.

This is the non-decorator interface to <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a>.

<dl><dt>Parameters</dt>
<dd>

**func** – The function that will be used as a check.

</dd></dl></dd>
</dl><dl><dt>remove_check(*func*, */*)<a href="#discord.app_commands.Command.remove_check" title="Permalink to this definition">¶</a></dt>
<dd>

Removes a check from the command.

This function is idempotent and will not raise an exception if the function is not in the command’s checks.

<dl><dt>Parameters</dt>
<dd>

**func** – The function to remove from the checks.

</dd></dl></dd>
</dl></dd>
</dl>

#### Parameter ¶

Attributes

- [autocomplete](#discord.app_commands.Parameter.autocomplete)
- [channel\_types](#discord.app_commands.Parameter.channel_types)
- [choices](#discord.app_commands.Parameter.choices)
- [command](#discord.app_commands.Parameter.command)
- [default](#discord.app_commands.Parameter.default)
- [description](#discord.app_commands.Parameter.description)
- [display\_name](#discord.app_commands.Parameter.display_name)
- [locale\_description](#discord.app_commands.Parameter.locale_description)
- [locale\_name](#discord.app_commands.Parameter.locale_name)
- [max\_value](#discord.app_commands.Parameter.max_value)
- [min\_value](#discord.app_commands.Parameter.min_value)
- [name](#discord.app_commands.Parameter.name)
- [required](#discord.app_commands.Parameter.required)
- [type](#discord.app_commands.Parameter.type)

<dl><dt>*class*discord.app_commands.Parameter<a href="#discord.app_commands.Parameter" title="Permalink to this definition">¶</a></dt>
<dd>

A class that contains the parameter information of a <a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a> callback.

New in version 2.0.

<dl><dt>name<a href="#discord.app_commands.Parameter.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the parameter. This is the Python identifier for the parameter.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>display_name<a href="#discord.app_commands.Parameter.display_name" title="Permalink to this definition">¶</a></dt>
<dd>

The displayed name of the parameter on Discord.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.app_commands.Parameter.description" title="Permalink to this definition">¶</a></dt>
<dd>

The description of the parameter.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>autocomplete<a href="#discord.app_commands.Parameter.autocomplete" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the parameter has an autocomplete handler.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>locale_name<a href="#discord.app_commands.Parameter.locale_name" title="Permalink to this definition">¶</a></dt>
<dd>

The display name’s locale string, if available.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]

</dd></dl></dd>
</dl><dl><dt>locale_description<a href="#discord.app_commands.Parameter.locale_description" title="Permalink to this definition">¶</a></dt>
<dd>

The description’s locale string, if available.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]

</dd></dl></dd>
</dl><dl><dt>required<a href="#discord.app_commands.Parameter.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the parameter is required

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>choices<a href="#discord.app_commands.Parameter.choices" title="Permalink to this definition">¶</a></dt>
<dd>

A list of choices this parameter takes, if any.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.app_commands.Choice" title="discord.app_commands.Choice"><code>Choice</code></a>]

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.app_commands.Parameter.type" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying type of this parameter.

<dl><dt>Type</dt>
<dd>

<a href="#discord.AppCommandOptionType" title="discord.AppCommandOptionType"><code>AppCommandOptionType</code></a>

</dd></dl></dd>
</dl><dl><dt>channel_types<a href="#discord.app_commands.Parameter.channel_types" title="Permalink to this definition">¶</a></dt>
<dd>

The channel types that are allowed for this parameter.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelType" title="discord.ChannelType"><code>ChannelType</code></a>]

</dd></dl></dd>
</dl><dl><dt>min_value<a href="#discord.app_commands.Parameter.min_value" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum supported value for this parameter.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]]

</dd></dl></dd>
</dl><dl><dt>max_value<a href="#discord.app_commands.Parameter.max_value" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum supported value for this parameter.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]]

</dd></dl></dd>
</dl><dl><dt>default<a href="#discord.app_commands.Parameter.default" title="Permalink to this definition">¶</a></dt>
<dd>

The default value of the parameter, if given. If not given then this is <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.utils.MISSING" title="discord.utils.MISSING"><code>MISSING</code></a>.

<dl><dt>Type</dt>
<dd>

Any

</dd></dl></dd>
</dl><dl><dt>command<a href="#discord.app_commands.Parameter.command" title="Permalink to this definition">¶</a></dt>
<dd>

The command this parameter is attached to.

<dl><dt>Type</dt>
<dd>

<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

#### ContextMenu ¶

Attributes

- [allowed\_contexts](#discord.app_commands.ContextMenu.allowed_contexts)
- [allowed\_installs](#discord.app_commands.ContextMenu.allowed_installs)
- [callback](#discord.app_commands.ContextMenu.callback)
- [checks](#discord.app_commands.ContextMenu.checks)
- [default\_permissions](#discord.app_commands.ContextMenu.default_permissions)
- [extras](#discord.app_commands.ContextMenu.extras)
- [guild\_only](#discord.app_commands.ContextMenu.guild_only)
- [name](#discord.app_commands.ContextMenu.name)
- [nsfw](#discord.app_commands.ContextMenu.nsfw)
- [qualified\_name](#discord.app_commands.ContextMenu.qualified_name)
- [type](#discord.app_commands.ContextMenu.type)

Methods

- def [add\_check](#discord.app_commands.ContextMenu.add_check)
- @ [error](#discord.app_commands.ContextMenu.error)
- def [remove\_check](#discord.app_commands.ContextMenu.remove_check)

<dl><dt>*class*discord.app_commands.ContextMenu(***, *name*, *callback*, *type=...*, *nsfw=False*, *guild_ids=None*, *allowed_contexts=None*, *allowed_installs=None*, *auto_locale_strings=True*, *extras=...*)<a href="#discord.app_commands.ContextMenu" title="Permalink to this definition">¶</a></dt>
<dd>

A class that implements a context menu application command.

These are usually not created manually, instead they are created using one of the following decorators:

- <a href="#discord.app_commands.context_menu" title="discord.app_commands.context_menu"><code>context_menu()</code></a>
- <a href="#discord.app_commands.CommandTree.context_menu" title="discord.app_commands.CommandTree.context_menu"><code>CommandTree.context_menu</code></a>

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **name** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The name of the context menu.
- **callback** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine that is executed when the command is called.
- **type** (<a href="#discord.AppCommandType" title="discord.AppCommandType"><code>AppCommandType</code></a>) – The type of context menu application command. By default, this is inferred by the parameter of the callback.
- **auto\_locale\_strings** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If this is set to <code>True</code>, then all translatable strings will implicitly be wrapped into <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> rather than <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>. This could avoid some repetition and be more ergonomic for certain defaults such as default command names, command descriptions, and parameter names. Defaults to <code>True</code>.
- **nsfw** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the command is NSFW and should only work in NSFW channels. Defaults to <code>False</code>.
- **extras** (<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>) – A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.

</dd></dl><dl><dt>name<a href="#discord.app_commands.ContextMenu.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the context menu.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.app_commands.ContextMenu.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of context menu application command. By default, this is inferred by the parameter of the callback.

<dl><dt>Type</dt>
<dd>

<a href="#discord.AppCommandType" title="discord.AppCommandType"><code>AppCommandType</code></a>

</dd></dl></dd>
</dl><dl><dt>default_permissions<a href="#discord.app_commands.ContextMenu.default_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The default permissions that can execute this command on Discord. Note that server administrators can override this value in the client. Setting an empty permissions field will disallow anyone except server administrators from using the command in a guild.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>]

</dd></dl></dd>
</dl><dl><dt>guild_only<a href="#discord.app_commands.ContextMenu.guild_only" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the command should only be usable in guild contexts. Defaults to <code>False</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>allowed_contexts<a href="#discord.app_commands.ContextMenu.allowed_contexts" title="Permalink to this definition">¶</a></dt>
<dd>

The contexts that this context menu is allowed to be used in. Overrides <code>guild_only</code> if set.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.AppCommandContext" title="discord.app_commands.AppCommandContext"><code>AppCommandContext</code></a>]

</dd></dl></dd>
</dl><dl><dt>allowed_installs<a href="#discord.app_commands.ContextMenu.allowed_installs" title="Permalink to this definition">¶</a></dt>
<dd>

The installation contexts that the command is allowed to be installed on.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.AppInstallationType" title="discord.app_commands.AppInstallationType"><code>AppInstallationType</code></a>]

</dd></dl></dd>
</dl><dl><dt>nsfw<a href="#discord.app_commands.ContextMenu.nsfw" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the command is NSFW and should only work in NSFW channels. Defaults to <code>False</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>checks<a href="#discord.app_commands.ContextMenu.checks" title="Permalink to this definition">¶</a></dt>
<dd>

A list of predicates that take a <a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a> parameter to indicate whether the command callback should be executed. If an exception is necessary to be thrown to signal failure, then one inherited from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a> should be used. If all the checks fail without propagating an exception, <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a> is raised.

</dd></dl><dl><dt>extras<a href="#discord.app_commands.ContextMenu.extras" title="Permalink to this definition">¶</a></dt>
<dd>

A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

</dd></dl></dd>
</dl><dl><dt>@error(*coro*)<a href="#discord.app_commands.ContextMenu.error" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a local error handler.

The local error handler is called whenever an exception is raised in the body of the command or during handling of the command. The error handler must take 2 parameters, the interaction and the error.

The error passed will be derived from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the local error handler.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>*property*callback<a href="#discord.app_commands.ContextMenu.callback" title="Permalink to this definition">¶</a></dt>
<dd>

The coroutine that is executed when the context menu is called.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>

</dd></dl></dd>
</dl><dl><dt>*property*qualified_name<a href="#discord.app_commands.ContextMenu.qualified_name" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the fully qualified command name.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>add_check(*func*, */*)<a href="#discord.app_commands.ContextMenu.add_check" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a check to the command.

This is the non-decorator interface to <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a>.

<dl><dt>Parameters</dt>
<dd>

**func** – The function that will be used as a check.

</dd></dl></dd>
</dl><dl><dt>remove_check(*func*, */*)<a href="#discord.app_commands.ContextMenu.remove_check" title="Permalink to this definition">¶</a></dt>
<dd>

Removes a check from the command.

This function is idempotent and will not raise an exception if the function is not in the command’s checks.

<dl><dt>Parameters</dt>
<dd>

**func** – The function to remove from the checks.

</dd></dl></dd>
</dl></dd>
</dl>

#### Group ¶

Attributes

- [allowed\_contexts](#discord.app_commands.Group.allowed_contexts)
- [allowed\_installs](#discord.app_commands.Group.allowed_installs)
- [commands](#discord.app_commands.Group.commands)
- [default\_permissions](#discord.app_commands.Group.default_permissions)
- [description](#discord.app_commands.Group.description)
- [extras](#discord.app_commands.Group.extras)
- [guild\_only](#discord.app_commands.Group.guild_only)
- [name](#discord.app_commands.Group.name)
- [nsfw](#discord.app_commands.Group.nsfw)
- [parent](#discord.app_commands.Group.parent)
- [qualified\_name](#discord.app_commands.Group.qualified_name)
- [root\_parent](#discord.app_commands.Group.root_parent)

Methods

- def [add\_command](#discord.app_commands.Group.add_command)
- @ [command](#discord.app_commands.Group.command)
- @ [error](#discord.app_commands.Group.error)
- def [get\_command](#discord.app_commands.Group.get_command)
- async [interaction\_check](#discord.app_commands.Group.interaction_check)
- async [on\_error](#discord.app_commands.Group.on_error)
- def [remove\_command](#discord.app_commands.Group.remove_command)
- def [walk\_commands](#discord.app_commands.Group.walk_commands)

<dl><dt>*class*discord.app_commands.Group(***, *name=...*, *description=...*, *parent=None*, *guild_ids=None*, *guild_only=...*, *allowed_contexts=...*, *allowed_installs=...*, *nsfw=...*, *auto_locale_strings=True*, *default_permissions=...*, *extras=...*)<a href="#discord.app_commands.Group" title="Permalink to this definition">¶</a></dt>
<dd>

A class that implements an application command group.

These are usually inherited rather than created manually.

Decorators such as <a href="#discord.app_commands.guild_only" title="discord.app_commands.guild_only"><code>guild_only()</code></a>, <a href="#discord.app_commands.guilds" title="discord.app_commands.guilds"><code>guilds()</code></a>, and <a href="#discord.app_commands.default_permissions" title="discord.app_commands.default_permissions"><code>default_permissions()</code></a> will apply to the group if used on top of a subclass. For example:

```
from discord import app_commands

@app_commands.guild_only()
class MyGroup(app_commands.Group):
    pass

```

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **name** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The name of the group. If not given, it defaults to a lower-case kebab-case version of the class name.
- **description** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The description of the group. This shows up in the UI to describe the group. If not given, it defaults to the docstring of the class shortened to 100 characters.
- **auto\_locale\_strings** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If this is set to <code>True</code>, then all translatable strings will implicitly be wrapped into <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> rather than <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>. This could avoid some repetition and be more ergonomic for certain defaults such as default command names, command descriptions, and parameter names. Defaults to <code>True</code>.
- **default\_permissions** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>]) –

  The default permissions that can execute this group on Discord. Note that server administrators can override this value in the client. Setting an empty permissions field will disallow anyone except server administrators from using the command in a guild.

  Due to a Discord limitation, this does not work on subcommands.
- **guild\_only** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the group should only be usable in guild contexts. Defaults to <code>False</code>.

  Due to a Discord limitation, this does not work on subcommands.
- **nsfw** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the command is NSFW and should only work in NSFW channels. Defaults to <code>False</code>.

  Due to a Discord limitation, this does not work on subcommands.
- **parent** (Optional\[<a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]) – The parent application command. <code>None</code> if there isn’t one.
- **extras** (<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>) – A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.

</dd></dl><dl><dt>name<a href="#discord.app_commands.Group.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the group.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.app_commands.Group.description" title="Permalink to this definition">¶</a></dt>
<dd>

The description of the group. This shows up in the UI to describe the group.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>default_permissions<a href="#discord.app_commands.Group.default_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The default permissions that can execute this group on Discord. Note that server administrators can override this value in the client. Setting an empty permissions field will disallow anyone except server administrators from using the command in a guild.

Due to a Discord limitation, this does not work on subcommands.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>]

</dd></dl></dd>
</dl><dl><dt>guild_only<a href="#discord.app_commands.Group.guild_only" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the group should only be usable in guild contexts.

Due to a Discord limitation, this does not work on subcommands.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>allowed_contexts<a href="#discord.app_commands.Group.allowed_contexts" title="Permalink to this definition">¶</a></dt>
<dd>

The contexts that this group is allowed to be used in. Overrides guild\_only if set.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.AppCommandContext" title="discord.app_commands.AppCommandContext"><code>AppCommandContext</code></a>]

</dd></dl></dd>
</dl><dl><dt>allowed_installs<a href="#discord.app_commands.Group.allowed_installs" title="Permalink to this definition">¶</a></dt>
<dd>

The installation contexts that the command is allowed to be installed on.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.AppInstallationType" title="discord.app_commands.AppInstallationType"><code>AppInstallationType</code></a>]

</dd></dl></dd>
</dl><dl><dt>nsfw<a href="#discord.app_commands.Group.nsfw" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the command is NSFW and should only work in NSFW channels.

Due to a Discord limitation, this does not work on subcommands.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>parent<a href="#discord.app_commands.Group.parent" title="Permalink to this definition">¶</a></dt>
<dd>

The parent group. <code>None</code> if there isn’t one.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>extras<a href="#discord.app_commands.Group.extras" title="Permalink to this definition">¶</a></dt>
<dd>

A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

</dd></dl></dd>
</dl><dl><dt>@command(***, *name=...*, *description=...*, *nsfw=False*, *auto_locale_strings=True*, *extras=...*)<a href="#discord.app_commands.Group.command" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that creates an application command from a regular function under this group.

<dl><dt>Parameters</dt>
<dd>

- **name** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The name of the application command. If not given, it defaults to a lower-case version of the callback name.
- **description** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The description of the application command. This shows up in the UI to describe the application command. If not given, it defaults to the first line of the docstring of the callback shortened to 100 characters.
- **nsfw** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the command is NSFW and should only work in NSFW channels. Defaults to <code>False</code>.
- **auto\_locale\_strings** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If this is set to <code>True</code>, then all translatable strings will implicitly be wrapped into <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> rather than <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>. This could avoid some repetition and be more ergonomic for certain defaults such as default command names, command descriptions, and parameter names. Defaults to <code>True</code>.
- **extras** (<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>) – A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.

</dd></dl></dd>
</dl><dl><dt>@error(*coro*)<a href="#discord.app_commands.Group.error" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a local error handler.

The local error handler is called whenever an exception is raised in a child command. The error handler must take 2 parameters, the interaction and the error.

The error passed will be derived from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the local error handler.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine, or is an invalid coroutine.

</dd></dl></dd>
</dl><dl><dt>*property*root_parent<a href="#discord.app_commands.Group.root_parent" title="Permalink to this definition">¶</a></dt>
<dd>

The parent of this group.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*qualified_name<a href="#discord.app_commands.Group.qualified_name" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the fully qualified group name.

The qualified name includes the parent name as well. For example, in a group like <code>/foo bar</code> the qualified name is <code>foo bar</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*commands<a href="#discord.app_commands.Group.commands" title="Permalink to this definition">¶</a></dt>
<dd>

The commands that this group contains.

<dl><dt>Type</dt>
<dd>

List\[Union\[<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*for ... in* walk_commands()<a href="#discord.app_commands.Group.walk_commands" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all commands that this group contains.

<dl><dt>Yields</dt>
<dd>

Union\[<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>] – The commands in this group.

</dd></dl></dd>
</dl><dl><dt>*await* on_error(*interaction*, *error*, */*)<a href="#discord.app_commands.Group.on_error" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when a child’s command raises an <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

To get the command that failed, <a href="#discord.Interaction.command" title="discord.Interaction.command"><code>discord.Interaction.command</code></a> should be used.

The default implementation does nothing.

<dl><dt>Parameters</dt>
<dd>

- **interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that is being handled.
- **error** (<a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>) – The exception that was raised.

</dd></dl></dd>
</dl><dl><dt>*await* interaction_check(*interaction*, */*)<a href="#discord.app_commands.Group.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A callback that is called when an interaction happens within the group that checks whether a command inside the group should be executed.

This is useful to override if, for example, you want to ensure that the interaction author is a given user.

The default implementation of this returns <code>True</code>.

Note

If an exception occurs within the body then the check is considered a failure and error handlers such as <a href="#discord.app_commands.Group.on_error" title="discord.app_commands.Group.on_error"><code>on_error()</code></a> is called. See <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a> for more information.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that occurred.

</dd><dt>Returns</dt>
<dd>

Whether the view children’s callbacks should be called.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>add_command(*command*, */*, ***, *override=False*)<a href="#discord.app_commands.Group.add_command" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a command or group to this group’s internal list of commands.

<dl><dt>Parameters</dt>
<dd>

- **command** (Union\[<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]) – The command or group to add.
- **override** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to override a pre-existing command or group with the same name. If <code>False</code> then an exception is raised.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.app_commands.CommandAlreadyRegistered" title="discord.app_commands.CommandAlreadyRegistered">**CommandAlreadyRegistered**</a> – The command or group is already registered. Note that the <a href="#discord.app_commands.CommandAlreadyRegistered.guild_id" title="discord.app_commands.CommandAlreadyRegistered.guild_id"><code>CommandAlreadyRegistered.guild_id</code></a> attribute will always be <code>None</code> in this case.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – There are too many commands already registered or the group is too deeply nested.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The wrong command type was passed.

</dd></dl></dd>
</dl><dl><dt>remove_command(*name*, */*)<a href="#discord.app_commands.Group.remove_command" title="Permalink to this definition">¶</a></dt>
<dd>

Removes a command or group from the internal list of commands.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the command or group to remove.

</dd><dt>Returns</dt>
<dd>

The command that was removed. If nothing was removed then <code>None</code> is returned instead.

</dd><dt>Return type</dt>
<dd>

Optional\[Union\[<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]]

</dd></dl></dd>
</dl><dl><dt>get_command(*name*, */*)<a href="#discord.app_commands.Group.get_command" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves a command or group from its name.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the command or group to retrieve.

</dd><dt>Returns</dt>
<dd>

The command or group that was retrieved. If nothing was found then <code>None</code> is returned instead.

</dd><dt>Return type</dt>
<dd>

Optional\[Union\[<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl>

### Decorators ¶

<dl><dt>@discord.app_commands.command(***, *name=...*, *description=...*, *nsfw=False*, *auto_locale_strings=True*, *extras=...*)<a href="#discord.app_commands.command" title="Permalink to this definition">¶</a></dt>
<dd>

Creates an application command from a regular function.

<dl><dt>Parameters</dt>
<dd>

- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the application command. If not given, it defaults to a lower-case version of the callback name.
- **description** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The description of the application command. This shows up in the UI to describe the application command. If not given, it defaults to the first line of the docstring of the callback shortened to 100 characters.
- **nsfw** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the command is NSFW and should only work in NSFW channels. Defaults to <code>False</code>.

  Due to a Discord limitation, this does not work on subcommands.
- **auto\_locale\_strings** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If this is set to <code>True</code>, then all translatable strings will implicitly be wrapped into <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> rather than <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>. This could avoid some repetition and be more ergonomic for certain defaults such as default command names, command descriptions, and parameter names. Defaults to <code>True</code>.
- **extras** (<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>) – A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.

</dd></dl></dd>
</dl><dl><dt>@discord.app_commands.context_menu(***, *name=...*, *nsfw=False*, *auto_locale_strings=True*, *extras=...*)<a href="#discord.app_commands.context_menu" title="Permalink to this definition">¶</a></dt>
<dd>

Creates an application command context menu from a regular function.

This function must have a signature of <a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a> as its first parameter and taking either a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a>, or <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>, or a <a href="https://docs.python.org/3/library/typing.html#typing.Union" title="(in Python v3.14)"><code>typing.Union</code></a> of <code>Member</code> and <code>User</code> as its second parameter.

Examples

```
@app_commands.context_menu()
async def react(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message('Very cool message!', ephemeral=True)

@app_commands.context_menu()
async def ban(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.send_message(f'Should I actually ban {user}...', ephemeral=True)

```

<dl><dt>Parameters</dt>
<dd>

- **name** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The name of the context menu command. If not given, it defaults to a title-case version of the callback name. Note that unlike regular slash commands this can have spaces and upper case characters in the name.
- **nsfw** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the command is NSFW and should only work in NSFW channels. Defaults to <code>False</code>.

  Due to a Discord limitation, this does not work on subcommands.
- **auto\_locale\_strings** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If this is set to <code>True</code>, then all translatable strings will implicitly be wrapped into <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> rather than <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>. This could avoid some repetition and be more ergonomic for certain defaults such as default command names, command descriptions, and parameter names. Defaults to <code>True</code>.
- **extras** (<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>) – A dictionary that can be used to store extraneous data. The library will not touch any values or keys within this dictionary.

</dd></dl></dd>
</dl><dl><dt>@discord.app_commands.describe(***parameters*)<a href="#discord.app_commands.describe" title="Permalink to this definition">¶</a></dt>
<dd>

Describes the given parameters by their name using the key of the keyword argument as the name.

Example:

```
@app_commands.command(description='Bans a member')
@app_commands.describe(member='the member to ban')
async def ban(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f'Banned {member}')

```

Alternatively, you can describe parameters using Google, Sphinx, or Numpy style docstrings.

Example:

```
@app_commands.command()
async def ban(interaction: discord.Interaction, member: discord.Member):
"""Bans a member

    Parameters
    -----------
    member: discord.Member
        the member to ban
    """
    await interaction.response.send_message(f'Banned {member}')

```

<dl><dt>Parameters</dt>
<dd>

**\*\*parameters** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The description of the parameters.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The parameter name is not found.

</dd></dl></dd>
</dl><dl><dt>@discord.app_commands.rename(***parameters*)<a href="#discord.app_commands.rename" title="Permalink to this definition">¶</a></dt>
<dd>

Renames the given parameters by their name using the key of the keyword argument as the name.

This renames the parameter within the Discord UI. When referring to the parameter in other decorators, the parameter name used in the function is used instead of the renamed one.

Example:

```
@app_commands.command()
@app_commands.rename(the_member_to_ban='member')
async def ban(interaction: discord.Interaction, the_member_to_ban: discord.Member):
    await interaction.response.send_message(f'Banned {the_member_to_ban}')

```

<dl><dt>Parameters</dt>
<dd>

**\*\*parameters** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The name of the parameters.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The parameter name is already used by another parameter.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The parameter name is not found.

</dd></dl></dd>
</dl><dl><dt>@discord.app_commands.choices(***parameters*)<a href="#discord.app_commands.choices" title="Permalink to this definition">¶</a></dt>
<dd>

Instructs the given parameters by their name to use the given choices for their choices.

Example:

```
@app_commands.command()
@app_commands.describe(fruits='fruits to choose from')
@app_commands.choices(fruits=[
    Choice(name='apple', value=1),
    Choice(name='banana', value=2),
    Choice(name='cherry', value=3),
])
async def fruit(interaction: discord.Interaction, fruits: Choice[int]):
    await interaction.response.send_message(f'Your favourite fruit is {fruits.name}.')

```

Note

This is not the only way to provide choices to a command. There are two more ergonomic ways of doing this. The first one is to use a <a href="https://docs.python.org/3/library/typing.html#typing.Literal" title="(in Python v3.14)"><code>typing.Literal</code></a> annotation:

```
@app_commands.command()
@app_commands.describe(fruits='fruits to choose from')
async def fruit(interaction: discord.Interaction, fruits: Literal['apple', 'banana', 'cherry']):
    await interaction.response.send_message(f'Your favourite fruit is {fruits}.')

```

The second way is to use an <a href="https://docs.python.org/3/library/enum.html#enum.Enum" title="(in Python v3.14)"><code>enum.Enum</code></a>:

```
class Fruits(enum.Enum):
    apple = 1
    banana = 2
    cherry = 3

@app_commands.command()
@app_commands.describe(fruits='fruits to choose from')
async def fruit(interaction: discord.Interaction, fruits: Fruits):
    await interaction.response.send_message(f'Your favourite fruit is {fruits}.')

```

<dl><dt>Parameters</dt>
<dd>

**\*\*parameters** – The choices of the parameters.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The parameter name is not found or the parameter type was incorrect.

</dd></dl></dd>
</dl><dl><dt>@discord.app_commands.autocomplete(***parameters*)<a href="#discord.app_commands.autocomplete" title="Permalink to this definition">¶</a></dt>
<dd>

Associates the given parameters with the given autocomplete callback.

Autocomplete is only supported on types that have <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, or <a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a> values.

<a href="#discord.app_commands.check" title="discord.app_commands.check"><code>Checks</code></a> are supported, however they must be attached to the autocomplete callback in order to work. Checks attached to the command are ignored when invoking the autocomplete callback.

For more information, see the <a href="#discord.app_commands.Command.autocomplete" title="discord.app_commands.Command.autocomplete"><code>Command.autocomplete()</code></a> documentation.

Warning

The choices returned from this coroutine are suggestions. The user may ignore them and input their own value.

Example:

```
async def fruit_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    fruits = ['Banana', 'Pineapple', 'Apple', 'Watermelon', 'Melon', 'Cherry']
    return [
        app_commands.Choice(name=fruit, value=fruit)
        for fruit in fruits if current.lower() in fruit.lower()
    ]

@app_commands.command()
@app_commands.autocomplete(fruit=fruit_autocomplete)
async def fruits(interaction: discord.Interaction, fruit: str):
    await interaction.response.send_message(f'Your favourite fruit seems to be {fruit}')

```

<dl><dt>Parameters</dt>
<dd>

**\*\*parameters** – The parameters to mark as autocomplete.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The parameter name is not found or the parameter type was incorrect.

</dd></dl></dd>
</dl><dl><dt>@discord.app_commands.guilds(**guild_ids*)<a href="#discord.app_commands.guilds" title="Permalink to this definition">¶</a></dt>
<dd>

Associates the given guilds with the command.

When the command instance is added to a <a href="#discord.app_commands.CommandTree" title="discord.app_commands.CommandTree"><code>CommandTree</code></a>, the guilds that are specified by this decorator become the default guilds that it’s added to rather than being a global command.

If no arguments are given, then the command will not be synced anywhere. This may be modified later using the <a href="#discord.app_commands.CommandTree.add_command" title="discord.app_commands.CommandTree.add_command"><code>CommandTree.add_command()</code></a> method.

Note

Due to an implementation quirk and Python limitation, if this is used in conjunction with the <a href="#discord.app_commands.CommandTree.command" title="discord.app_commands.CommandTree.command"><code>CommandTree.command()</code></a> or <a href="#discord.app_commands.CommandTree.context_menu" title="discord.app_commands.CommandTree.context_menu"><code>CommandTree.context_menu()</code></a> decorator then this must go below that decorator.

Note

Due to a Discord limitation, this decorator cannot be used in conjunction with contexts (e.g. <a href="#discord.app_commands.allowed_contexts" title="discord.app_commands.allowed_contexts"><code>app_commands.allowed_contexts()</code></a>) or installation types (e.g. <a href="#discord.app_commands.allowed_installs" title="discord.app_commands.allowed_installs"><code>app_commands.allowed_installs()</code></a>).

Example:

```
MY_GUILD_ID = discord.Object(...)  # Guild ID here

@app_commands.command()
@app_commands.guilds(MY_GUILD_ID)
async def bonk(interaction: discord.Interaction):
    await interaction.response.send_message('Bonk', ephemeral=True)

```

<dl><dt>Parameters</dt>
<dd>

**\*guild\_ids** (Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – The guilds to associate this command with. The command tree will use this as the default when added rather than adding it as a global command.

</dd></dl></dd>
</dl><dl><dt>@discord.app_commands.guild_only(*func=None*)<a href="#discord.app_commands.guild_only" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that indicates this command can only be used in a guild context.

This is **not** implemented as a <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a>, and is instead verified by Discord server side. Therefore, there is no error handler called when a command is used within a private message.

This decorator can be called with or without parentheses.

Due to a Discord limitation, this decorator does nothing in subcommands and is ignored.

Examples

```
@app_commands.command()
@app_commands.guild_only()
async def my_guild_only_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am only available in guilds!')

```

</dd></dl><dl><dt>@discord.app_commands.dm_only(*func=None*)<a href="#discord.app_commands.dm_only" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that indicates this command can only be used in the context of bot DMs.

This is **not** implemented as a <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a>, and is instead verified by Discord server side. Therefore, there is no error handler called when a command is used within a guild or group DM.

This decorator can be called with or without parentheses.

Due to a Discord limitation, this decorator does nothing in subcommands and is ignored.

Examples

```
@app_commands.command()
@app_commands.dm_only()
async def my_dm_only_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am only available in DMs!')

```

</dd></dl><dl><dt>@discord.app_commands.private_channel_only(*func=None*)<a href="#discord.app_commands.private_channel_only" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that indicates this command can only be used in the context of DMs and group DMs.

This is **not** implemented as a <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a>, and is instead verified by Discord server side. Therefore, there is no error handler called when a command is used within a guild.

This decorator can be called with or without parentheses.

Due to a Discord limitation, this decorator does nothing in subcommands and is ignored.

New in version 2.4.

Examples

```
@app_commands.command()
@app_commands.private_channel_only()
async def my_private_channel_only_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am only available in DMs and GDMs!')

```

</dd></dl><dl><dt>@discord.app_commands.allowed_contexts(*guilds=...*, *dms=...*, *private_channels=...*)<a href="#discord.app_commands.allowed_contexts" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that indicates this command can only be used in certain contexts. Valid contexts are guilds, DMs and private channels.

This is **not** implemented as a <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a>, and is instead verified by Discord server side.

Due to a Discord limitation, this decorator does nothing in subcommands and is ignored.

New in version 2.4.

Examples

```
@app_commands.command()
@app_commands.allowed_contexts(guilds=True, dms=False, private_channels=True)
async def my_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am only available in guilds and private channels!')

```

</dd></dl><dl><dt>@discord.app_commands.user_install(*func=None*)<a href="#discord.app_commands.user_install" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that indicates this command should be installed for users.

This is **not** implemented as a <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a>, and is instead verified by Discord server side.

Due to a Discord limitation, this decorator does nothing in subcommands and is ignored.

New in version 2.4.

Examples

```
@app_commands.command()
@app_commands.user_install()
async def my_user_install_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in users by default!')

```

</dd></dl><dl><dt>@discord.app_commands.guild_install(*func=None*)<a href="#discord.app_commands.guild_install" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that indicates this command should be installed in guilds.

This is **not** implemented as a <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a>, and is instead verified by Discord server side.

Due to a Discord limitation, this decorator does nothing in subcommands and is ignored.

New in version 2.4.

Examples

```
@app_commands.command()
@app_commands.guild_install()
async def my_guild_install_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in guilds by default!')

```

</dd></dl><dl><dt>@discord.app_commands.allowed_installs(*guilds=...*, *users=...*)<a href="#discord.app_commands.allowed_installs" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that indicates this command should be installed in certain contexts. Valid contexts are guilds and users.

This is **not** implemented as a <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a>, and is instead verified by Discord server side.

Due to a Discord limitation, this decorator does nothing in subcommands and is ignored.

New in version 2.4.

Examples

```
@app_commands.command()
@app_commands.allowed_installs(guilds=False, users=True)
async def my_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('I am installed in users by default!')

```

</dd></dl><dl><dt>@discord.app_commands.default_permissions(*perms_obj=None*, */*, ***perms*)<a href="#discord.app_commands.default_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that sets the default permissions needed to execute this command.

When this decorator is used, by default users must have these permissions to execute the command. However, an administrator can change the permissions needed to execute this command using the official client. Therefore, this only serves as a hint.

Setting an empty permissions field, including via calling this with no arguments, will disallow anyone except server administrators from using the command in a guild.

This is sent to Discord server side, and is not a <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a>. Therefore, error handlers are not called.

Due to a Discord limitation, this decorator does nothing in subcommands and is ignored.

Warning

This serves as a *hint* and members are *not* required to have the permissions given to actually execute this command. If you want to ensure that members have the permissions needed, consider using <a href="#discord.app_commands.checks.has_permissions" title="discord.app_commands.checks.has_permissions"><code>has_permissions()</code></a> instead.

<dl><dt>Parameters</dt>
<dd>

- **\*\*perms** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Keyword arguments denoting the permissions to set as the default.
- **perms\_obj** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>) –

  A permissions object as positional argument. This can be used in combination with <code>**perms</code>.

  New in version 2.5.

</dd></dl>

Examples

```
@app_commands.command()
@app_commands.default_permissions(manage_messages=True)
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('You may or may not have manage messages.')

```

```
ADMIN_PERMS = discord.Permissions(administrator=True)

@app_commands.command()
@app_commands.default_permissions(ADMIN_PERMS, manage_messages=True)
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('You may or may not have manage messages.')

```

</dd></dl>

### Checks ¶

<dl><dt>@discord.app_commands.check(*predicate*)<a href="#discord.app_commands.check" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that adds a check to an application command.

These checks should be predicates that take in a single parameter taking a <a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>. If the check returns a <code>False</code>-like value then during invocation a <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a> exception is raised and sent to the appropriate error handlers.

These checks can be either a coroutine or not.

Examples

Creating a basic check to see if the command invoker is you.

```
def check_if_it_is_me(interaction: discord.Interaction) -> bool:
    return interaction.user.id == 85309593344815104

@tree.command()
@app_commands.check(check_if_it_is_me)
async def only_for_me(interaction: discord.Interaction):
    await interaction.response.send_message('I know you!', ephemeral=True)

```

Transforming common checks into its own decorator:

```
def is_me():
    def predicate(interaction: discord.Interaction) -> bool:
        return interaction.user.id == 85309593344815104
    return app_commands.check(predicate)

@tree.command()
@is_me()
async def only_me(interaction: discord.Interaction):
    await interaction.response.send_message('Only you!')

```

<dl><dt>Parameters</dt>
<dd>

**predicate** (Callable\[\[<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>], <a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]) – The predicate to check if the command should be invoked.

</dd></dl></dd>
</dl><dl><dt>@discord.app_commands.checks.has_role(*item*, */*)<a href="#discord.app_commands.checks.has_role" title="Permalink to this definition">¶</a></dt>
<dd>

A <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a> that is added that checks if the member invoking the command has the role specified via the name or ID specified.

If a string is specified, you must give the exact name of the role, including caps and spelling.

If an integer is specified, you must give the exact snowflake ID of the role.

This check raises one of two special exceptions, <a href="#discord.app_commands.MissingRole" title="discord.app_commands.MissingRole"><code>MissingRole</code></a> if the user is missing a role, or <a href="#discord.app_commands.NoPrivateMessage" title="discord.app_commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> if it is used in a private message. Both inherit from <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 2.0.

Note

This is different from the permission system that Discord provides for application commands. This is done entirely locally in the program rather than being handled by Discord.

<dl><dt>Parameters</dt>
<dd>

**item** (Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The name or ID of the role to check.

</dd></dl></dd>
</dl><dl><dt>@discord.app_commands.checks.has_any_role(**items*)<a href="#discord.app_commands.checks.has_any_role" title="Permalink to this definition">¶</a></dt>
<dd>

A <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a> that is added that checks if the member invoking the command has **any** of the roles specified. This means that if they have one out of the three roles specified, then this check will return <code>True</code>.

Similar to <a href="#discord.app_commands.checks.has_role" title="discord.app_commands.checks.has_role"><code>has_role()</code></a>, the names or IDs passed in must be exact.

This check raises one of two special exceptions, <a href="#discord.app_commands.MissingAnyRole" title="discord.app_commands.MissingAnyRole"><code>MissingAnyRole</code></a> if the user is missing all roles, or <a href="#discord.app_commands.NoPrivateMessage" title="discord.app_commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> if it is used in a private message. Both inherit from <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 2.0.

Note

This is different from the permission system that Discord provides for application commands. This is done entirely locally in the program rather than being handled by Discord.

<dl><dt>Parameters</dt>
<dd>

**items** (List\[Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]]) – An argument list of names or IDs to check that the member has roles wise.

</dd></dl>

Example

```
@tree.command()
@app_commands.checks.has_any_role('Library Devs', 'Moderators', 492212595072434186)
async def cool(interaction: discord.Interaction):
    await interaction.response.send_message('You are cool indeed')

```

</dd></dl><dl><dt>@discord.app_commands.checks.has_permissions(***perms*)<a href="#discord.app_commands.checks.has_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

A <a href="#discord.app_commands.check" title="discord.app_commands.check"><code>check()</code></a> that is added that checks if the member has all of the permissions necessary.

Note that this check operates on the permissions given by <a href="#discord.Interaction.permissions" title="discord.Interaction.permissions"><code>discord.Interaction.permissions</code></a>.

The permissions passed in must be exactly like the properties shown under <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>discord.Permissions</code></a>.

This check raises a special exception, <a href="#discord.app_commands.MissingPermissions" title="discord.app_commands.MissingPermissions"><code>MissingPermissions</code></a> that is inherited from <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 2.0.

Note

This is different from the permission system that Discord provides for application commands. This is done entirely locally in the program rather than being handled by Discord.

<dl><dt>Parameters</dt>
<dd>

**\*\*perms** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Keyword arguments denoting the permissions to check for.

</dd></dl>

Example

```
@tree.command()
@app_commands.checks.has_permissions(manage_messages=True)
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('You can manage messages.')

```

</dd></dl><dl><dt>@discord.app_commands.checks.bot_has_permissions(***perms*)<a href="#discord.app_commands.checks.bot_has_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

Similar to <a href="#discord.app_commands.checks.has_permissions" title="discord.app_commands.checks.has_permissions"><code>has_permissions()</code></a> except checks if the bot itself has the permissions listed. This relies on <a href="#discord.Interaction.app_permissions" title="discord.Interaction.app_permissions"><code>discord.Interaction.app_permissions</code></a>.

This check raises a special exception, <a href="#discord.app_commands.BotMissingPermissions" title="discord.app_commands.BotMissingPermissions"><code>BotMissingPermissions</code></a> that is inherited from <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 2.0.

</dd></dl><dl><dt>@discord.app_commands.checks.cooldown(*rate*, *per*, ***, *key=...*)<a href="#discord.app_commands.checks.cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that adds a cooldown to a command.

A cooldown allows a command to only be used a specific amount of times in a specific time frame. These cooldowns are based off of the <code>key</code> function provided. If a <code>key</code> is not provided then it defaults to a user-level cooldown. The <code>key</code> function must take a single parameter, the <a href="#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a> and return a value that is used as a key to the internal cooldown mapping.

The <code>key</code> function can optionally be a coroutine.

If a cooldown is triggered, then <a href="#discord.app_commands.CommandOnCooldown" title="discord.app_commands.CommandOnCooldown"><code>CommandOnCooldown</code></a> is raised to the error handlers.

Examples

Setting a one per 5 seconds per member cooldown on a command:

```
@tree.command()
@app_commands.checks.cooldown(1, 5.0, key=lambda i: (i.guild_id, i.user.id))
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('Hello')

@test.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(str(error), ephemeral=True)

```

<dl><dt>Parameters</dt>
<dd>

- **rate** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The number of times a command can be used before triggering a cooldown.
- **per** (<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>) – The amount of seconds to wait for a cooldown when it’s been triggered.
- **key** (Optional\[Callable\[\[<a href="#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a>], <a href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable" title="(in Python v3.14)"><code>collections.abc.Hashable</code></a>]]) – A function that returns a key to the mapping denoting the type of cooldown. Can optionally be a coroutine. If not given then defaults to a user-level cooldown. If <code>None</code> is passed then it is interpreted as a “global” cooldown.

</dd></dl></dd>
</dl><dl><dt>@discord.app_commands.checks.dynamic_cooldown(*factory*, ***, *key=...*)<a href="#discord.app_commands.checks.dynamic_cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that adds a dynamic cooldown to a command.

A cooldown allows a command to only be used a specific amount of times in a specific time frame. These cooldowns are based off of the <code>key</code> function provided. If a <code>key</code> is not provided then it defaults to a user-level cooldown. The <code>key</code> function must take a single parameter, the <a href="#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a> and return a value that is used as a key to the internal cooldown mapping.

If a <code>factory</code> function is given, it must be a function that accepts a single parameter of type <a href="#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a> and must return a <a href="#discord.app_commands.Cooldown" title="discord.app_commands.Cooldown"><code>Cooldown</code></a> or <code>None</code>. If <code>None</code> is returned then that cooldown is effectively bypassed.

Both <code>key</code> and <code>factory</code> can optionally be coroutines.

If a cooldown is triggered, then <a href="#discord.app_commands.CommandOnCooldown" title="discord.app_commands.CommandOnCooldown"><code>CommandOnCooldown</code></a> is raised to the error handlers.

Examples

Setting a cooldown for everyone but the owner.

```
def cooldown_for_everyone_but_me(interaction: discord.Interaction) -> Optional[app_commands.Cooldown]:
    if interaction.user.id == 80088516616269824:
        return None
    return app_commands.Cooldown(1, 10.0)

@tree.command()
@app_commands.checks.dynamic_cooldown(cooldown_for_everyone_but_me)
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('Hello')

@test.error
async def on_test_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(str(error), ephemeral=True)

```

<dl><dt>Parameters</dt>
<dd>

- **factory** (Optional\[Callable\[\[<a href="#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a>], Optional\[<a href="#discord.app_commands.Cooldown" title="discord.app_commands.Cooldown"><code>Cooldown</code></a>]]]) – A function that takes an interaction and returns a cooldown that will apply to that interaction or <code>None</code> if the interaction should not have a cooldown.
- **key** (Optional\[Callable\[\[<a href="#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a>], <a href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable" title="(in Python v3.14)"><code>collections.abc.Hashable</code></a>]]) – A function that returns a key to the mapping denoting the type of cooldown. Can optionally be a coroutine. If not given then defaults to a user-level cooldown. If <code>None</code> is passed then it is interpreted as a “global” cooldown.

</dd></dl></dd>
</dl>

### Cooldown ¶

Attributes

- [per](#discord.app_commands.Cooldown.per)
- [rate](#discord.app_commands.Cooldown.rate)

Methods

- def [copy](#discord.app_commands.Cooldown.copy)
- def [get\_retry\_after](#discord.app_commands.Cooldown.get_retry_after)
- def [get\_tokens](#discord.app_commands.Cooldown.get_tokens)
- def [reset](#discord.app_commands.Cooldown.reset)
- def [update\_rate\_limit](#discord.app_commands.Cooldown.update_rate_limit)

<dl><dt>*class*discord.app_commands.Cooldown(*rate*, *per*)<a href="#discord.app_commands.Cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a cooldown for a command.

New in version 2.0.

<dl><dt>rate<a href="#discord.app_commands.Cooldown.rate" title="Permalink to this definition">¶</a></dt>
<dd>

The total number of tokens available per <a href="#discord.app_commands.Cooldown.per" title="discord.app_commands.Cooldown.per"><code>per</code></a> seconds.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>

</dd></dl></dd>
</dl><dl><dt>per<a href="#discord.app_commands.Cooldown.per" title="Permalink to this definition">¶</a></dt>
<dd>

The length of the cooldown period in seconds.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>

</dd></dl></dd>
</dl><dl><dt>get_tokens(*current=None*)<a href="#discord.app_commands.Cooldown.get_tokens" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the number of available tokens before rate limiting is applied.

<dl><dt>Parameters</dt>
<dd>

**current** (Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – The time in seconds since Unix epoch to calculate tokens at. If not supplied then <a href="https://docs.python.org/3/library/time.html#time.time" title="(in Python v3.14)"><code>time.time()</code></a> is used.

</dd><dt>Returns</dt>
<dd>

The number of tokens available before the cooldown is to be applied.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>get_retry_after(*current=None*)<a href="#discord.app_commands.Cooldown.get_retry_after" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the time in seconds until the cooldown will be reset.

<dl><dt>Parameters</dt>
<dd>

**current** (Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – The current time in seconds since Unix epoch. If not supplied, then <a href="https://docs.python.org/3/library/time.html#time.time" title="(in Python v3.14)"><code>time.time()</code></a> is used.

</dd><dt>Returns</dt>
<dd>

The number of seconds to wait before this cooldown will be reset.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>

</dd></dl></dd>
</dl><dl><dt>update_rate_limit(*current=None*, ***, *tokens=1*)<a href="#discord.app_commands.Cooldown.update_rate_limit" title="Permalink to this definition">¶</a></dt>
<dd>

Updates the cooldown rate limit.

<dl><dt>Parameters</dt>
<dd>

- **current** (Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – The time in seconds since Unix epoch to update the rate limit at. If not supplied, then <a href="https://docs.python.org/3/library/time.html#time.time" title="(in Python v3.14)"><code>time.time()</code></a> is used.
- **tokens** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The amount of tokens to deduct from the rate limit.

</dd><dt>Returns</dt>
<dd>

The retry-after time in seconds if rate limited.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]

</dd></dl></dd>
</dl><dl><dt>reset()<a href="#discord.app_commands.Cooldown.reset" title="Permalink to this definition">¶</a></dt>
<dd>

Reset the cooldown to its initial state.

</dd></dl><dl><dt>copy()<a href="#discord.app_commands.Cooldown.copy" title="Permalink to this definition">¶</a></dt>
<dd>

Creates a copy of this cooldown.

<dl><dt>Returns</dt>
<dd>

A new instance of this cooldown.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.app_commands.Cooldown" title="discord.app_commands.Cooldown"><code>Cooldown</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### Namespace ¶

<dl><dt>*class*discord.app_commands.Namespace<a href="#discord.app_commands.Namespace" title="Permalink to this definition">¶</a></dt>
<dd>

An object that holds the parameters being passed to a command in a mostly raw state.

This class is deliberately simple and just holds the option name and resolved value as a simple key-pair mapping. These attributes can be accessed using dot notation. For example, an option with the name of <code>example</code> can be accessed using <code>ns.example</code>. If an attribute is not found, then <code>None</code> is returned rather than an attribute error.

Warning

The key names come from the raw Discord data, which means that if a parameter was renamed then the renamed key is used instead of the function parameter name.

New in version 2.0.

<dl><dt>x == y</dt>
<dd>

Checks if two namespaces are equal by checking if all attributes are equal.

</dd></dl><dl><dt>x != y</dt>
<dd>

Checks if two namespaces are not equal.

</dd></dl><dl><dt>x[key]</dt>
<dd>

Returns an attribute if it is found, otherwise raises a <a href="https://docs.python.org/3/library/exceptions.html#KeyError" title="(in Python v3.14)"><code>KeyError</code></a>.

</dd></dl><dl><dt>key in x</dt>
<dd>

Checks if the attribute is in the namespace.

</dd></dl><dl><dt>iter(x)</dt>
<dd>

Returns an iterator of <code>(name, value)</code> pairs. This allows it to be, for example, constructed as a dict or a list of pairs.

</dd></dl>

This namespace object converts resolved objects into their appropriate form depending on their type. Consult the table below for conversion information.

| Option Type | Resolved Type |
| --- | --- |
| <a href="#discord.AppCommandOptionType.string" title="discord.AppCommandOptionType.string"><code>AppCommandOptionType.string</code></a> | <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a> |
| <a href="#discord.AppCommandOptionType.integer" title="discord.AppCommandOptionType.integer"><code>AppCommandOptionType.integer</code></a> | <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a> |
| <a href="#discord.AppCommandOptionType.boolean" title="discord.AppCommandOptionType.boolean"><code>AppCommandOptionType.boolean</code></a> | <a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a> |
| <a href="#discord.AppCommandOptionType.number" title="discord.AppCommandOptionType.number"><code>AppCommandOptionType.number</code></a> | <a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a> |
| <a href="#discord.AppCommandOptionType.user" title="discord.AppCommandOptionType.user"><code>AppCommandOptionType.user</code></a> | <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a> or <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a> |
| <a href="#discord.AppCommandOptionType.channel" title="discord.AppCommandOptionType.channel"><code>AppCommandOptionType.channel</code></a> | <a href="#discord.app_commands.AppCommandChannel" title="discord.app_commands.AppCommandChannel"><code>AppCommandChannel</code></a> or <a href="#discord.app_commands.AppCommandThread" title="discord.app_commands.AppCommandThread"><code>AppCommandThread</code></a> |
| <a href="#discord.AppCommandOptionType.role" title="discord.AppCommandOptionType.role"><code>AppCommandOptionType.role</code></a> | <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Role" title="discord.Role"><code>Role</code></a> |
| <a href="#discord.AppCommandOptionType.mentionable" title="discord.AppCommandOptionType.mentionable"><code>AppCommandOptionType.mentionable</code></a> | <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a> or <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a>, or <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Role" title="discord.Role"><code>Role</code></a> |
| <a href="#discord.AppCommandOptionType.attachment" title="discord.AppCommandOptionType.attachment"><code>AppCommandOptionType.attachment</code></a> | <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Attachment" title="discord.Attachment"><code>Attachment</code></a> |

Note

In autocomplete interactions, the namespace might not be validated or filled in. Discord does not send the resolved data as well, so this means that certain fields end up just as IDs rather than the resolved data. In these cases, a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Object" title="discord.Object"><code>discord.Object</code></a> is returned instead.

This is a Discord limitation.

</dd></dl>

### Transformers ¶

#### Transformer ¶

Attributes

- [channel\_types](#discord.app_commands.Transformer.channel_types)
- [choices](#discord.app_commands.Transformer.choices)
- [max\_value](#discord.app_commands.Transformer.max_value)
- [min\_value](#discord.app_commands.Transformer.min_value)
- [type](#discord.app_commands.Transformer.type)

Methods

- async [autocomplete](#discord.app_commands.Transformer.autocomplete)
- async [transform](#discord.app_commands.Transformer.transform)

<dl><dt>*class*discord.app_commands.Transformer(**args*, ***kwds*)<a href="#discord.app_commands.Transformer" title="Permalink to this definition">¶</a></dt>
<dd>

The base class that allows a type annotation in an application command parameter to map into a <a href="#discord.AppCommandOptionType" title="discord.AppCommandOptionType"><code>AppCommandOptionType</code></a> and transform the raw value into one from this type.

This class is customisable through the overriding of methods and properties in the class and by using it as the second type parameter of the <a href="#discord.app_commands.Transform" title="discord.app_commands.Transform"><code>Transform</code></a> class. For example, to convert a string into a custom pair type:

```
class Point(typing.NamedTuple):
    x: int
    y: int

class PointTransformer(app_commands.Transformer):
    async def transform(self, interaction: discord.Interaction, value: str) -> Point:
        (x, _, y) = value.partition(',')
        return Point(x=int(x.strip()), y=int(y.strip()))

@app_commands.command()
async def graph(
    interaction: discord.Interaction,
    point: app_commands.Transform[Point, PointTransformer],
):
    await interaction.response.send_message(str(point))

```

If a class is passed instead of an instance to the second type parameter, then it is constructed with no arguments passed to the <code>__init__</code> method.

New in version 2.0.

<dl><dt>*property*type<a href="#discord.app_commands.Transformer.type" title="Permalink to this definition">¶</a></dt>
<dd>

The option type associated with this transformer.

This must be a <a href="https://docs.python.org/3/library/functions.html#property" title="(in Python v3.14)"><code>property</code></a>.

Defaults to <a href="#discord.AppCommandOptionType.string" title="discord.AppCommandOptionType.string"><code>string</code></a>.

<dl><dt>Type</dt>
<dd>

<a href="#discord.AppCommandOptionType" title="discord.AppCommandOptionType"><code>AppCommandOptionType</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*channel_types<a href="#discord.app_commands.Transformer.channel_types" title="Permalink to this definition">¶</a></dt>
<dd>

A list of channel types that are allowed to this parameter.

Only valid if the <a href="#discord.app_commands.Transformer.type" title="discord.app_commands.Transformer.type"><code>type()</code></a> returns <a href="#discord.AppCommandOptionType.channel" title="discord.AppCommandOptionType.channel"><code>channel</code></a>.

This must be a <a href="https://docs.python.org/3/library/functions.html#property" title="(in Python v3.14)"><code>property</code></a>.

Defaults to an empty list.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelType" title="discord.ChannelType"><code>ChannelType</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*min_value<a href="#discord.app_commands.Transformer.min_value" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum supported value for this parameter.

Only valid if the <a href="#discord.app_commands.Transformer.type" title="discord.app_commands.Transformer.type"><code>type()</code></a> returns <a href="#discord.AppCommandOptionType.number" title="discord.AppCommandOptionType.number"><code>number</code></a> <a href="#discord.AppCommandOptionType.integer" title="discord.AppCommandOptionType.integer"><code>integer</code></a>, or <a href="#discord.AppCommandOptionType.string" title="discord.AppCommandOptionType.string"><code>string</code></a>.

This must be a <a href="https://docs.python.org/3/library/functions.html#property" title="(in Python v3.14)"><code>property</code></a>.

Defaults to <code>None</code>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*max_value<a href="#discord.app_commands.Transformer.max_value" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum supported value for this parameter.

Only valid if the <a href="#discord.app_commands.Transformer.type" title="discord.app_commands.Transformer.type"><code>type()</code></a> returns <a href="#discord.AppCommandOptionType.number" title="discord.AppCommandOptionType.number"><code>number</code></a> <a href="#discord.AppCommandOptionType.integer" title="discord.AppCommandOptionType.integer"><code>integer</code></a>, or <a href="#discord.AppCommandOptionType.string" title="discord.AppCommandOptionType.string"><code>string</code></a>.

This must be a <a href="https://docs.python.org/3/library/functions.html#property" title="(in Python v3.14)"><code>property</code></a>.

Defaults to <code>None</code>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*choices<a href="#discord.app_commands.Transformer.choices" title="Permalink to this definition">¶</a></dt>
<dd>

A list of up to 25 choices that are allowed to this parameter.

Only valid if the <a href="#discord.app_commands.Transformer.type" title="discord.app_commands.Transformer.type"><code>type()</code></a> returns <a href="#discord.AppCommandOptionType.number" title="discord.AppCommandOptionType.number"><code>number</code></a> <a href="#discord.AppCommandOptionType.integer" title="discord.AppCommandOptionType.integer"><code>integer</code></a>, or <a href="#discord.AppCommandOptionType.string" title="discord.AppCommandOptionType.string"><code>string</code></a>.

This must be a <a href="https://docs.python.org/3/library/functions.html#property" title="(in Python v3.14)"><code>property</code></a>.

Defaults to <code>None</code>.

<dl><dt>Type</dt>
<dd>

Optional\[List\[<a href="#discord.app_commands.Choice" title="discord.app_commands.Choice"><code>Choice</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*await* transform(*interaction*, *value*, */*)<a href="#discord.app_commands.Transformer.transform" title="Permalink to this definition">¶</a></dt>
<dd>

This function *could be a* <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Transforms the converted option value into another value.

The value passed into this transform function is the same as the one in the <a href="#discord.app_commands.Namespace" title="discord.app_commands.Namespace"><code>conversion table</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction being handled.
- **value** (*Any*) – The value of the given argument after being resolved. See the <a href="#discord.app_commands.Namespace" title="discord.app_commands.Namespace"><code>conversion table</code></a> for how certain option types correspond to certain values.

</dd></dl></dd>
</dl><dl><dt>*await* autocomplete(*interaction*, *value*, */*)<a href="#discord.app_commands.Transformer.autocomplete" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

An autocomplete prompt handler to be automatically used by options using this transformer.

Note

Autocomplete is only supported for options with a <a href="#discord.app_commands.Transformer.type" title="discord.app_commands.Transformer.type"><code>type()</code></a> of <a href="#discord.AppCommandOptionType.string" title="discord.AppCommandOptionType.string"><code>string</code></a>, <a href="#discord.AppCommandOptionType.integer" title="discord.AppCommandOptionType.integer"><code>integer</code></a>, or <a href="#discord.AppCommandOptionType.number" title="discord.AppCommandOptionType.number"><code>number</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The autocomplete interaction being handled.
- **value** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – The current value entered by the user.

</dd><dt>Returns</dt>
<dd>

A list of choices to be displayed to the user, a maximum of 25.

</dd><dt>Return type</dt>
<dd>

List\[<a href="#discord.app_commands.Choice" title="discord.app_commands.Choice"><code>Choice</code></a>]

</dd></dl></dd>
</dl></dd>
</dl>

#### Transform ¶

<dl><dt>*class*discord.app_commands.Transform<a href="#discord.app_commands.Transform" title="Permalink to this definition">¶</a></dt>
<dd>

A type annotation that can be applied to a parameter to customise the behaviour of an option type by transforming with the given <a href="#discord.app_commands.Transformer" title="discord.app_commands.Transformer"><code>Transformer</code></a>. This requires the usage of two generic parameters, the first one is the type you’re converting to and the second one is the type of the <a href="#discord.app_commands.Transformer" title="discord.app_commands.Transformer"><code>Transformer</code></a> actually doing the transformation.

During type checking time this is equivalent to <a href="https://docs.python.org/3/library/typing.html#typing.Annotated" title="(in Python v3.14)"><code>typing.Annotated</code></a> so type checkers understand the intent of the code.

For example usage, check <a href="#discord.app_commands.Transformer" title="discord.app_commands.Transformer"><code>Transformer</code></a>.

New in version 2.0.

</dd></dl>

#### Range ¶

<dl><dt>*class*discord.app_commands.Range<a href="#discord.app_commands.Range" title="Permalink to this definition">¶</a></dt>
<dd>

A type annotation that can be applied to a parameter to require a numeric or string type to fit within the range provided.

During type checking time this is equivalent to <a href="https://docs.python.org/3/library/typing.html#typing.Annotated" title="(in Python v3.14)"><code>typing.Annotated</code></a> so type checkers understand the intent of the code.

Some example ranges:

- <code>Range[int, 10]</code> means the minimum is 10 with no maximum.
- <code>Range[int, None, 10]</code> means the maximum is 10 with no minimum.
- <code>Range[int, 1, 10]</code> means the minimum is 1 and the maximum is 10.
- <code>Range[float, 1.0, 5.0]</code> means the minimum is 1.0 and the maximum is 5.0.
- <code>Range[str, 1, 10]</code> means the minimum length is 1 and the maximum length is 10.

New in version 2.0.

Examples

```
@app_commands.command()
async def range(interaction: discord.Interaction, value: app_commands.Range[int, 10, 12]):
    await interaction.response.send_message(f'Your value is {value}', ephemeral=True)

```

</dd></dl>

#### Timestamp ¶

Attributes

- [type](#discord.app_commands.Timestamp.type)

Methods

- async [transform](#discord.app_commands.Timestamp.transform)

<dl><dt>*class*discord.app_commands.Timestamp(**args*, ***kwds*)<a href="#discord.app_commands.Timestamp" title="Permalink to this definition">¶</a></dt>
<dd>

A type annotation that can be applied to a parameter for transforming a <a href="https://discord.com/developers/docs/reference#message-formatting">Discord style timestamp</a> input to a <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>.

New in version 2.7.

Warning

Due to a Discord limitation, no timezone is provided with the input. The UTC timezone has been supplanted instead.

Examples

```
@app_commands.command()
async def datetime(interaction: discord.Interaction, value: app_commands.Timestamp):
    await interaction.response.send_message(value.isoformat())

```

<dl><dt>*property*type<a href="#discord.app_commands.Timestamp.type" title="Permalink to this definition">¶</a></dt>
<dd>

The option type associated with this transformer.

This must be a <a href="https://docs.python.org/3/library/functions.html#property" title="(in Python v3.14)"><code>property</code></a>.

Defaults to <a href="#discord.AppCommandOptionType.string" title="discord.AppCommandOptionType.string"><code>string</code></a>.

<dl><dt>Type</dt>
<dd>

<a href="#discord.AppCommandOptionType" title="discord.AppCommandOptionType"><code>AppCommandOptionType</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* transform(*interaction*, *value*, */*)<a href="#discord.app_commands.Timestamp.transform" title="Permalink to this definition">¶</a></dt>
<dd>

This function *could be a* <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Transforms the converted option value into another value.

The value passed into this transform function is the same as the one in the <a href="#discord.app_commands.Namespace" title="discord.app_commands.Namespace"><code>conversion table</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **interaction** (<a href="#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction being handled.
- **value** (*Any*) – The value of the given argument after being resolved. See the <a href="#discord.app_commands.Namespace" title="discord.app_commands.Namespace"><code>conversion table</code></a> for how certain option types correspond to certain values.

</dd></dl></dd>
</dl></dd>
</dl>

### Translations ¶

#### Translator ¶

Methods

- async [load](#discord.app_commands.Translator.load)
- async [translate](#discord.app_commands.Translator.translate)
- async [unload](#discord.app_commands.Translator.unload)

<dl><dt>*class*discord.app_commands.Translator<a href="#discord.app_commands.Translator" title="Permalink to this definition">¶</a></dt>
<dd>

A class that handles translations for commands, parameters, and choices.

Translations are done lazily in order to allow for async enabled translations as well as supporting a wide array of translation systems such as <a href="https://docs.python.org/3/library/gettext.html#module-gettext" title="(in Python v3.14)"><code>gettext</code></a> and <a href="https://projectfluent.org">Project Fluent</a>.

In order for a translator to be used, it must be set using the <a href="#discord.app_commands.CommandTree.set_translator" title="discord.app_commands.CommandTree.set_translator"><code>CommandTree.set_translator()</code></a> method. The translation flow for a string is as follows:

1. <dl><dt>Use <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> instead of <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a> in areas of a command you want to be translated.</dt><dd>
   - Currently, these are command names, command descriptions, parameter names, parameter descriptions, and choice names.
   - This can also be used inside the <a href="#discord.app_commands.describe" title="discord.app_commands.describe"><code>describe()</code></a> decorator.</dd></dl>
2. Call <a href="#discord.app_commands.CommandTree.set_translator" title="discord.app_commands.CommandTree.set_translator"><code>CommandTree.set_translator()</code></a> to the translator instance that will handle the translations.
3. Call <a href="#discord.app_commands.CommandTree.sync" title="discord.app_commands.CommandTree.sync"><code>CommandTree.sync()</code></a>
4. The library will call <a href="#discord.app_commands.Translator.translate" title="discord.app_commands.Translator.translate"><code>Translator.translate()</code></a> on all the relevant strings being translated.

New in version 2.0.

<dl><dt>*await* load()<a href="#discord.app_commands.Translator.load" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

An asynchronous setup function for loading the translation system.

The default implementation does nothing.

This is invoked when <a href="#discord.app_commands.CommandTree.set_translator" title="discord.app_commands.CommandTree.set_translator"><code>CommandTree.set_translator()</code></a> is called.

</dd></dl><dl><dt>*await* unload()<a href="#discord.app_commands.Translator.unload" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

An asynchronous teardown function for unloading the translation system.

The default implementation does nothing.

This is invoked when <a href="#discord.app_commands.CommandTree.set_translator" title="discord.app_commands.CommandTree.set_translator"><code>CommandTree.set_translator()</code></a> is called if a tree already has a translator or when <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client.close" title="discord.Client.close"><code>discord.Client.close()</code></a> is called.

</dd></dl><dl><dt>*await* translate(*string*, *locale*, *context*)<a href="#discord.app_commands.Translator.translate" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Translates the given string to the specified locale.

If the string cannot be translated, <code>None</code> should be returned.

The default implementation returns <code>None</code>.

If an exception is raised in this method, it should inherit from <a href="#discord.app_commands.TranslationError" title="discord.app_commands.TranslationError"><code>TranslationError</code></a>. If it doesn’t, then when this is called the exception will be chained with it instead.

<dl><dt>Parameters</dt>
<dd>

- **string** (<a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>) – The string being translated.
- **locale** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>) – The locale being requested for translation.
- **context** (<a href="#discord.app_commands.TranslationContext" title="discord.app_commands.TranslationContext"><code>TranslationContext</code></a>) – The translation context where the string originated from. For better type checking ergonomics, the <code>TranslationContextTypes</code> type can be used instead to aid with type narrowing. It is functionally equivalent to <a href="#discord.app_commands.TranslationContext" title="discord.app_commands.TranslationContext"><code>TranslationContext</code></a>.

</dd></dl></dd>
</dl></dd>
</dl>

#### locale\_str ¶

Attributes

- [extras](#discord.app_commands.locale_str.extras)
- [message](#discord.app_commands.locale_str.message)

<dl><dt>*class*discord.app_commands.locale_str(*message*, */*, ***kwargs*)<a href="#discord.app_commands.locale_str" title="Permalink to this definition">¶</a></dt>
<dd>

Marks a string as ready for translation.

This is done lazily and is not actually translated until <a href="#discord.app_commands.CommandTree.sync" title="discord.app_commands.CommandTree.sync"><code>CommandTree.sync()</code></a> is called.

The sync method then ultimately defers the responsibility of translating to the <a href="#discord.app_commands.Translator" title="discord.app_commands.Translator"><code>Translator</code></a> instance used by the <a href="#discord.app_commands.CommandTree" title="discord.app_commands.CommandTree"><code>CommandTree</code></a>. For more information on the translation flow, see the <a href="#discord.app_commands.Translator" title="discord.app_commands.Translator"><code>Translator</code></a> documentation.

<dl><dt>str(x)</dt>
<dd>

Returns the message passed to the string.

</dd></dl><dl><dt>x == y</dt>
<dd>

Checks if the string is equal to another string.

</dd></dl><dl><dt>x != y</dt>
<dd>

Checks if the string is not equal to another string.

</dd></dl><dl><dt>hash(x)</dt>
<dd>

Returns the hash of the string.

</dd></dl>

New in version 2.0.

<dl><dt>message<a href="#discord.app_commands.locale_str.message" title="Permalink to this definition">¶</a></dt>
<dd>

The message being translated. Once set, this cannot be changed.

Warning

This must be the default “message” that you send to Discord. Discord sends this message back to the library and the library uses it to access the data in order to dispatch commands.

For example, in a command name context, if the command name is <code>foo</code> then the message *must* also be <code>foo</code>. For other translation systems that require a message ID such as Fluent, consider using a keyword argument to pass it in.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>extras<a href="#discord.app_commands.locale_str.extras" title="Permalink to this definition">¶</a></dt>
<dd>

A dict of user provided extras to attach to the translated string. This can be used to add more context, information, or any metadata necessary to aid in actually translating the string.

Since these are passed via keyword arguments, the keys are strings.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

#### TranslationContext ¶

Attributes

- [data](#discord.app_commands.TranslationContext.data)
- [location](#discord.app_commands.TranslationContext.location)

<dl><dt>*class*discord.app_commands.TranslationContext(*location*, *data*)<a href="#discord.app_commands.TranslationContext" title="Permalink to this definition">¶</a></dt>
<dd>

A class that provides context for the <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> being translated.

This is useful to determine where exactly the string is located and aid in looking up the actual translation.

<dl><dt>location<a href="#discord.app_commands.TranslationContext.location" title="Permalink to this definition">¶</a></dt>
<dd>

The location where this string is located.

<dl><dt>Type</dt>
<dd>

<a href="#discord.app_commands.TranslationContextLocation" title="discord.app_commands.TranslationContextLocation"><code>TranslationContextLocation</code></a>

</dd></dl></dd>
</dl><dl><dt>data<a href="#discord.app_commands.TranslationContext.data" title="Permalink to this definition">¶</a></dt>
<dd>

The extraneous data that is being translated.

<dl><dt>Type</dt>
<dd>

Any

</dd></dl></dd>
</dl></dd>
</dl>

#### TranslationContextLocation ¶

<dl><dt>*class*discord.app_commands.TranslationContextLocation<a href="#discord.app_commands.TranslationContextLocation" title="Permalink to this definition">¶</a></dt>
<dd>

An enum representing the location context that the translation occurs in when requested for translation.

New in version 2.0.

<dl><dt>command_name<a href="#discord.app_commands.TranslationContextLocation.command_name" title="Permalink to this definition">¶</a></dt>
<dd>

The translation involved a command name.

</dd></dl><dl><dt>command_description<a href="#discord.app_commands.TranslationContextLocation.command_description" title="Permalink to this definition">¶</a></dt>
<dd>

The translation involved a command description.

</dd></dl><dl><dt>group_name<a href="#discord.app_commands.TranslationContextLocation.group_name" title="Permalink to this definition">¶</a></dt>
<dd>

The translation involved a group name.

</dd></dl><dl><dt>group_description<a href="#discord.app_commands.TranslationContextLocation.group_description" title="Permalink to this definition">¶</a></dt>
<dd>

The translation involved a group description.

</dd></dl><dl><dt>parameter_name<a href="#discord.app_commands.TranslationContextLocation.parameter_name" title="Permalink to this definition">¶</a></dt>
<dd>

The translation involved a parameter name.

</dd></dl><dl><dt>parameter_description<a href="#discord.app_commands.TranslationContextLocation.parameter_description" title="Permalink to this definition">¶</a></dt>
<dd>

The translation involved a parameter description.

</dd></dl><dl><dt>choice_name<a href="#discord.app_commands.TranslationContextLocation.choice_name" title="Permalink to this definition">¶</a></dt>
<dd>

The translation involved a choice name.

</dd></dl><dl><dt>other<a href="#discord.app_commands.TranslationContextLocation.other" title="Permalink to this definition">¶</a></dt>
<dd>

The translation involved something else entirely. This is useful for running <a href="#discord.app_commands.Translator.translate" title="discord.app_commands.Translator.translate"><code>Translator.translate()</code></a> for custom usage.

</dd></dl></dd>
</dl>

### Exceptions ¶

<dl><dt>*exception*discord.app_commands.AppCommandError<a href="#discord.app_commands.AppCommandError" title="Permalink to this definition">¶</a></dt>
<dd>

The base exception type for all application command related errors.

This inherits from <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.DiscordException" title="discord.DiscordException"><code>discord.DiscordException</code></a>.

This exception and exceptions inherited from it are handled in a special way as they are caught and passed into various error handlers in this order:

- <a href="#discord.app_commands.Command.error" title="discord.app_commands.Command.error"><code>Command.error</code></a>
- <a href="#discord.app_commands.Group.on_error" title="discord.app_commands.Group.on_error"><code>Group.on_error</code></a>
- <a href="#discord.app_commands.CommandTree.on_error" title="discord.app_commands.CommandTree.on_error"><code>CommandTree.on_error</code></a>

New in version 2.0.

</dd></dl><dl><dt>*exception*discord.app_commands.CommandInvokeError(*command*, *e*)<a href="#discord.app_commands.CommandInvokeError" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when the command being invoked raised an exception.

This inherits from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

New in version 2.0.

<dl><dt>original<a href="#discord.app_commands.CommandInvokeError.original" title="Permalink to this definition">¶</a></dt>
<dd>

The original exception that was raised. You can also get this via the <code>__cause__</code> attribute.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a>

</dd></dl></dd>
</dl><dl><dt>command<a href="#discord.app_commands.CommandInvokeError.command" title="Permalink to this definition">¶</a></dt>
<dd>

The command that failed.

<dl><dt>Type</dt>
<dd>

Union\[<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.ContextMenu" title="discord.app_commands.ContextMenu"><code>ContextMenu</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.TransformerError(*value*, *opt_type*, *transformer*)<a href="#discord.app_commands.TransformerError" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when a <a href="#discord.app_commands.Transformer" title="discord.app_commands.Transformer"><code>Transformer</code></a> or type annotation fails to convert to its target type.

This inherits from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

If an exception occurs while converting that does not subclass <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a> then the exception is wrapped into this exception. The original exception can be retrieved using the <code>__cause__</code> attribute. Otherwise if the exception derives from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a> then it will be propagated as-is.

New in version 2.0.

<dl><dt>value<a href="#discord.app_commands.TransformerError.value" title="Permalink to this definition">¶</a></dt>
<dd>

The value that failed to convert.

<dl><dt>Type</dt>
<dd>

Any

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.app_commands.TransformerError.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of argument that failed to convert.

<dl><dt>Type</dt>
<dd>

<a href="#discord.AppCommandOptionType" title="discord.AppCommandOptionType"><code>AppCommandOptionType</code></a>

</dd></dl></dd>
</dl><dl><dt>transformer<a href="#discord.app_commands.TransformerError.transformer" title="Permalink to this definition">¶</a></dt>
<dd>

The transformer that failed the conversion.

<dl><dt>Type</dt>
<dd>

<a href="#discord.app_commands.Transformer" title="discord.app_commands.Transformer"><code>Transformer</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.TranslationError(**msg*, *string=None*, *locale=None*, *context*)<a href="#discord.app_commands.TranslationError" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when the library fails to translate a string.

This inherits from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

If an exception occurs while calling <a href="#discord.app_commands.Translator.translate" title="discord.app_commands.Translator.translate"><code>Translator.translate()</code></a> that does not subclass this then the exception is wrapped into this exception. The original exception can be retrieved using the <code>__cause__</code> attribute. Otherwise it will be propagated as-is.

New in version 2.0.

<dl><dt>string<a href="#discord.app_commands.TranslationError.string" title="Permalink to this definition">¶</a></dt>
<dd>

The string that caused the error, if any.

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]]

</dd></dl></dd>
</dl><dl><dt>locale<a href="#discord.app_commands.TranslationError.locale" title="Permalink to this definition">¶</a></dt>
<dd>

The locale that caused the error, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Locale" title="discord.Locale"><code>Locale</code></a>]

</dd></dl></dd>
</dl><dl><dt>context<a href="#discord.app_commands.TranslationError.context" title="Permalink to this definition">¶</a></dt>
<dd>

The context of the translation that triggered the error.

<dl><dt>Type</dt>
<dd>

<a href="#discord.app_commands.TranslationContext" title="discord.app_commands.TranslationContext"><code>TranslationContext</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.CheckFailure<a href="#discord.app_commands.CheckFailure" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when check predicates in a command have failed.

This inherits from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

New in version 2.0.

</dd></dl><dl><dt>*exception*discord.app_commands.NoPrivateMessage(*message=None*)<a href="#discord.app_commands.NoPrivateMessage" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when a command does not work in a direct message.

This inherits from <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 2.0.

</dd></dl><dl><dt>*exception*discord.app_commands.MissingRole(*missing_role*)<a href="#discord.app_commands.MissingRole" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when the command invoker lacks a role to run a command.

This inherits from <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 2.0.

<dl><dt>missing_role<a href="#discord.app_commands.MissingRole.missing_role" title="Permalink to this definition">¶</a></dt>
<dd>

The required role that is missing. This is the parameter passed to <a href="#discord.app_commands.checks.has_role" title="discord.app_commands.checks.has_role"><code>has_role()</code></a>.

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.MissingAnyRole(*missing_roles*)<a href="#discord.app_commands.MissingAnyRole" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when the command invoker lacks any of the roles specified to run a command.

This inherits from <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 2.0.

<dl><dt>missing_roles<a href="#discord.app_commands.MissingAnyRole.missing_roles" title="Permalink to this definition">¶</a></dt>
<dd>

The roles that the invoker is missing. These are the parameters passed to <a href="#discord.app_commands.checks.has_any_role" title="discord.app_commands.checks.has_any_role"><code>has_any_role()</code></a>.

<dl><dt>Type</dt>
<dd>

List\[Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.MissingPermissions(*missing_permissions*, **args*)<a href="#discord.app_commands.MissingPermissions" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when the command invoker lacks permissions to run a command.

This inherits from <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 2.0.

<dl><dt>missing_permissions<a href="#discord.app_commands.MissingPermissions.missing_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The required permissions that are missing.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.BotMissingPermissions(*missing_permissions*, **args*)<a href="#discord.app_commands.BotMissingPermissions" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when the bot’s member lacks permissions to run a command.

This inherits from <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 2.0.

<dl><dt>missing_permissions<a href="#discord.app_commands.BotMissingPermissions.missing_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The required permissions that are missing.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.CommandOnCooldown(*cooldown*, *retry_after*)<a href="#discord.app_commands.CommandOnCooldown" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when the command being invoked is on cooldown.

This inherits from <a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 2.0.

<dl><dt>cooldown<a href="#discord.app_commands.CommandOnCooldown.cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

The cooldown that was triggered.

<dl><dt>Type</dt>
<dd>

<a href="#discord.app_commands.Cooldown" title="discord.app_commands.Cooldown"><code>Cooldown</code></a>

</dd></dl></dd>
</dl><dl><dt>retry_after<a href="#discord.app_commands.CommandOnCooldown.retry_after" title="Permalink to this definition">¶</a></dt>
<dd>

The amount of seconds to wait before you can retry again.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.CommandLimitReached(*guild_id*, *limit*, *type=&lt;AppCommandType.chat_input: 1&gt;*)<a href="#discord.app_commands.CommandLimitReached" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when the maximum number of application commands was reached either globally or in a guild.

This inherits from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

New in version 2.0.

<dl><dt>type<a href="#discord.app_commands.CommandLimitReached.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of command that reached the limit.

<dl><dt>Type</dt>
<dd>

<a href="#discord.AppCommandType" title="discord.AppCommandType"><code>AppCommandType</code></a>

</dd></dl></dd>
</dl><dl><dt>guild_id<a href="#discord.app_commands.CommandLimitReached.guild_id" title="Permalink to this definition">¶</a></dt>
<dd>

The guild ID that reached the limit or <code>None</code> if it was global.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>limit<a href="#discord.app_commands.CommandLimitReached.limit" title="Permalink to this definition">¶</a></dt>
<dd>

The limit that was hit.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.CommandAlreadyRegistered(*name*, *guild_id*)<a href="#discord.app_commands.CommandAlreadyRegistered" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when a command is already registered.

This inherits from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

New in version 2.0.

<dl><dt>name<a href="#discord.app_commands.CommandAlreadyRegistered.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the command already registered.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>guild_id<a href="#discord.app_commands.CommandAlreadyRegistered.guild_id" title="Permalink to this definition">¶</a></dt>
<dd>

The guild ID this command was already registered at. If <code>None</code> then it was a global command.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.CommandSignatureMismatch(*command*)<a href="#discord.app_commands.CommandSignatureMismatch" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when an application command from Discord has a different signature from the one provided in the code. This happens because your command definition differs from the command definition you provided Discord. Either your code is out of date or the data from Discord is out of sync.

This inherits from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

New in version 2.0.

<dl><dt>command<a href="#discord.app_commands.CommandSignatureMismatch.command" title="Permalink to this definition">¶</a></dt>
<dd>

The command that had the signature mismatch.

<dl><dt>Type</dt>
<dd>

Union\[<a href="#discord.app_commands.Command" title="discord.app_commands.Command"><code>Command</code></a>, <a href="#discord.app_commands.ContextMenu" title="discord.app_commands.ContextMenu"><code>ContextMenu</code></a>, <a href="#discord.app_commands.Group" title="discord.app_commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.CommandNotFound(*name*, *parents*, *type=&lt;AppCommandType.chat_input: 1&gt;*)<a href="#discord.app_commands.CommandNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when an application command could not be found.

This inherits from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>.

New in version 2.0.

<dl><dt>name<a href="#discord.app_commands.CommandNotFound.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the application command not found.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>parents<a href="#discord.app_commands.CommandNotFound.parents" title="Permalink to this definition">¶</a></dt>
<dd>

A list of parent command names that were previously found prior to the application command not being found.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.app_commands.CommandNotFound.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type of command that was not found.

<dl><dt>Type</dt>
<dd>

<a href="#discord.AppCommandType" title="discord.AppCommandType"><code>AppCommandType</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.app_commands.CommandSyncFailure(*child*, *commands*)<a href="#discord.app_commands.CommandSyncFailure" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when <a href="#discord.app_commands.CommandTree.sync" title="discord.app_commands.CommandTree.sync"><code>CommandTree.sync()</code></a> failed.

This provides syncing failures in a slightly more readable format.

This inherits from <a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a> and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException"><code>HTTPException</code></a>.

New in version 2.0.

</dd></dl>

#### Exception Hierarchy ¶

- <dl><dt><a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.DiscordException" title="discord.DiscordException"><code>DiscordException</code></a></dt><dd>
  - <dl><dt><a href="#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a></dt><dd>
    - <a href="#discord.app_commands.CommandInvokeError" title="discord.app_commands.CommandInvokeError"><code>CommandInvokeError</code></a>
    - <a href="#discord.app_commands.TransformerError" title="discord.app_commands.TransformerError"><code>TransformerError</code></a>
    - <a href="#discord.app_commands.TranslationError" title="discord.app_commands.TranslationError"><code>TranslationError</code></a>
    - <dl><dt><a href="#discord.app_commands.CheckFailure" title="discord.app_commands.CheckFailure"><code>CheckFailure</code></a></dt><dd>
      - <a href="#discord.app_commands.NoPrivateMessage" title="discord.app_commands.NoPrivateMessage"><code>NoPrivateMessage</code></a>
      - <a href="#discord.app_commands.MissingRole" title="discord.app_commands.MissingRole"><code>MissingRole</code></a>
      - <a href="#discord.app_commands.MissingAnyRole" title="discord.app_commands.MissingAnyRole"><code>MissingAnyRole</code></a>
      - <a href="#discord.app_commands.MissingPermissions" title="discord.app_commands.MissingPermissions"><code>MissingPermissions</code></a>
      - <a href="#discord.app_commands.BotMissingPermissions" title="discord.app_commands.BotMissingPermissions"><code>BotMissingPermissions</code></a>
      - <a href="#discord.app_commands.CommandOnCooldown" title="discord.app_commands.CommandOnCooldown"><code>CommandOnCooldown</code></a></dd></dl>
    - <a href="#discord.app_commands.CommandLimitReached" title="discord.app_commands.CommandLimitReached"><code>CommandLimitReached</code></a>
    - <a href="#discord.app_commands.CommandAlreadyRegistered" title="discord.app_commands.CommandAlreadyRegistered"><code>CommandAlreadyRegistered</code></a>
    - <a href="#discord.app_commands.CommandSignatureMismatch" title="discord.app_commands.CommandSignatureMismatch"><code>CommandSignatureMismatch</code></a>
    - <a href="#discord.app_commands.CommandNotFound" title="discord.app_commands.CommandNotFound"><code>CommandNotFound</code></a>
    - <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID"><code>MissingApplicationID</code></a>
    - <a href="#discord.app_commands.CommandSyncFailure" title="discord.app_commands.CommandSyncFailure"><code>CommandSyncFailure</code></a></dd></dl>
  - <dl><dt><a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException"><code>HTTPException</code></a></dt><dd>
    - <a href="#discord.app_commands.CommandSyncFailure" title="discord.app_commands.CommandSyncFailure"><code>CommandSyncFailure</code></a></dd></dl></dd></dl>

close

# Settings

## Font

### Use a serif font:

## Theme

### Automatic

### Light

### Dark

arrow\_upwardto top