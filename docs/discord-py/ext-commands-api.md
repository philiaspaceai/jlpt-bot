---
source: https://discordpy.readthedocs.io/en/stable/ext/commands/api.html
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

- API Reference
  - [Bots](#bots)
    - [Bot](#bot)
    - [AutoShardedBot](#autoshardedbot)
  - [Prefix Helpers](#prefix-helpers)
  - [Event Reference](#event-reference)
  - [Commands](#commands)
    - [Decorators](#decorators)
    - [Command](#command)
    - [Group](#group)
    - [GroupMixin](#groupmixin)
    - [HybridCommand](#hybridcommand)
    - [HybridGroup](#hybridgroup)
  - [Cogs](#cogs)
    - [Cog](#cog)
    - [GroupCog](#groupcog)
    - [CogMeta](#cogmeta)
  - [Help Commands](#help-commands)
    - [HelpCommand](#helpcommand)
    - [DefaultHelpCommand](#defaulthelpcommand)
    - [MinimalHelpCommand](#minimalhelpcommand)
    - [Paginator](#paginator)
  - [Enums](#enums)
  - [Checks](#checks)
  - [Context](#context)
  - [Converters](#converters)
    - [Flag Converter](#flag-converter)
  - [Defaults](#defaults)
  - [Exceptions](#exceptions)
    - [Exception Hierarchy](#exception-hierarchy)

# API Reference ¶

The following section outlines the API of discord.py’s command extension module.

## Bots ¶

### Bot ¶

Attributes

- [activity](#discord.ext.commands.Bot.activity)
- [allowed\_contexts](#discord.ext.commands.Bot.allowed_contexts)
- [allowed\_installs](#discord.ext.commands.Bot.allowed_installs)
- [allowed\_mentions](#discord.ext.commands.Bot.allowed_mentions)
- [application](#discord.ext.commands.Bot.application)
- [application\_flags](#discord.ext.commands.Bot.application_flags)
- [application\_id](#discord.ext.commands.Bot.application_id)
- [cached\_messages](#discord.ext.commands.Bot.cached_messages)
- [case\_insensitive](#discord.ext.commands.Bot.case_insensitive)
- [cogs](#discord.ext.commands.Bot.cogs)
- [command\_prefix](#discord.ext.commands.Bot.command_prefix)
- [commands](#discord.ext.commands.Bot.commands)
- [description](#discord.ext.commands.Bot.description)
- [emojis](#discord.ext.commands.Bot.emojis)
- [extensions](#discord.ext.commands.Bot.extensions)
- [guilds](#discord.ext.commands.Bot.guilds)
- [help\_command](#discord.ext.commands.Bot.help_command)
- [intents](#discord.ext.commands.Bot.intents)
- [latency](#discord.ext.commands.Bot.latency)
- [owner\_id](#discord.ext.commands.Bot.owner_id)
- [owner\_ids](#discord.ext.commands.Bot.owner_ids)
- [persistent\_views](#discord.ext.commands.Bot.persistent_views)
- [private\_channels](#discord.ext.commands.Bot.private_channels)
- [soundboard\_sounds](#discord.ext.commands.Bot.soundboard_sounds)
- [status](#discord.ext.commands.Bot.status)
- [stickers](#discord.ext.commands.Bot.stickers)
- [strip\_after\_prefix](#discord.ext.commands.Bot.strip_after_prefix)
- [tree](#discord.ext.commands.Bot.tree)
- [tree\_cls](#discord.ext.commands.Bot.tree_cls)
- [user](#discord.ext.commands.Bot.user)
- [users](#discord.ext.commands.Bot.users)
- [voice\_clients](#discord.ext.commands.Bot.voice_clients)

Methods

- def [add\_check](#discord.ext.commands.Bot.add_check)
- async [add\_cog](#discord.ext.commands.Bot.add_cog)
- def [add\_command](#discord.ext.commands.Bot.add_command)
- def [add\_dynamic\_items](#discord.ext.commands.Bot.add_dynamic_items)
- def [add\_listener](#discord.ext.commands.Bot.add_listener)
- def [add\_view](#discord.ext.commands.Bot.add_view)
- @ [after\_invoke](#discord.ext.commands.Bot.after_invoke)
- async [application\_info](#discord.ext.commands.Bot.application_info)
- async [before\_identify\_hook](#discord.ext.commands.Bot.before_identify_hook)
- @ [before\_invoke](#discord.ext.commands.Bot.before_invoke)
- async [change\_presence](#discord.ext.commands.Bot.change_presence)
- @ [check](#discord.ext.commands.Bot.check)
- @ [check\_once](#discord.ext.commands.Bot.check_once)
- def [clear](#discord.ext.commands.Bot.clear)
- async [close](#discord.ext.commands.Bot.close)
- @ [command](#discord.ext.commands.Bot.command)
- async [connect](#discord.ext.commands.Bot.connect)
- async [create\_application\_emoji](#discord.ext.commands.Bot.create_application_emoji)
- async [create\_dm](#discord.ext.commands.Bot.create_dm)
- async [create\_entitlement](#discord.ext.commands.Bot.create_entitlement)
- async [create\_guild](#discord.ext.commands.Bot.create_guild)
- async [delete\_invite](#discord.ext.commands.Bot.delete_invite)
- async for [entitlements](#discord.ext.commands.Bot.entitlements)
- @ [event](#discord.ext.commands.Bot.event)
- async [fetch\_application\_emoji](#discord.ext.commands.Bot.fetch_application_emoji)
- async [fetch\_application\_emojis](#discord.ext.commands.Bot.fetch_application_emojis)
- async [fetch\_channel](#discord.ext.commands.Bot.fetch_channel)
- async [fetch\_entitlement](#discord.ext.commands.Bot.fetch_entitlement)
- async [fetch\_guild](#discord.ext.commands.Bot.fetch_guild)
- async [fetch\_guild\_preview](#discord.ext.commands.Bot.fetch_guild_preview)
- async for [fetch\_guilds](#discord.ext.commands.Bot.fetch_guilds)
- async [fetch\_invite](#discord.ext.commands.Bot.fetch_invite)
- async [fetch\_premium\_sticker\_pack](#discord.ext.commands.Bot.fetch_premium_sticker_pack)
- async [fetch\_premium\_sticker\_packs](#discord.ext.commands.Bot.fetch_premium_sticker_packs)
- async [fetch\_skus](#discord.ext.commands.Bot.fetch_skus)
- async [fetch\_soundboard\_default\_sounds](#discord.ext.commands.Bot.fetch_soundboard_default_sounds)
- async [fetch\_stage\_instance](#discord.ext.commands.Bot.fetch_stage_instance)
- async [fetch\_sticker](#discord.ext.commands.Bot.fetch_sticker)
- async [fetch\_template](#discord.ext.commands.Bot.fetch_template)
- async [fetch\_user](#discord.ext.commands.Bot.fetch_user)
- async [fetch\_webhook](#discord.ext.commands.Bot.fetch_webhook)
- async [fetch\_widget](#discord.ext.commands.Bot.fetch_widget)
- def [get\_all\_channels](#discord.ext.commands.Bot.get_all_channels)
- def [get\_all\_members](#discord.ext.commands.Bot.get_all_members)
- def [get\_channel](#discord.ext.commands.Bot.get_channel)
- def [get\_cog](#discord.ext.commands.Bot.get_cog)
- def [get\_command](#discord.ext.commands.Bot.get_command)
- async [get\_context](#discord.ext.commands.Bot.get_context)
- def [get\_emoji](#discord.ext.commands.Bot.get_emoji)
- def [get\_guild](#discord.ext.commands.Bot.get_guild)
- def [get\_partial\_messageable](#discord.ext.commands.Bot.get_partial_messageable)
- async [get\_prefix](#discord.ext.commands.Bot.get_prefix)
- def [get\_soundboard\_sound](#discord.ext.commands.Bot.get_soundboard_sound)
- def [get\_stage\_instance](#discord.ext.commands.Bot.get_stage_instance)
- def [get\_sticker](#discord.ext.commands.Bot.get_sticker)
- def [get\_user](#discord.ext.commands.Bot.get_user)
- @ [group](#discord.ext.commands.Bot.group)
- @ [hybrid\_command](#discord.ext.commands.Bot.hybrid_command)
- @ [hybrid\_group](#discord.ext.commands.Bot.hybrid_group)
- async [invoke](#discord.ext.commands.Bot.invoke)
- def [is\_closed](#discord.ext.commands.Bot.is_closed)
- async [is\_owner](#discord.ext.commands.Bot.is_owner)
- def [is\_ready](#discord.ext.commands.Bot.is_ready)
- def [is\_ws\_ratelimited](#discord.ext.commands.Bot.is_ws_ratelimited)
- @ [listen](#discord.ext.commands.Bot.listen)
- async [load\_extension](#discord.ext.commands.Bot.load_extension)
- async [login](#discord.ext.commands.Bot.login)
- async [on\_command\_error](#discord.ext.commands.Bot.on_command_error)
- async [on\_error](#discord.ext.commands.Bot.on_error)
- async [process\_commands](#discord.ext.commands.Bot.process_commands)
- async [reload\_extension](#discord.ext.commands.Bot.reload_extension)
- def [remove\_check](#discord.ext.commands.Bot.remove_check)
- async [remove\_cog](#discord.ext.commands.Bot.remove_cog)
- def [remove\_command](#discord.ext.commands.Bot.remove_command)
- def [remove\_dynamic\_items](#discord.ext.commands.Bot.remove_dynamic_items)
- def [remove\_listener](#discord.ext.commands.Bot.remove_listener)
- def [run](#discord.ext.commands.Bot.run)
- async [setup\_hook](#discord.ext.commands.Bot.setup_hook)
- async [start](#discord.ext.commands.Bot.start)
- async [unload\_extension](#discord.ext.commands.Bot.unload_extension)
- async [wait\_for](#discord.ext.commands.Bot.wait_for)
- async [wait\_until\_ready](#discord.ext.commands.Bot.wait_until_ready)
- def [walk\_commands](#discord.ext.commands.Bot.walk_commands)

<dl><dt>*class*discord.ext.commands.Bot(*command_prefix*, ***, *help_command=&lt;default-help-command&gt;*, *tree_cls=&lt;class 'discord.app_commands.tree.CommandTree'&gt;*, *description=None*, *allowed_contexts=...*, *allowed_installs=...*, *intents*, ***options*)<a href="#discord.ext.commands.Bot" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a Discord bot.

This class is a subclass of <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client" title="discord.Client"><code>discord.Client</code></a> and as a result anything that you can do with a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client" title="discord.Client"><code>discord.Client</code></a> you can do with this bot.

This class also subclasses <a href="#discord.ext.commands.GroupMixin" title="discord.ext.commands.GroupMixin"><code>GroupMixin</code></a> to provide the functionality to manage commands.

Unlike <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client" title="discord.Client"><code>discord.Client</code></a>, this class does not require manually setting a <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.CommandTree" title="discord.app_commands.CommandTree"><code>CommandTree</code></a> and is automatically set upon instantiating the class.

<dl><dt>async with x</dt>
<dd>

Asynchronously initialises the bot and automatically cleans up.

New in version 2.0.

</dd></dl>

<dl><dt>command_prefix<a href="#discord.ext.commands.Bot.command_prefix" title="Permalink to this definition">¶</a></dt>
<dd>

The command prefix is what the message content must contain initially to have a command invoked. This prefix could either be a string to indicate what the prefix should be, or a callable that takes in the bot as its first parameter and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>discord.Message</code></a> as its second parameter and returns the prefix. This is to facilitate “dynamic” command prefixes. This callable can be either a regular function or a coroutine.

An empty string as the prefix always matches, enabling prefix-less command invocation. While this may be useful in DMs it should be avoided in servers, as it’s likely to cause performance issues and unintended command invocations.

The command prefix could also be an iterable of strings indicating that multiple checks for the prefix should be used and the first one to match will be the invocation prefix. You can get this prefix via <a href="#discord.ext.commands.Context.prefix" title="discord.ext.commands.Context.prefix"><code>Context.prefix</code></a>.

Note

When passing multiple prefixes be careful to not pass a prefix that matches a longer prefix occurring later in the sequence. For example, if the command prefix is <code>('!', '!?')</code> the <code>'!?'</code> prefix will never be matched to any message as the previous one matches messages starting with <code>!?</code>. This is especially important when passing an empty string, it should always be last as no prefix after it will be matched.

</dd></dl><dl><dt>case_insensitive<a href="#discord.ext.commands.Bot.case_insensitive" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the commands should be case insensitive. Defaults to <code>False</code>. This attribute does not carry over to groups. You must set it to every group if you require group commands to be case insensitive as well.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.ext.commands.Bot.description" title="Permalink to this definition">¶</a></dt>
<dd>

The content prefixed into the default help message.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>help_command<a href="#discord.ext.commands.Bot.help_command" title="Permalink to this definition">¶</a></dt>
<dd>

The help command implementation to use. This can be dynamically set at runtime. To remove the help command pass <code>None</code>. For more information on implementing a help command, see <a href="#ext-commands-help-command">Help Commands</a>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.HelpCommand" title="discord.ext.commands.HelpCommand"><code>HelpCommand</code></a>]

</dd></dl></dd>
</dl><dl><dt>owner_id<a href="#discord.ext.commands.Bot.owner_id" title="Permalink to this definition">¶</a></dt>
<dd>

The user ID that owns the bot. If this is not set and is then queried via <a href="#discord.ext.commands.Bot.is_owner" title="discord.ext.commands.Bot.is_owner"><code>is_owner()</code></a> then it is fetched automatically using <a href="#discord.ext.commands.Bot.application_info" title="discord.ext.commands.Bot.application_info"><code>application_info()</code></a>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>owner_ids<a href="#discord.ext.commands.Bot.owner_ids" title="Permalink to this definition">¶</a></dt>
<dd>

The user IDs that owns the bot. This is similar to <a href="#discord.ext.commands.Bot.owner_id" title="discord.ext.commands.Bot.owner_id"><code>owner_id</code></a>. If this is not set and the application is team based, then it is fetched automatically using <a href="#discord.ext.commands.Bot.application_info" title="discord.ext.commands.Bot.application_info"><code>application_info()</code></a>. For performance reasons it is recommended to use a <a href="https://docs.python.org/3/library/stdtypes.html#set" title="(in Python v3.14)"><code>set</code></a> for the collection. You cannot set both <code>owner_id</code> and <code>owner_ids</code>.

New in version 1.3.

<dl><dt>Type</dt>
<dd>

Optional\[Collection\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]]

</dd></dl></dd>
</dl><dl><dt>strip_after_prefix<a href="#discord.ext.commands.Bot.strip_after_prefix" title="Permalink to this definition">¶</a></dt>
<dd>

Whether to strip whitespace characters after encountering the command prefix. This allows for <code>!   hello</code> and <code>!hello</code> to both work if the <code>command_prefix</code> is set to <code>!</code>. Defaults to <code>False</code>.

New in version 1.7.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>tree_cls<a href="#discord.ext.commands.Bot.tree_cls" title="Permalink to this definition">¶</a></dt>
<dd>

The type of application command tree to use. Defaults to <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.CommandTree" title="discord.app_commands.CommandTree"><code>CommandTree</code></a>.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Type\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.CommandTree" title="discord.app_commands.CommandTree"><code>CommandTree</code></a>]

</dd></dl></dd>
</dl><dl><dt>allowed_contexts<a href="#discord.ext.commands.Bot.allowed_contexts" title="Permalink to this definition">¶</a></dt>
<dd>

The default allowed contexts that applies to all application commands in the application command tree.

Note that you can override this on a per command basis.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.AppCommandContext" title="discord.app_commands.AppCommandContext"><code>AppCommandContext</code></a>

</dd></dl></dd>
</dl><dl><dt>allowed_installs<a href="#discord.ext.commands.Bot.allowed_installs" title="Permalink to this definition">¶</a></dt>
<dd>

The default allowed install locations that apply to all application commands in the application command tree.

Note that you can override this on a per command basis.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.AppInstallationType" title="discord.app_commands.AppInstallationType"><code>AppInstallationType</code></a>

</dd></dl></dd>
</dl><dl><dt>@after_invoke<a href="#discord.ext.commands.Bot.after_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a post-invoke hook.

A post-invoke hook is called directly after the command is called. This makes it a useful function to clean-up database connections or any type of clean up required.

This post-invoke hook takes a sole parameter, a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

Note

Similar to <a href="#discord.ext.commands.Bot.before_invoke" title="discord.ext.commands.Bot.before_invoke"><code>before_invoke()</code></a>, this is not called unless checks and argument parsing procedures succeed. This hook is, however, **always** called regardless of the internal command callback raising an error (i.e. <a href="#discord.ext.commands.CommandInvokeError" title="discord.ext.commands.CommandInvokeError"><code>CommandInvokeError</code></a>). This makes it ideal for clean-up scenarios.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the post-invoke hook.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@before_invoke<a href="#discord.ext.commands.Bot.before_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a pre-invoke hook.

A pre-invoke hook is called directly before the command is called. This makes it a useful function to set up database connections or any type of set up required.

This pre-invoke hook takes a sole parameter, a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

Note

The <a href="#discord.ext.commands.Bot.before_invoke" title="discord.ext.commands.Bot.before_invoke"><code>before_invoke()</code></a> and <a href="#discord.ext.commands.Bot.after_invoke" title="discord.ext.commands.Bot.after_invoke"><code>after_invoke()</code></a> hooks are only called if all checks and argument parsing procedures pass without error. If any check or argument parsing procedures fail then the hooks are not called.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the pre-invoke hook.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@check<a href="#discord.ext.commands.Bot.check" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that adds a global check to the bot.

A global check is similar to a <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> that is applied on a per command basis except it is run before any command checks have been verified and applies to every command the bot has.

Note

This function can either be a regular function or a coroutine.

Similar to a command <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a>, this takes a single parameter of type <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a> and can only raise exceptions inherited from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

Example

```
@bot.check
def check_commands(ctx):
    return ctx.command.qualified_name in allowed_commands

```

Changed in version 2.0: <code>func</code> parameter is now positional-only.

</dd></dl><dl><dt>@check_once<a href="#discord.ext.commands.Bot.check_once" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that adds a “call once” global check to the bot.

Unlike regular global checks, this one is called only once per <a href="#discord.ext.commands.Bot.invoke" title="discord.ext.commands.Bot.invoke"><code>invoke()</code></a> call.

Regular global checks are called whenever a command is called or <a href="#discord.ext.commands.Command.can_run" title="discord.ext.commands.Command.can_run"><code>Command.can_run()</code></a> is called. This type of check bypasses that and ensures that it’s called only once, even inside the default help command.

Note

When using this function the <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a> sent to a group subcommand may only parse the parent command and not the subcommands due to it being invoked once per <a href="#discord.ext.commands.Bot.invoke" title="discord.ext.commands.Bot.invoke"><code>Bot.invoke()</code></a> call.

Note

This function can either be a regular function or a coroutine.

Similar to a command <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a>, this takes a single parameter of type <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a> and can only raise exceptions inherited from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

Example

```
@bot.check_once
def whitelist(ctx):
    return ctx.message.author.id in my_whitelist

```

Changed in version 2.0: <code>func</code> parameter is now positional-only.

</dd></dl><dl><dt>@command(**args*, ***kwargs*)<a href="#discord.ext.commands.Bot.command" title="Permalink to this definition">¶</a></dt>
<dd>

A shortcut decorator that invokes <a href="#discord.ext.commands.command" title="discord.ext.commands.command"><code>command()</code></a> and adds it to the internal command list via <a href="#discord.ext.commands.GroupMixin.add_command" title="discord.ext.commands.GroupMixin.add_command"><code>add_command()</code></a>.

<dl><dt>Returns</dt>
<dd>

A decorator that converts the provided method into a Command, adds it to the bot, then returns it.

</dd><dt>Return type</dt>
<dd>

Callable\[…, <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>@event<a href="#discord.ext.commands.Bot.event" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers an event to listen to.

You can find more info about the events on the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord-api-events">documentation below</a>.

The events must be a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>, if not, <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)"><code>TypeError</code></a> is raised.

Example

```
@client.event
async def on_ready():
    print('Ready!')

```

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@group(**args*, ***kwargs*)<a href="#discord.ext.commands.Bot.group" title="Permalink to this definition">¶</a></dt>
<dd>

A shortcut decorator that invokes <a href="#discord.ext.commands.group" title="discord.ext.commands.group"><code>group()</code></a> and adds it to the internal command list via <a href="#discord.ext.commands.GroupMixin.add_command" title="discord.ext.commands.GroupMixin.add_command"><code>add_command()</code></a>.

<dl><dt>Returns</dt>
<dd>

A decorator that converts the provided method into a Group, adds it to the bot, then returns it.

</dd><dt>Return type</dt>
<dd>

Callable\[…, <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>@hybrid_command(*name=...*, *with_app_command=True*, **args*, ***kwargs*)<a href="#discord.ext.commands.Bot.hybrid_command" title="Permalink to this definition">¶</a></dt>
<dd>

A shortcut decorator that invokes <a href="#discord.ext.commands.hybrid_command" title="discord.ext.commands.hybrid_command"><code>hybrid_command()</code></a> and adds it to the internal command list via <a href="#discord.ext.commands.Bot.add_command" title="discord.ext.commands.Bot.add_command"><code>add_command()</code></a>.

<dl><dt>Returns</dt>
<dd>

A decorator that converts the provided method into a Command, adds it to the bot, then returns it.

</dd><dt>Return type</dt>
<dd>

Callable\[…, <a href="#discord.ext.commands.HybridCommand" title="discord.ext.commands.HybridCommand"><code>HybridCommand</code></a>]

</dd></dl></dd>
</dl><dl><dt>@hybrid_group(*name=...*, *with_app_command=True*, **args*, ***kwargs*)<a href="#discord.ext.commands.Bot.hybrid_group" title="Permalink to this definition">¶</a></dt>
<dd>

A shortcut decorator that invokes <a href="#discord.ext.commands.hybrid_group" title="discord.ext.commands.hybrid_group"><code>hybrid_group()</code></a> and adds it to the internal command list via <a href="#discord.ext.commands.Bot.add_command" title="discord.ext.commands.Bot.add_command"><code>add_command()</code></a>.

<dl><dt>Returns</dt>
<dd>

A decorator that converts the provided method into a Group, adds it to the bot, then returns it.

</dd><dt>Return type</dt>
<dd>

Callable\[…, <a href="#discord.ext.commands.HybridGroup" title="discord.ext.commands.HybridGroup"><code>HybridGroup</code></a>]

</dd></dl></dd>
</dl><dl><dt>@listen(*name=None*)<a href="#discord.ext.commands.Bot.listen" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers another function as an external event listener. Basically this allows you to listen to multiple events from different places e.g. such as <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.on_ready" title="discord.on_ready"><code>on_ready()</code></a>

The functions being listened to must be a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>.

Example

```
@bot.listen()
async def on_message(message):
    print('one')

# in some other file...

@bot.listen('on_message')
async def my_message(message):
    print('two')

```

Would print one and two in an unspecified order.

<dl><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The function being listened to is not a coroutine.

</dd></dl></dd>
</dl><dl><dt>*property*activity<a href="#discord.ext.commands.Bot.activity" title="Permalink to this definition">¶</a></dt>
<dd>

The activity being used upon logging in.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.BaseActivity" title="discord.BaseActivity"><code>BaseActivity</code></a>]

</dd></dl></dd>
</dl><dl><dt>add_check(*func*, */*, ***, *call_once=False*)<a href="#discord.ext.commands.Bot.add_check" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a global check to the bot.

This is the non-decorator interface to <a href="#discord.ext.commands.Bot.check" title="discord.ext.commands.Bot.check"><code>check()</code></a> and <a href="#discord.ext.commands.Bot.check_once" title="discord.ext.commands.Bot.check_once"><code>check_once()</code></a>.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

See also

The <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> decorator

<dl><dt>Parameters</dt>
<dd>

- **func** – The function that was used as a global check.
- **call\_once** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If the function should only be called once per <a href="#discord.ext.commands.Bot.invoke" title="discord.ext.commands.Bot.invoke"><code>invoke()</code></a> call.

</dd></dl></dd>
</dl><dl><dt>*await* add_cog(*cog*, */*, ***, *override=False*, *guild=...*, *guilds=...*)<a href="#discord.ext.commands.Bot.add_cog" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Adds a “cog” to the bot.

A cog is a class that has its own event listeners and commands.

If the cog is a <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Group" title="discord.app_commands.Group"><code>app_commands.Group</code></a> then it is added to the bot’s <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.CommandTree" title="discord.app_commands.CommandTree"><code>CommandTree</code></a> as well.

Note

Exceptions raised inside a <a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>’s <a href="#discord.ext.commands.Cog.cog_load" title="discord.ext.commands.Cog.cog_load"><code>cog_load()</code></a> method will be propagated to the caller.

Changed in version 2.0: <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientException" title="discord.ClientException"><code>ClientException</code></a> is raised when a cog with the same name is already loaded.

Changed in version 2.0: <code>cog</code> parameter is now positional-only.

Changed in version 2.0: This method is now a <a href="https://docs.python.org/3/glossary.html#term-coroutine" title="(in Python v3.14)">coroutine</a>.

<dl><dt>Parameters</dt>
<dd>

- **cog** (<a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>) – The cog to register to the bot.
- **override** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  If a previously loaded cog with the same name should be ejected instead of raising an error.

  New in version 2.0.
- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  If the cog is an application command group, then this would be the guild where the cog group would be added to. If not given then it becomes a global command instead.

  New in version 2.0.
- **guilds** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  If the cog is an application command group, then this would be the guilds where the cog group would be added to. If not given then it becomes a global command instead. Cannot be mixed with <code>guild</code>.

  New in version 2.0.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The cog does not inherit from <a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>.
- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – An error happened during loading.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientException" title="discord.ClientException">**ClientException**</a> – A cog with the same name is already loaded.

</dd></dl></dd>
</dl><dl><dt>add_command(*command*, */*)<a href="#discord.ext.commands.Bot.add_command" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> into the internal list of commands.

This is usually not called, instead the <a href="#discord.ext.commands.GroupMixin.command" title="discord.ext.commands.GroupMixin.command"><code>command()</code></a> or <a href="#discord.ext.commands.GroupMixin.group" title="discord.ext.commands.GroupMixin.group"><code>group()</code></a> shortcut decorators are used instead.

Changed in version 1.4: Raise <a href="#discord.ext.commands.CommandRegistrationError" title="discord.ext.commands.CommandRegistrationError"><code>CommandRegistrationError</code></a> instead of generic <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientException" title="discord.ClientException"><code>ClientException</code></a>

Changed in version 2.0: <code>command</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command to add.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandRegistrationError" title="discord.ext.commands.CommandRegistrationError">**CommandRegistrationError**</a> – If the command or its alias is already registered by different command.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – If the command passed is not a subclass of <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>.

</dd></dl></dd>
</dl><dl><dt>add_dynamic_items(**items*)<a href="#discord.ext.commands.Bot.add_dynamic_items" title="Permalink to this definition">¶</a></dt>
<dd>

Registers <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> classes for persistent listening.

This method accepts *class types* rather than instances.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**\*items** (Type\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a>]) – The classes of dynamic items to add.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – A class is not a subclass of <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a>.

</dd></dl></dd>
</dl><dl><dt>add_listener(*func*, */*, *name=...*)<a href="#discord.ext.commands.Bot.add_listener" title="Permalink to this definition">¶</a></dt>
<dd>

The non decorator alternative to <a href="#discord.ext.commands.Bot.listen" title="discord.ext.commands.Bot.listen"><code>listen()</code></a>.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **func** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The function to call.
- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the event to listen for. Defaults to <code>func.__name__</code>.

</dd></dl>

Example

```
async def on_ready(): pass
async def my_message(message): pass

bot.add_listener(on_ready)
bot.add_listener(my_message, 'on_message')

```

</dd></dl><dl><dt>add_view(*view*, ***, *message_id=None*)<a href="#discord.ext.commands.Bot.add_view" title="Permalink to this definition">¶</a></dt>
<dd>

Registers a <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.View" title="discord.ui.View"><code>View</code></a> for persistent listening.

This method should be used for when a view is comprised of components that last longer than the lifecycle of the program.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **view** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.View" title="discord.ui.View"><code>discord.ui.View</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>discord.ui.LayoutView</code></a>]) – The view to register for dispatching.
- **message\_id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The message ID that the view is attached to. This is currently used to refresh the view’s state during message update events. If not given then message update events are not propagated for the view.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – A view was not passed.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The view is not persistent or is already finished. A persistent view has no timeout and all their components have an explicitly provided custom\_id.

</dd></dl></dd>
</dl><dl><dt>*property*allowed_mentions<a href="#discord.ext.commands.Bot.allowed_mentions" title="Permalink to this definition">¶</a></dt>
<dd>

The allowed mention configuration.

New in version 1.4.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AllowedMentions" title="discord.AllowedMentions"><code>AllowedMentions</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*application<a href="#discord.ext.commands.Bot.application" title="Permalink to this definition">¶</a></dt>
<dd>

The client’s application info.

This is retrieved on <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client.login" title="discord.Client.login"><code>login()</code></a> and is not updated afterwards. This allows populating the application\_id without requiring a gateway connection.

This is <code>None</code> if accessed before <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client.login" title="discord.Client.login"><code>login()</code></a> is called.

See also

The <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client.application_info" title="discord.Client.application_info"><code>application_info()</code></a> API call

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AppInfo" title="discord.AppInfo"><code>AppInfo</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*application_flags<a href="#discord.ext.commands.Bot.application_flags" title="Permalink to this definition">¶</a></dt>
<dd>

The client’s application flags.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ApplicationFlags" title="discord.ApplicationFlags"><code>ApplicationFlags</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*application_id<a href="#discord.ext.commands.Bot.application_id" title="Permalink to this definition">¶</a></dt>
<dd>

The client’s application ID.

If this is not passed via <code>__init__</code> then this is retrieved through the gateway when an event contains the data or after a call to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client.login" title="discord.Client.login"><code>login()</code></a>. Usually after <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.on_connect" title="discord.on_connect"><code>on_connect()</code></a> is called.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* application_info()<a href="#discord.ext.commands.Bot.application_info" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves the bot’s application information.

<dl><dt>Raises</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the information failed somehow.

</dd><dt>Returns</dt>
<dd>

The bot’s application information.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AppInfo" title="discord.AppInfo"><code>AppInfo</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* before_identify_hook(*shard_id*, ***, *initial=False*)<a href="#discord.ext.commands.Bot.before_identify_hook" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A hook that is called before IDENTIFYing a session. This is useful if you wish to have more control over the synchronization of multiple IDENTIFYing clients.

The default implementation sleeps for 5 seconds.

New in version 1.4.

<dl><dt>Parameters</dt>
<dd>

- **shard\_id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The shard ID that requested being IDENTIFY’d
- **initial** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether this IDENTIFY is the first initial IDENTIFY.

</dd></dl></dd>
</dl><dl><dt>*property*cached_messages<a href="#discord.ext.commands.Bot.cached_messages" title="Permalink to this definition">¶</a></dt>
<dd>

Read-only list of messages the connected client has cached.

New in version 1.1.

<dl><dt>Type</dt>
<dd>

Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* change_presence(***, *activity=None*, *status=None*)<a href="#discord.ext.commands.Bot.change_presence" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Changes the client’s presence.

Example

```
game = discord.Game("with the API")
await client.change_presence(status=discord.Status.idle, activity=game)

```

Changed in version 2.0: Removed the <code>afk</code> keyword-only parameter.

Changed in version 2.0: This function will now raise <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)"><code>TypeError</code></a> instead of <code>InvalidArgument</code>.

<dl><dt>Parameters</dt>
<dd>

- **activity** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.BaseActivity" title="discord.BaseActivity"><code>BaseActivity</code></a>]) – The activity being done. <code>None</code> if no currently active activity is done.
- **status** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Status" title="discord.Status"><code>Status</code></a>]) – Indicates what status to change to. If <code>None</code>, then <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Status.online" title="discord.Status.online"><code>Status.online</code></a> is used.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – If the <code>activity</code> parameter is not the proper type.

</dd></dl></dd>
</dl><dl><dt>clear()<a href="#discord.ext.commands.Bot.clear" title="Permalink to this definition">¶</a></dt>
<dd>

Clears the internal state of the bot.

After this, the bot can be considered “re-opened”, i.e. <a href="#discord.ext.commands.Bot.is_closed" title="discord.ext.commands.Bot.is_closed"><code>is_closed()</code></a> and <a href="#discord.ext.commands.Bot.is_ready" title="discord.ext.commands.Bot.is_ready"><code>is_ready()</code></a> both return <code>False</code> along with the bot’s internal cache cleared.

</dd></dl><dl><dt>*await* close()<a href="#discord.ext.commands.Bot.close" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Closes the connection to Discord.

</dd></dl><dl><dt>*property*cogs<a href="#discord.ext.commands.Bot.cogs" title="Permalink to this definition">¶</a></dt>
<dd>

A read-only mapping of cog name to cog.

<dl><dt>Type</dt>
<dd>

Mapping\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*commands<a href="#discord.ext.commands.Bot.commands" title="Permalink to this definition">¶</a></dt>
<dd>

A unique set of commands without aliases that are registered.

<dl><dt>Type</dt>
<dd>

Set\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* connect(***, *reconnect=True*)<a href="#discord.ext.commands.Bot.connect" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Creates a websocket connection and lets the websocket listen to messages from Discord. This is a loop that runs the entire event system and miscellaneous aspects of the library. Control is not resumed until the WebSocket connection is terminated.

<dl><dt>Parameters</dt>
<dd>

**reconnect** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If we should attempt reconnecting, either due to internet failure or a specific failure on Discord’s part. Certain disconnects that lead to bad state will not be handled (such as invalid sharding payloads or bad tokens).

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.GatewayNotFound" title="discord.GatewayNotFound">**GatewayNotFound**</a> – If the gateway to connect to Discord is not found. Usually if this is thrown then there is a Discord API outage.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ConnectionClosed" title="discord.ConnectionClosed">**ConnectionClosed**</a> – The websocket connection has been terminated.

</dd></dl></dd>
</dl><dl><dt>*await* create_application_emoji(***, *name*, *image*)<a href="#discord.ext.commands.Bot.create_application_emoji" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Create an emoji for the current application.

New in version 2.5.

<dl><dt>Parameters</dt>
<dd>

- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The emoji name. Must be between 2 and 32 characters long.
- **image** (<a href="https://docs.python.org/3/library/stdtypes.html#bytes" title="(in Python v3.14)"><code>bytes</code></a>) – The <a href="https://docs.python.org/3/glossary.html#term-bytes-like-object" title="(in Python v3.14)">bytes-like object</a> representing the image data to use. Only JPG, PNG and GIF images are supported.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The application ID could not be found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Creating the emoji failed.

</dd><dt>Returns</dt>
<dd>

The emoji that was created.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* create_dm(*user*)<a href="#discord.ext.commands.Bot.create_dm" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Creates a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.DMChannel" title="discord.DMChannel"><code>DMChannel</code></a> with this user.

This should be rarely called, as this is done transparently for most people.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

**user** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>) – The user to create a DM with.

</dd><dt>Returns</dt>
<dd>

The channel that was created.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.DMChannel" title="discord.DMChannel"><code>DMChannel</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* create_entitlement(*sku*, *owner*, *owner_type*)<a href="#discord.ext.commands.Bot.create_entitlement" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Creates a test <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Entitlement" title="discord.Entitlement"><code>Entitlement</code></a> for the application.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

- **sku** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>) – The SKU to create the entitlement for.
- **owner** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>) – The ID of the owner.
- **owner\_type** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.EntitlementOwnerType" title="discord.EntitlementOwnerType"><code>EntitlementOwnerType</code></a>) – The type of the owner.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The application ID could not be found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The SKU or owner could not be found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Creating the entitlement failed.

</dd></dl></dd>
</dl><dl><dt>*await* create_guild(***, *name*, *icon=...*, *code=...*)<a href="#discord.ext.commands.Bot.create_guild" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Creates a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>.

Bot accounts in more than 10 guilds are not allowed to create guilds.

Changed in version 2.0: <code>name</code> and <code>icon</code> parameters are now keyword-only. The <code>region</code> parameter has been removed.

Changed in version 2.0: This function will now raise <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)"><code>ValueError</code></a> instead of <code>InvalidArgument</code>.

Deprecated since version 2.6: This function is deprecated and will be removed in a future version.

<dl><dt>Parameters</dt>
<dd>

- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the guild.
- **icon** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#bytes" title="(in Python v3.14)"><code>bytes</code></a>]) – The <a href="https://docs.python.org/3/glossary.html#term-bytes-like-object" title="(in Python v3.14)">bytes-like object</a> representing the icon. See <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientUser.edit" title="discord.ClientUser.edit"><code>ClientUser.edit()</code></a> for more details on what is expected.
- **code** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) –

  The code for a template to create the guild with.

  New in version 1.4.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Guild creation failed.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – Invalid icon image format given. Must be PNG or JPG.

</dd><dt>Returns</dt>
<dd>

The guild created. This is not the same guild that is added to cache.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* delete_invite(*invite*, */*, ***, *reason=None*)<a href="#discord.ext.commands.Bot.delete_invite" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Revokes an <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Invite" title="discord.Invite"><code>Invite</code></a>, URL, or ID to an invite.

You must have <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.manage_channels" title="discord.Permissions.manage_channels"><code>manage_channels</code></a> in the associated guild to do this.

Changed in version 2.0: <code>invite</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **invite** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Invite" title="discord.Invite"><code>Invite</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The invite to revoke.
- **reason** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The reason for deleting the invite. Shows up on the audit log.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have permissions to revoke invites.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The invite is invalid or expired.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Revoking the invite failed.

</dd></dl></dd>
</dl><dl><dt>*property*emojis<a href="#discord.ext.commands.Bot.emojis" title="Permalink to this definition">¶</a></dt>
<dd>

The emojis that the connected client has.

Note

This does not include the emojis that are owned by the application. Use <a href="#discord.ext.commands.Bot.fetch_application_emoji" title="discord.ext.commands.Bot.fetch_application_emoji"><code>fetch_application_emoji()</code></a> to get those.

<dl><dt>Type</dt>
<dd>

Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>]

</dd></dl></dd>
</dl><dl><dt>*async for ... in* entitlements(***, *limit=100*, *before=None*, *after=None*, *skus=None*, *user=None*, *guild=None*, *exclude_ended=False*, *exclude_deleted=True*)<a href="#discord.ext.commands.Bot.entitlements" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves an <a href="https://docs.python.org/3/glossary.html#term-asynchronous-iterator" title="(in Python v3.14)">asynchronous iterator</a> of the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Entitlement" title="discord.Entitlement"><code>Entitlement</code></a> that applications has.

New in version 2.4.

Examples

Usage

```
async for entitlement in client.entitlements(limit=100):
    print(entitlement.user_id, entitlement.ends_at)

```

Flattening into a list

```
entitlements = [entitlement async for entitlement in client.entitlements(limit=100)]
# entitlements is now a list of Entitlement...

```

All parameters are optional.

<dl><dt>Parameters</dt>
<dd>

- **limit** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The number of entitlements to retrieve. If <code>None</code>, it retrieves every entitlement for this application. Note, however, that this would make it a slow operation. Defaults to <code>100</code>.
- **before** (Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>, <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>]]) – Retrieve entitlements before this date or entitlement. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
- **after** (Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>, <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>]]) – Retrieve entitlements after this date or entitlement. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
- **skus** (Optional\[Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]]) – A list of SKUs to filter by.
- **user** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – The user to filter by.
- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) – The guild to filter by.
- **exclude\_ended** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to exclude ended entitlements. Defaults to <code>False</code>.
- **exclude\_deleted** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether to exclude deleted entitlements. Defaults to <code>True</code>.

  New in version 2.5.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The application ID could not be found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Fetching the entitlements failed.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – Both <code>after</code> and <code>before</code> were provided, as Discord does not support this type of pagination.

</dd><dt>Yields</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Entitlement" title="discord.Entitlement"><code>Entitlement</code></a> – The entitlement with the application.

</dd></dl></dd>
</dl><dl><dt>*property*extensions<a href="#discord.ext.commands.Bot.extensions" title="Permalink to this definition">¶</a></dt>
<dd>

A read-only mapping of extension name to extension.

<dl><dt>Type</dt>
<dd>

Mapping\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/types.html#types.ModuleType" title="(in Python v3.14)"><code>types.ModuleType</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* fetch_application_emoji(*emoji_id*, */*)<a href="#discord.ext.commands.Bot.fetch_application_emoji" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves an emoji for the current application.

New in version 2.5.

<dl><dt>Parameters</dt>
<dd>

**emoji\_id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The emoji ID to retrieve.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The application ID could not be found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the emoji failed.

</dd><dt>Returns</dt>
<dd>

The emoji requested.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_application_emojis()<a href="#discord.ext.commands.Bot.fetch_application_emojis" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves all emojis for the current application.

New in version 2.5.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The application ID could not be found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the emojis failed.

</dd><dt>Returns</dt>
<dd>

The list of emojis for the current application.

</dd><dt>Return type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* fetch_channel(*channel_id*, */*)<a href="#discord.ext.commands.Bot.fetch_channel" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.PrivateChannel" title="discord.abc.PrivateChannel"><code>abc.PrivateChannel</code></a>, or <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a> with the specified ID.

Note

This method is an API call. For general usage, consider <a href="#discord.ext.commands.Bot.get_channel" title="discord.ext.commands.Bot.get_channel"><code>get_channel()</code></a> instead.

New in version 1.2.

Changed in version 2.0: <code>channel_id</code> parameter is now positional-only.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.InvalidData" title="discord.InvalidData">**InvalidData**</a> – An unknown channel type was received from Discord.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the channel failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – Invalid Channel ID.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have permission to fetch this channel.

</dd><dt>Returns</dt>
<dd>

The channel from the ID.

</dd><dt>Return type</dt>
<dd>

Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.PrivateChannel" title="discord.abc.PrivateChannel"><code>abc.PrivateChannel</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* fetch_entitlement(*entitlement_id*, */*)<a href="#discord.ext.commands.Bot.fetch_entitlement" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Entitlement" title="discord.Entitlement"><code>Entitlement</code></a> with the specified ID.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**entitlement\_id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The entitlement’s ID to fetch from.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – An entitlement with this ID does not exist.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The application ID could not be found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Fetching the entitlement failed.

</dd><dt>Returns</dt>
<dd>

The entitlement you requested.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Entitlement" title="discord.Entitlement"><code>Entitlement</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_guild(*guild_id*, */*, ***, *with_counts=True*)<a href="#discord.ext.commands.Bot.fetch_guild" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a> from an ID.

Note

Using this, you will **not** receive <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.channels" title="discord.Guild.channels"><code>Guild.channels</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.members" title="discord.Guild.members"><code>Guild.members</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member.activity" title="discord.Member.activity"><code>Member.activity</code></a> and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member.voice" title="discord.Member.voice"><code>Member.voice</code></a> per <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a>.

Note

This method is an API call. For general usage, consider <a href="#discord.ext.commands.Bot.get_guild" title="discord.ext.commands.Bot.get_guild"><code>get_guild()</code></a> instead.

Changed in version 2.0: <code>guild_id</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **guild\_id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The guild’s ID to fetch from.
- **with\_counts** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether to include count information in the guild. This fills the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.approximate_member_count" title="discord.Guild.approximate_member_count"><code>Guild.approximate_member_count</code></a> and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.approximate_presence_count" title="discord.Guild.approximate_presence_count"><code>Guild.approximate_presence_count</code></a> attributes without needing any privileged intents. Defaults to <code>True</code>.

  New in version 2.0.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The guild doesn’t exist or you got no access to it.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Getting the guild failed.

</dd><dt>Returns</dt>
<dd>

The guild from the ID.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_guild_preview(*guild_id*)<a href="#discord.ext.commands.Bot.fetch_guild_preview" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves a preview of a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a> from an ID. If the guild is discoverable, you don’t have to be a member of it.

New in version 2.5.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The guild doesn’t exist, or is not discoverable and you are not in it.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Getting the guild failed.

</dd><dt>Returns</dt>
<dd>

The guild preview from the ID.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.GuildPreview" title="discord.GuildPreview"><code>GuildPreview</code></a>

</dd></dl></dd>
</dl><dl><dt>*async for ... in* fetch_guilds(***, *limit=200*, *before=None*, *after=None*, *with_counts=True*)<a href="#discord.ext.commands.Bot.fetch_guilds" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves an <a href="https://docs.python.org/3/glossary.html#term-asynchronous-iterator" title="(in Python v3.14)">asynchronous iterator</a> that enables receiving your guilds.

Note

Using this, you will only receive <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.owner" title="discord.Guild.owner"><code>Guild.owner</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.icon" title="discord.Guild.icon"><code>Guild.icon</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.id" title="discord.Guild.id"><code>Guild.id</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.name" title="discord.Guild.name"><code>Guild.name</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.approximate_member_count" title="discord.Guild.approximate_member_count"><code>Guild.approximate_member_count</code></a>, and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.approximate_presence_count" title="discord.Guild.approximate_presence_count"><code>Guild.approximate_presence_count</code></a> per <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>.

Note

This method is an API call. For general usage, consider <a href="#discord.ext.commands.Bot.guilds" title="discord.ext.commands.Bot.guilds"><code>guilds</code></a> instead.

Examples

Usage

```
async for guild in client.fetch_guilds(limit=150):
    print(guild.name)

```

Flattening into a list

```
guilds = [guild async for guild in client.fetch_guilds(limit=150)]
# guilds is now a list of Guild...

```

All parameters are optional.

<dl><dt>Parameters</dt>
<dd>

- **limit** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The number of guilds to retrieve. If <code>None</code>, it retrieves every guild you have access to. Note, however, that this would make it a slow operation. Defaults to <code>200</code>.

  Changed in version 2.0: The default has been changed to 200.
- **before** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>abc.Snowflake</code></a>, <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>]) – Retrieves guilds before this date or object. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
- **after** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>abc.Snowflake</code></a>, <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>]) – Retrieve guilds after this date or object. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
- **with\_counts** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether to include count information in the guilds. This fills the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.approximate_member_count" title="discord.Guild.approximate_member_count"><code>Guild.approximate_member_count</code></a> and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.approximate_presence_count" title="discord.Guild.approximate_presence_count"><code>Guild.approximate_presence_count</code></a> attributes without needing any privileged intents. Defaults to <code>True</code>.

  New in version 2.3.

</dd><dt>Raises</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Getting the guilds failed.

</dd><dt>Yields</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a> – The guild with the guild data parsed.

</dd></dl></dd>
</dl><dl><dt>*await* fetch_invite(*url*, ***, *with_counts=True*, *with_expiration=True*, *scheduled_event_id=None*)<a href="#discord.ext.commands.Bot.fetch_invite" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Gets an <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Invite" title="discord.Invite"><code>Invite</code></a> from a discord.gg URL or ID.

Note

If the invite is for a guild you have not joined, the guild and channel attributes of the returned <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Invite" title="discord.Invite"><code>Invite</code></a> will be <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialInviteGuild" title="discord.PartialInviteGuild"><code>PartialInviteGuild</code></a> and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialInviteChannel" title="discord.PartialInviteChannel"><code>PartialInviteChannel</code></a> respectively.

<dl><dt>Parameters</dt>
<dd>

- **url** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Invite" title="discord.Invite"><code>Invite</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The Discord invite ID or URL (must be a discord.gg URL).
- **with\_counts** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to include count information in the invite. This fills the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Invite.approximate_member_count" title="discord.Invite.approximate_member_count"><code>Invite.approximate_member_count</code></a> and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Invite.approximate_presence_count" title="discord.Invite.approximate_presence_count"><code>Invite.approximate_presence_count</code></a> fields.
- **with\_expiration** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether to include the expiration date of the invite. This fills the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Invite.expires_at" title="discord.Invite.expires_at"><code>Invite.expires_at</code></a> field.

  New in version 2.0.

  Deprecated since version 2.6: This parameter is deprecated and will be removed in a future version as it is no longer needed to fill the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Invite.expires_at" title="discord.Invite.expires_at"><code>Invite.expires_at</code></a> field.
- **scheduled\_event\_id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The ID of the scheduled event this invite is for.

  Note

  It is not possible to provide a url that contains an <code>event_id</code> parameter when using this parameter.

  New in version 2.0.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The url contains an <code>event_id</code>, but <code>scheduled_event_id</code> has also been provided.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The invite has expired or is invalid.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Getting the invite failed.

</dd><dt>Returns</dt>
<dd>

The invite from the URL/ID.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Invite" title="discord.Invite"><code>Invite</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_premium_sticker_pack(*sticker_pack_id*, */*)<a href="#discord.ext.commands.Bot.fetch_premium_sticker_pack" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves a premium sticker pack with the specified ID.

New in version 2.5.

<dl><dt>Parameters</dt>
<dd>

**sticker\_pack\_id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The sticker pack’s ID to fetch from.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – A sticker pack with this ID does not exist.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the sticker pack failed.

</dd><dt>Returns</dt>
<dd>

The retrieved premium sticker pack.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.StickerPack" title="discord.StickerPack"><code>StickerPack</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_premium_sticker_packs()<a href="#discord.ext.commands.Bot.fetch_premium_sticker_packs" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves all available premium sticker packs.

New in version 2.0.

<dl><dt>Raises</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the sticker packs failed.

</dd><dt>Returns</dt>
<dd>

All available premium sticker packs.

</dd><dt>Return type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.StickerPack" title="discord.StickerPack"><code>StickerPack</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* fetch_skus()<a href="#discord.ext.commands.Bot.fetch_skus" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves the bot’s available SKUs.

New in version 2.4.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MissingApplicationID" title="discord.MissingApplicationID">**MissingApplicationID**</a> – The application ID could not be found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the SKUs failed.

</dd><dt>Returns</dt>
<dd>

The bot’s available SKUs.

</dd><dt>Return type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.SKU" title="discord.SKU"><code>SKU</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* fetch_soundboard_default_sounds()<a href="#discord.ext.commands.Bot.fetch_soundboard_default_sounds" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves all default soundboard sounds.

New in version 2.5.

<dl><dt>Raises</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the default soundboard sounds failed.

</dd><dt>Returns</dt>
<dd>

All default soundboard sounds.

</dd><dt>Return type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.SoundboardDefaultSound" title="discord.SoundboardDefaultSound"><code>SoundboardDefaultSound</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* fetch_stage_instance(*channel_id*, */*)<a href="#discord.ext.commands.Bot.fetch_stage_instance" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Gets a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.StageInstance" title="discord.StageInstance"><code>StageInstance</code></a> for a stage channel id.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

**channel\_id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The stage channel ID.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The stage instance or channel could not be found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Getting the stage instance failed.

</dd><dt>Returns</dt>
<dd>

The stage instance from the stage channel ID.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.StageInstance" title="discord.StageInstance"><code>StageInstance</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_sticker(*sticker_id*, */*)<a href="#discord.ext.commands.Bot.fetch_sticker" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Sticker" title="discord.Sticker"><code>Sticker</code></a> with the specified ID.

New in version 2.0.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the sticker failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – Invalid sticker ID.

</dd><dt>Returns</dt>
<dd>

The sticker you requested.

</dd><dt>Return type</dt>
<dd>

Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.StandardSticker" title="discord.StandardSticker"><code>StandardSticker</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.GuildSticker" title="discord.GuildSticker"><code>GuildSticker</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* fetch_template(*code*)<a href="#discord.ext.commands.Bot.fetch_template" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Gets a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Template" title="discord.Template"><code>Template</code></a> from a discord.new URL or code.

<dl><dt>Parameters</dt>
<dd>

**code** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Template" title="discord.Template"><code>Template</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The Discord Template Code or URL (must be a discord.new URL).

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The template is invalid.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Getting the template failed.

</dd><dt>Returns</dt>
<dd>

The template from the URL/code.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Template" title="discord.Template"><code>Template</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_user(*user_id*, */*)<a href="#discord.ext.commands.Bot.fetch_user" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a> based on their ID. You do not have to share any guilds with the user to get this information, however many operations do require that you do.

Note

This method is an API call. If you have <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Intents.members" title="discord.Intents.members"><code>discord.Intents.members</code></a> and member cache enabled, consider <a href="#discord.ext.commands.Bot.get_user" title="discord.ext.commands.Bot.get_user"><code>get_user()</code></a> instead.

Changed in version 2.0: <code>user_id</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**user\_id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The user’s ID to fetch from.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – A user with this ID does not exist.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Fetching the user failed.

</dd><dt>Returns</dt>
<dd>

The user you requested.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_webhook(*webhook_id*, */*)<a href="#discord.ext.commands.Bot.fetch_webhook" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Webhook" title="discord.Webhook"><code>Webhook</code></a> with the specified ID.

Changed in version 2.0: <code>webhook_id</code> parameter is now positional-only.

<dl><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the webhook failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – Invalid webhook ID.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have permission to fetch this webhook.

</dd><dt>Returns</dt>
<dd>

The webhook you requested.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Webhook" title="discord.Webhook"><code>Webhook</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* fetch_widget(*guild_id*, */*)<a href="#discord.ext.commands.Bot.fetch_widget" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Gets a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Widget" title="discord.Widget"><code>Widget</code></a> from a guild ID.

Note

The guild must have the widget enabled to get this information.

Changed in version 2.0: <code>guild_id</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**guild\_id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID of the guild.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – The widget for this guild is disabled.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the widget failed.

</dd><dt>Returns</dt>
<dd>

The guild’s widget.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Widget" title="discord.Widget"><code>Widget</code></a>

</dd></dl></dd>
</dl><dl><dt>*for ... in* get_all_channels()<a href="#discord.ext.commands.Bot.get_all_channels" title="Permalink to this definition">¶</a></dt>
<dd>

A generator that retrieves every <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a> the client can ‘access’.

This is equivalent to:

```
for guild in client.guilds:
    for channel in guild.channels:
        yield channel

```

Note

Just because you receive a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a> does not mean that you can communicate in said channel. <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel.permissions_for" title="discord.abc.GuildChannel.permissions_for"><code>abc.GuildChannel.permissions_for()</code></a> should be used for that.

<dl><dt>Yields</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a> – A channel the client can ‘access’.

</dd></dl></dd>
</dl><dl><dt>*for ... in* get_all_members()<a href="#discord.ext.commands.Bot.get_all_members" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a generator with every <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a> the client can see.

This is equivalent to:

```
for guild in client.guilds:
    for member in guild.members:
        yield member

```

<dl><dt>Yields</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a> – A member the client can see.

</dd></dl></dd>
</dl><dl><dt>get_channel(*id*, */*)<a href="#discord.ext.commands.Bot.get_channel" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a channel or thread with the given ID.

Changed in version 2.0: <code>id</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID to search for.

</dd><dt>Returns</dt>
<dd>

The returned channel or <code>None</code> if not found.

</dd><dt>Return type</dt>
<dd>

Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.PrivateChannel" title="discord.abc.PrivateChannel"><code>abc.PrivateChannel</code></a>]]

</dd></dl></dd>
</dl><dl><dt>get_cog(*name*, */*)<a href="#discord.ext.commands.Bot.get_cog" title="Permalink to this definition">¶</a></dt>
<dd>

Gets the cog instance requested.

If the cog is not found, <code>None</code> is returned instead.

Changed in version 2.0: <code>name</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the cog you are requesting. This is equivalent to the name passed via keyword argument in class creation or the class name if unspecified.

</dd><dt>Returns</dt>
<dd>

The cog that was requested. If not found, returns <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_command(*name*, */*)<a href="#discord.ext.commands.Bot.get_command" title="Permalink to this definition">¶</a></dt>
<dd>

Get a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> from the internal list of commands.

This could also be used as a way to get aliases.

The name could be fully qualified (e.g. <code>'foo bar'</code>) will get the subcommand <code>bar</code> of the group command <code>foo</code>. If a subcommand is not found then <code>None</code> is returned just as usual.

Changed in version 2.0: <code>name</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the command to get.

</dd><dt>Returns</dt>
<dd>

The command that was requested. If not found, returns <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* get_context(*origin*, */*, ***, *cls=...*)<a href="#discord.ext.commands.Bot.get_context" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Returns the invocation context from the message or interaction.

This is a more low-level counter-part for <a href="#discord.ext.commands.Bot.process_commands" title="discord.ext.commands.Bot.process_commands"><code>process_commands()</code></a> to allow users more fine grained control over the processing.

The returned context is not guaranteed to be a valid invocation context, <a href="#discord.ext.commands.Context.valid" title="discord.ext.commands.Context.valid"><code>Context.valid</code></a> must be checked to make sure it is. If the context is not valid then it is not a valid candidate to be invoked under <a href="#discord.ext.commands.Bot.invoke" title="discord.ext.commands.Bot.invoke"><code>invoke()</code></a>.

Note

In order for the custom context to be used inside an interaction-based context (such as <a href="#discord.ext.commands.HybridCommand" title="discord.ext.commands.HybridCommand"><code>HybridCommand</code></a>) then this method must be overridden to return that class.

Changed in version 2.0: <code>message</code> parameter is now positional-only and renamed to <code>origin</code>.

<dl><dt>Parameters</dt>
<dd>

- **origin** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>discord.Message</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a>]) – The message or interaction to get the invocation context from.
- **cls** – The factory class that will be used to create the context. By default, this is <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>. Should a custom class be provided, it must be similar enough to <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>'s interface.

</dd><dt>Returns</dt>
<dd>

The invocation context. The type of this can change via the <code>cls</code> parameter.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>

</dd></dl></dd>
</dl><dl><dt>get_emoji(*id*, */*)<a href="#discord.ext.commands.Bot.get_emoji" title="Permalink to this definition">¶</a></dt>
<dd>

Returns an emoji with the given ID.

Changed in version 2.0: <code>id</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID to search for.

</dd><dt>Returns</dt>
<dd>

The custom emoji or <code>None</code> if not found.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_guild(*id*, */*)<a href="#discord.ext.commands.Bot.get_guild" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a guild with the given ID.

Changed in version 2.0: <code>id</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID to search for.

</dd><dt>Returns</dt>
<dd>

The guild or <code>None</code> if not found.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_partial_messageable(*id*, ***, *guild_id=None*, *type=None*)<a href="#discord.ext.commands.Bot.get_partial_messageable" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a partial messageable with the given channel ID.

This is useful if you have a channel\_id but don’t want to do an API call to send messages to it.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The channel ID to create a partial messageable for.
- **guild\_id** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) –

  The optional guild ID to create a partial messageable for.

  This is not required to actually send messages, but it does allow the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialMessageable.jump_url" title="discord.PartialMessageable.jump_url"><code>jump_url()</code></a> and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialMessageable.guild" title="discord.PartialMessageable.guild"><code>guild</code></a> properties to function properly.
- **type** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ChannelType" title="discord.ChannelType"><code>ChannelType</code></a>]) – The underlying channel type for the partial messageable.

</dd><dt>Returns</dt>
<dd>

The partial messageable

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialMessageable" title="discord.PartialMessageable"><code>PartialMessageable</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* get_prefix(*message*, */*)<a href="#discord.ext.commands.Bot.get_prefix" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves the prefix the bot is listening to with the message as a context.

Changed in version 2.0: <code>message</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**message** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>discord.Message</code></a>) – The message context to get the prefix of.

</dd><dt>Returns</dt>
<dd>

A list of prefixes or a single prefix that the bot is listening for.

</dd><dt>Return type</dt>
<dd>

Union\[List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>], <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_soundboard_sound(*id*, */*)<a href="#discord.ext.commands.Bot.get_soundboard_sound" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a soundboard sound with the given ID.

New in version 2.5.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID to search for.

</dd><dt>Returns</dt>
<dd>

The soundboard sound or <code>None</code> if not found.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.SoundboardSound" title="discord.SoundboardSound"><code>SoundboardSound</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_stage_instance(*id*, */*)<a href="#discord.ext.commands.Bot.get_stage_instance" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a stage instance with the given stage channel ID.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID to search for.

</dd><dt>Returns</dt>
<dd>

The stage instance or <code>None</code> if not found.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.StageInstance" title="discord.StageInstance"><code>StageInstance</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_sticker(*id*, */*)<a href="#discord.ext.commands.Bot.get_sticker" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a guild sticker with the given ID.

New in version 2.0.

Note

To retrieve standard stickers, use <a href="#discord.ext.commands.Bot.fetch_sticker" title="discord.ext.commands.Bot.fetch_sticker"><code>fetch_sticker()</code></a>. or <a href="#discord.ext.commands.Bot.fetch_premium_sticker_packs" title="discord.ext.commands.Bot.fetch_premium_sticker_packs"><code>fetch_premium_sticker_packs()</code></a>.

<dl><dt>Returns</dt>
<dd>

The sticker or <code>None</code> if not found.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.GuildSticker" title="discord.GuildSticker"><code>GuildSticker</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_user(*id*, */*)<a href="#discord.ext.commands.Bot.get_user" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a user with the given ID.

Changed in version 2.0: <code>id</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The ID to search for.

</dd><dt>Returns</dt>
<dd>

The user or <code>None</code> if not found.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*guilds<a href="#discord.ext.commands.Bot.guilds" title="Permalink to this definition">¶</a></dt>
<dd>

The guilds that the connected client is a member of.

<dl><dt>Type</dt>
<dd>

Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*intents<a href="#discord.ext.commands.Bot.intents" title="Permalink to this definition">¶</a></dt>
<dd>

The intents configured for this connection.

New in version 1.5.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Intents" title="discord.Intents"><code>Intents</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* invoke(*ctx*, */*)<a href="#discord.ext.commands.Bot.invoke" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Invokes the command given under the invocation context and handles all the internal event dispatch mechanisms.

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context to invoke.

</dd></dl></dd>
</dl><dl><dt>is_closed()<a href="#discord.ext.commands.Bot.is_closed" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Indicates if the websocket connection is closed.

</dd></dl><dl><dt>*await* is_owner(*user*, */*)<a href="#discord.ext.commands.Bot.is_owner" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Checks if a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a> or <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a> is the owner of this bot.

If an <a href="#discord.ext.commands.Bot.owner_id" title="discord.ext.commands.Bot.owner_id"><code>owner_id</code></a> is not set, it is fetched automatically through the use of <a href="#discord.ext.commands.Bot.application_info" title="discord.ext.commands.Bot.application_info"><code>application_info()</code></a>.

Changed in version 1.3: The function also checks if the application is team-owned if <a href="#discord.ext.commands.Bot.owner_ids" title="discord.ext.commands.Bot.owner_ids"><code>owner_ids</code></a> is not set.

Changed in version 2.0: <code>user</code> parameter is now positional-only.

Changed in version 2.4: This function now respects the team member roles if the bot is team-owned. In order to be considered an owner, they must be either an admin or a developer.

<dl><dt>Parameters</dt>
<dd>

**user** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.User" title="discord.abc.User"><code>abc.User</code></a>) – The user to check for.

</dd><dt>Returns</dt>
<dd>

Whether the user is the owner.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>is_ready()<a href="#discord.ext.commands.Bot.is_ready" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Specifies if the client’s internal cache is ready for use.

</dd></dl><dl><dt>is_ws_ratelimited()<a href="#discord.ext.commands.Bot.is_ws_ratelimited" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Whether the websocket is currently rate limited.

This can be useful to know when deciding whether you should query members using HTTP or via the gateway.

New in version 1.6.

</dd></dl><dl><dt>*property*latency<a href="#discord.ext.commands.Bot.latency" title="Permalink to this definition">¶</a></dt>
<dd>

Measures latency between a HEARTBEAT and a HEARTBEAT\_ACK in seconds.

This could be referred to as the Discord WebSocket protocol latency.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* load_extension(*name*, ***, *package=None*)<a href="#discord.ext.commands.Bot.load_extension" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Loads an extension.

An extension is a python module that contains commands, cogs, or listeners.

An extension must have a global function, <code>setup</code> defined as the entry point on what to do when the extension is loaded. This entry point must have a single argument, the <code>bot</code>.

Changed in version 2.0: This method is now a <a href="https://docs.python.org/3/glossary.html#term-coroutine" title="(in Python v3.14)">coroutine</a>.

<dl><dt>Parameters</dt>
<dd>

- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The extension name to load. It must be dot separated like regular Python imports if accessing a sub-module. e.g. <code>foo.test</code> if you want to import <code>foo/test.py</code>.
- **package** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) –

  The package name to resolve relative imports with. This is required when loading an extension using a relative path, e.g <code>.foo.test</code>. Defaults to <code>None</code>.

  New in version 1.7.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.ExtensionNotFound" title="discord.ext.commands.ExtensionNotFound">**ExtensionNotFound**</a> – The extension could not be imported. This is also raised if the name of the extension could not be resolved using the provided <code>package</code> parameter.
- <a href="#discord.ext.commands.ExtensionAlreadyLoaded" title="discord.ext.commands.ExtensionAlreadyLoaded">**ExtensionAlreadyLoaded**</a> – The extension is already loaded.
- <a href="#discord.ext.commands.NoEntryPointError" title="discord.ext.commands.NoEntryPointError">**NoEntryPointError**</a> – The extension does not have a setup function.
- <a href="#discord.ext.commands.ExtensionFailed" title="discord.ext.commands.ExtensionFailed">**ExtensionFailed**</a> – The extension or its setup function had an execution error.

</dd></dl></dd>
</dl><dl><dt>*await* login(*token*)<a href="#discord.ext.commands.Bot.login" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Logs in the client with the specified credentials and calls the <a href="#discord.ext.commands.Bot.setup_hook" title="discord.ext.commands.Bot.setup_hook"><code>setup_hook()</code></a>.

<dl><dt>Parameters</dt>
<dd>

**token** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The authentication token. Do not prefix this token with anything as the library will do it for you.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.LoginFailure" title="discord.LoginFailure">**LoginFailure**</a> – The wrong credentials are passed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – An unknown HTTP related error occurred, usually when it isn’t 200 or the known incorrect credentials passing status code.

</dd></dl></dd>
</dl><dl><dt>*await* on_command_error(*context*, *exception*, */*)<a href="#discord.ext.commands.Bot.on_command_error" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The default command error handler provided by the bot.

By default this logs to the library logger, however it could be overridden to have a different implementation.

This only fires if you do not specify any listeners for command error.

Changed in version 2.0: <code>context</code> and <code>exception</code> parameters are now positional-only. Instead of writing to <code>sys.stderr</code> this now uses the library logger.

</dd></dl><dl><dt>*await* on_error(*event_method*, */*, **args*, ***kwargs*)<a href="#discord.ext.commands.Bot.on_error" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The default error handler provided by the client.

By default this logs to the library logger however it could be overridden to have a different implementation. Check <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.on_error" title="discord.on_error"><code>on_error()</code></a> for more details.

Changed in version 2.0: <code>event_method</code> parameter is now positional-only and instead of writing to <code>sys.stderr</code> it logs instead.

</dd></dl><dl><dt>*property*persistent_views<a href="#discord.ext.commands.Bot.persistent_views" title="Permalink to this definition">¶</a></dt>
<dd>

A sequence of persistent views added to the client.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Sequence\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.View" title="discord.ui.View"><code>View</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>LayoutView</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*private_channels<a href="#discord.ext.commands.Bot.private_channels" title="Permalink to this definition">¶</a></dt>
<dd>

The private channels that the connected client is participating on.

Note

This returns only up to 128 most recent private channels due to an internal working on how Discord deals with private channels.

<dl><dt>Type</dt>
<dd>

Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.PrivateChannel" title="discord.abc.PrivateChannel"><code>abc.PrivateChannel</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* process_commands(*message*, */*)<a href="#discord.ext.commands.Bot.process_commands" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

This function processes the commands that have been registered to the bot and other groups. Without this coroutine, none of the commands will be triggered.

By default, this coroutine is called inside the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.on_message" title="discord.on_message"><code>on_message()</code></a> event. If you choose to override the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.on_message" title="discord.on_message"><code>on_message()</code></a> event, then you should invoke this coroutine as well.

This is built using other low level tools, and is equivalent to a call to <a href="#discord.ext.commands.Bot.get_context" title="discord.ext.commands.Bot.get_context"><code>get_context()</code></a> followed by a call to <a href="#discord.ext.commands.Bot.invoke" title="discord.ext.commands.Bot.invoke"><code>invoke()</code></a>.

This also checks if the message’s author is a bot and doesn’t call <a href="#discord.ext.commands.Bot.get_context" title="discord.ext.commands.Bot.get_context"><code>get_context()</code></a> or <a href="#discord.ext.commands.Bot.invoke" title="discord.ext.commands.Bot.invoke"><code>invoke()</code></a> if so.

Changed in version 2.0: <code>message</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**message** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>discord.Message</code></a>) – The message to process commands for.

</dd></dl></dd>
</dl><dl><dt>*await* reload_extension(*name*, ***, *package=None*)<a href="#discord.ext.commands.Bot.reload_extension" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Atomically reloads an extension.

This replaces the extension with the same extension, only refreshed. This is equivalent to a <a href="#discord.ext.commands.Bot.unload_extension" title="discord.ext.commands.Bot.unload_extension"><code>unload_extension()</code></a> followed by a <a href="#discord.ext.commands.Bot.load_extension" title="discord.ext.commands.Bot.load_extension"><code>load_extension()</code></a> except done in an atomic way. That is, if an operation fails mid-reload then the bot will roll-back to the prior working state.

<dl><dt>Parameters</dt>
<dd>

- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The extension name to reload. It must be dot separated like regular Python imports if accessing a sub-module. e.g. <code>foo.test</code> if you want to import <code>foo/test.py</code>.
- **package** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) –

  The package name to resolve relative imports with. This is required when reloading an extension using a relative path, e.g <code>.foo.test</code>. Defaults to <code>None</code>.

  New in version 1.7.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.ExtensionNotLoaded" title="discord.ext.commands.ExtensionNotLoaded">**ExtensionNotLoaded**</a> – The extension was not loaded.
- <a href="#discord.ext.commands.ExtensionNotFound" title="discord.ext.commands.ExtensionNotFound">**ExtensionNotFound**</a> – The extension could not be imported. This is also raised if the name of the extension could not be resolved using the provided <code>package</code> parameter.
- <a href="#discord.ext.commands.NoEntryPointError" title="discord.ext.commands.NoEntryPointError">**NoEntryPointError**</a> – The extension does not have a setup function.
- <a href="#discord.ext.commands.ExtensionFailed" title="discord.ext.commands.ExtensionFailed">**ExtensionFailed**</a> – The extension setup function had an execution error.

</dd></dl></dd>
</dl><dl><dt>remove_check(*func*, */*, ***, *call_once=False*)<a href="#discord.ext.commands.Bot.remove_check" title="Permalink to this definition">¶</a></dt>
<dd>

Removes a global check from the bot.

This function is idempotent and will not raise an exception if the function is not in the global checks.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **func** – The function to remove from the global checks.
- **call\_once** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If the function was added with <code>call_once=True</code> in the <a href="#discord.ext.commands.Bot.add_check" title="discord.ext.commands.Bot.add_check"><code>Bot.add_check()</code></a> call or using <a href="#discord.ext.commands.Bot.check_once" title="discord.ext.commands.Bot.check_once"><code>check_once()</code></a>.

</dd></dl></dd>
</dl><dl><dt>*await* remove_cog(*name*, */*, ***, *guild=...*, *guilds=...*)<a href="#discord.ext.commands.Bot.remove_cog" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Removes a cog from the bot and returns it.

All registered commands and event listeners that the cog has registered will be removed as well.

If no cog is found then this method has no effect.

Changed in version 2.0: <code>name</code> parameter is now positional-only.

Changed in version 2.0: This method is now a <a href="https://docs.python.org/3/glossary.html#term-coroutine" title="(in Python v3.14)">coroutine</a>.

<dl><dt>Parameters</dt>
<dd>

- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the cog to remove.
- **guild** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  If the cog is an application command group, then this would be the guild where the cog group would be removed from. If not given then a global command is removed instead instead.

  New in version 2.0.
- **guilds** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>]) –

  If the cog is an application command group, then this would be the guilds where the cog group would be removed from. If not given then a global command is removed instead instead. Cannot be mixed with <code>guild</code>.

  New in version 2.0.

</dd><dt>Returns</dt>
<dd>

The cog that was removed. <code>None</code> if not found.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>]

</dd></dl></dd>
</dl><dl><dt>remove_command(*name*, */*)<a href="#discord.ext.commands.Bot.remove_command" title="Permalink to this definition">¶</a></dt>
<dd>

Remove a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> from the internal list of commands.

This could also be used as a way to remove aliases.

Changed in version 2.0: <code>name</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the command to remove.

</dd><dt>Returns</dt>
<dd>

The command that was removed. If the name is not valid then <code>None</code> is returned instead.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>remove_dynamic_items(**items*)<a href="#discord.ext.commands.Bot.remove_dynamic_items" title="Permalink to this definition">¶</a></dt>
<dd>

Removes <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a> classes from persistent listening.

This method accepts *class types* rather than instances.

New in version 2.4.

<dl><dt>Parameters</dt>
<dd>

**\*items** (Type\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a>]) – The classes of dynamic items to remove.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – A class is not a subclass of <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.DynamicItem" title="discord.ui.DynamicItem"><code>DynamicItem</code></a>.

</dd></dl></dd>
</dl><dl><dt>remove_listener(*func*, */*, *name=...*)<a href="#discord.ext.commands.Bot.remove_listener" title="Permalink to this definition">¶</a></dt>
<dd>

Removes a listener from the pool of listeners.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **func** – The function that was used as a listener to remove.
- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the event we want to remove. Defaults to <code>func.__name__</code>.

</dd></dl></dd>
</dl><dl><dt>run(*token*, ***, *reconnect=True*, *log_handler=...*, *log_formatter=...*, *log_level=...*, *root_logger=False*)<a href="#discord.ext.commands.Bot.run" title="Permalink to this definition">¶</a></dt>
<dd>

A blocking call that abstracts away the event loop initialisation from you.

If you want more control over the event loop then this function should not be used. Use <a href="#discord.ext.commands.Bot.start" title="discord.ext.commands.Bot.start"><code>start()</code></a> coroutine or <a href="#discord.ext.commands.Bot.connect" title="discord.ext.commands.Bot.connect"><code>connect()</code></a> + <a href="#discord.ext.commands.Bot.login" title="discord.ext.commands.Bot.login"><code>login()</code></a>.

This function also sets up the logging library to make it easier for beginners to know what is going on with the library. For more advanced users, this can be disabled by passing <code>None</code> to the <code>log_handler</code> parameter.

Warning

This function must be the last function to call due to the fact that it is blocking. That means that registration of events or anything being called after this function call will not execute until it returns.

<dl><dt>Parameters</dt>
<dd>

- **token** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The authentication token. Do not prefix this token with anything as the library will do it for you.
- **reconnect** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If we should attempt reconnecting, either due to internet failure or a specific failure on Discord’s part. Certain disconnects that lead to bad state will not be handled (such as invalid sharding payloads or bad tokens).
- **log\_handler** (Optional\[<a href="https://docs.python.org/3/library/logging.html#logging.Handler" title="(in Python v3.14)"><code>logging.Handler</code></a>]) –

  The log handler to use for the library’s logger. If this is <code>None</code> then the library will not set up anything logging related. Logging will still work if <code>None</code> is passed, though it is your responsibility to set it up.

  The default log handler if not provided is <a href="https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler" title="(in Python v3.14)"><code>logging.StreamHandler</code></a>.

  New in version 2.0.
- **log\_formatter** (<a href="https://docs.python.org/3/library/logging.html#logging.Formatter" title="(in Python v3.14)"><code>logging.Formatter</code></a>) –

  The formatter to use with the given log handler. If not provided then it defaults to a colour based logging formatter (if available).

  New in version 2.0.
- **log\_level** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) –

  The default log level for the library’s logger. This is only applied if the <code>log_handler</code> parameter is not <code>None</code>. Defaults to <code>logging.INFO</code>.

  New in version 2.0.
- **root\_logger** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether to set up the root logger rather than the library logger. By default, only the library logger (<code>'discord'</code>) is set up. If this is set to <code>True</code> then the root logger is set up as well.

  Defaults to <code>False</code>.

  New in version 2.0.

</dd></dl></dd>
</dl><dl><dt>*await* setup_hook()<a href="#discord.ext.commands.Bot.setup_hook" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A coroutine to be called to setup the bot, by default this is blank.

To perform asynchronous setup after the bot is logged in but before it has connected to the Websocket, overwrite this coroutine.

This is only called once, in <a href="#discord.ext.commands.Bot.login" title="discord.ext.commands.Bot.login"><code>login()</code></a>, and will be called before any events are dispatched, making it a better solution than doing such setup in the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.on_ready" title="discord.on_ready"><code>on_ready()</code></a> event.

Warning

Since this is called *before* the websocket connection is made therefore anything that waits for the websocket will deadlock, this includes things like <a href="#discord.ext.commands.Bot.wait_for" title="discord.ext.commands.Bot.wait_for"><code>wait_for()</code></a> and <a href="#discord.ext.commands.Bot.wait_until_ready" title="discord.ext.commands.Bot.wait_until_ready"><code>wait_until_ready()</code></a>.

New in version 2.0.

</dd></dl><dl><dt>*property*soundboard_sounds<a href="#discord.ext.commands.Bot.soundboard_sounds" title="Permalink to this definition">¶</a></dt>
<dd>

The soundboard sounds that the connected client has.

New in version 2.5.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.SoundboardSound" title="discord.SoundboardSound"><code>SoundboardSound</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* start(*token*, ***, *reconnect=True*)<a href="#discord.ext.commands.Bot.start" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A shorthand coroutine for <a href="#discord.ext.commands.Bot.login" title="discord.ext.commands.Bot.login"><code>login()</code></a> + <a href="#discord.ext.commands.Bot.connect" title="discord.ext.commands.Bot.connect"><code>connect()</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **token** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The authentication token. Do not prefix this token with anything as the library will do it for you.
- **reconnect** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – If we should attempt reconnecting, either due to internet failure or a specific failure on Discord’s part. Certain disconnects that lead to bad state will not be handled (such as invalid sharding payloads or bad tokens).

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – An unexpected keyword argument was received.

</dd></dl></dd>
</dl><dl><dt>*property*status<a href="#discord.ext.commands.Bot.status" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Status" title="discord.Status"><code>Status</code></a>: The status being used upon logging on to Discord.

</dd></dl><dl><dt>*property*stickers<a href="#discord.ext.commands.Bot.stickers" title="Permalink to this definition">¶</a></dt>
<dd>

The stickers that the connected client has.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Sequence\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.GuildSticker" title="discord.GuildSticker"><code>GuildSticker</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*tree<a href="#discord.ext.commands.Bot.tree" title="Permalink to this definition">¶</a></dt>
<dd>

The command tree responsible for handling the application commands in this bot.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.CommandTree" title="discord.app_commands.CommandTree"><code>CommandTree</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* unload_extension(*name*, ***, *package=None*)<a href="#discord.ext.commands.Bot.unload_extension" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Unloads an extension.

When the extension is unloaded, all commands, listeners, and cogs are removed from the bot and the module is un-imported.

The extension can provide an optional global function, <code>teardown</code>, to do miscellaneous clean-up if necessary. This function takes a single parameter, the <code>bot</code>, similar to <code>setup</code> from <a href="#discord.ext.commands.Bot.load_extension" title="discord.ext.commands.Bot.load_extension"><code>load_extension()</code></a>.

Changed in version 2.0: This method is now a <a href="https://docs.python.org/3/glossary.html#term-coroutine" title="(in Python v3.14)">coroutine</a>.

<dl><dt>Parameters</dt>
<dd>

- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The extension name to unload. It must be dot separated like regular Python imports if accessing a sub-module. e.g. <code>foo.test</code> if you want to import <code>foo/test.py</code>.
- **package** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) –

  The package name to resolve relative imports with. This is required when unloading an extension using a relative path, e.g <code>.foo.test</code>. Defaults to <code>None</code>.

  New in version 1.7.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.ExtensionNotFound" title="discord.ext.commands.ExtensionNotFound">**ExtensionNotFound**</a> – The name of the extension could not be resolved using the provided <code>package</code> parameter.
- <a href="#discord.ext.commands.ExtensionNotLoaded" title="discord.ext.commands.ExtensionNotLoaded">**ExtensionNotLoaded**</a> – The extension was not loaded.

</dd></dl></dd>
</dl><dl><dt>*property*user<a href="#discord.ext.commands.Bot.user" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the connected client. <code>None</code> if not logged in.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientUser" title="discord.ClientUser"><code>ClientUser</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*users<a href="#discord.ext.commands.Bot.users" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a list of all the users the bot can see.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*voice_clients<a href="#discord.ext.commands.Bot.voice_clients" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a list of voice connections.

These are usually <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.VoiceClient" title="discord.VoiceClient"><code>VoiceClient</code></a> instances.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.VoiceProtocol" title="discord.VoiceProtocol"><code>VoiceProtocol</code></a>]

</dd></dl></dd>
</dl><dl><dt>wait_for(*event*, */*, ***, *check=None*, *timeout=None*)<a href="#discord.ext.commands.Bot.wait_for" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Waits for a WebSocket event to be dispatched.

This could be used to wait for a user to reply to a message, or to react to a message, or to edit a message in a self-contained way.

The <code>timeout</code> parameter is passed onto <a href="https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for" title="(in Python v3.14)"><code>asyncio.wait_for()</code></a>. By default, it does not timeout. Note that this does propagate the <a href="https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.TimeoutError" title="(in Python v3.14)"><code>asyncio.TimeoutError</code></a> for you in case of timeout and is provided for ease of use.

In case the event returns multiple arguments, a <a href="https://docs.python.org/3/library/stdtypes.html#tuple" title="(in Python v3.14)"><code>tuple</code></a> containing those arguments is returned instead. Please check the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord-api-events">documentation</a> for a list of events and their parameters.

This function returns the **first event that meets the requirements**.

Examples

Waiting for a user reply:

```
@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(f'Hello {msg.author}!')

```

Waiting for a thumbs up reaction from the message author:

```
@client.event
async def on_message(message):
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

```

Changed in version 2.0: <code>event</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **event** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The event name, similar to the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord-api-events">event reference</a>, but without the <code>on_</code> prefix, to wait for.
- **check** (Optional\[Callable\[…, <a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]]) – A predicate to check what to wait for. The arguments must meet the parameters of the event being waited for.
- **timeout** (Optional\[<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]) – The number of seconds to wait before timing out and raising <a href="https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.TimeoutError" title="(in Python v3.14)"><code>asyncio.TimeoutError</code></a>.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.TimeoutError" title="(in Python v3.14)">**asyncio.TimeoutError**</a> – If a timeout is provided and it was reached.

</dd><dt>Returns</dt>
<dd>

Returns no arguments, a single argument, or a <a href="https://docs.python.org/3/library/stdtypes.html#tuple" title="(in Python v3.14)"><code>tuple</code></a> of multiple arguments that mirrors the parameters passed in the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord-api-events">event reference</a>.

</dd><dt>Return type</dt>
<dd>

Any

</dd></dl></dd>
</dl><dl><dt>*await* wait_until_ready()<a href="#discord.ext.commands.Bot.wait_until_ready" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Waits until the client’s internal cache is all ready.

Warning

Calling this inside <a href="#discord.ext.commands.Bot.setup_hook" title="discord.ext.commands.Bot.setup_hook"><code>setup_hook()</code></a> can lead to a deadlock.

</dd></dl><dl><dt>*for ... in* walk_commands()<a href="#discord.ext.commands.Bot.walk_commands" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all commands and subcommands.

Changed in version 1.4: Duplicates due to aliases are no longer returned

<dl><dt>Yields</dt>
<dd>

Union\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>, <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>] – A command or group from the internal list of commands.

</dd></dl></dd>
</dl></dd>
</dl>

### AutoShardedBot ¶

<dl><dt>*class*discord.ext.commands.AutoShardedBot(*command_prefix*, ***, *help_command=&lt;default-help-command&gt;*, *tree_cls=&lt;class 'discord.app_commands.tree.CommandTree'&gt;*, *description=None*, *allowed_contexts=...*, *allowed_installs=...*, *intents*, ***options*)<a href="#discord.ext.commands.AutoShardedBot" title="Permalink to this definition">¶</a></dt>
<dd>

This is similar to <a href="#discord.ext.commands.Bot" title="discord.ext.commands.Bot"><code>Bot</code></a> except that it is inherited from <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AutoShardedClient" title="discord.AutoShardedClient"><code>discord.AutoShardedClient</code></a> instead.

<dl><dt>async with x</dt>
<dd>

Asynchronously initialises the bot and automatically cleans.

New in version 2.0.

</dd></dl>

</dd></dl>

## Prefix Helpers ¶

<dl><dt>discord.ext.commands.when_mentioned(*bot*, *msg*, */*)<a href="#discord.ext.commands.when_mentioned" title="Permalink to this definition">¶</a></dt>
<dd>

A callable that implements a command prefix equivalent to being mentioned.

These are meant to be passed into the <a href="#discord.ext.commands.Bot.command_prefix" title="discord.ext.commands.Bot.command_prefix"><code>Bot.command_prefix</code></a> attribute.

> Changed in version 2.0: <code>bot</code> and <code>msg</code> parameters are now positional-only.

</dd></dl><dl><dt>discord.ext.commands.when_mentioned_or(**prefixes*)<a href="#discord.ext.commands.when_mentioned_or" title="Permalink to this definition">¶</a></dt>
<dd>

A callable that implements when mentioned or other prefixes provided.

These are meant to be passed into the <a href="#discord.ext.commands.Bot.command_prefix" title="discord.ext.commands.Bot.command_prefix"><code>Bot.command_prefix</code></a> attribute.

Example

```
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))

```

Note

This callable returns another callable, so if this is done inside a custom callable, you must call the returned callable, for example:

```
async def get_prefix(bot, message):
    extras = await prefixes_for(message.guild) # returns a list
    return commands.when_mentioned_or(*extras)(bot, message)

```

See also

<a href="#discord.ext.commands.when_mentioned" title="discord.ext.commands.when_mentioned"><code>when_mentioned()</code></a>

</dd></dl>

## Event Reference ¶

These events function similar to [the regular events](https://discordpy.readthedocs.io/en/stable/api.html#discord-api-events), except they are custom to the command extension module.

<dl><dt>discord.ext.commands.on_command_error(*ctx*, *error*)<a href="#discord.discord.ext.commands.on_command_error" title="Permalink to this definition">¶</a></dt>
<dd>

An error handler that is called when an error is raised inside a command either through user input error, check failure, or an error in your own code.

A default one is provided (<a href="#discord.ext.commands.Bot.on_command_error" title="discord.ext.commands.Bot.on_command_error"><code>Bot.on_command_error()</code></a>).

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context.
- **error** (<a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived) – The error that was raised.

</dd></dl></dd>
</dl><dl><dt>discord.ext.commands.on_command(*ctx*)<a href="#discord.discord.ext.commands.on_command" title="Permalink to this definition">¶</a></dt>
<dd>

An event that is called when a command is found and is about to be invoked.

This event is called regardless of whether the command itself succeeds via error or completes.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context.

</dd></dl></dd>
</dl><dl><dt>discord.ext.commands.on_command_completion(*ctx*)<a href="#discord.discord.ext.commands.on_command_completion" title="Permalink to this definition">¶</a></dt>
<dd>

An event that is called when a command has completed its invocation.

This event is called only if the command succeeded, i.e. all checks have passed and the user input it correctly.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context.

</dd></dl></dd>
</dl>

## Commands ¶

### Decorators ¶

<dl><dt>@discord.ext.commands.command(*name=...*, *cls=...*, ***attrs*)<a href="#discord.ext.commands.command" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that transforms a function into a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> or if called with <a href="#discord.ext.commands.group" title="discord.ext.commands.group"><code>group()</code></a>, <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>.

By default the <code>help</code> attribute is received automatically from the docstring of the function and is cleaned up with the use of <code>inspect.cleandoc</code>. If the docstring is <code>bytes</code>, then it is decoded into <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a> using utf-8 encoding.

All checks added using the <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> &amp; co. decorators are added into the function. There is no way to supply your own checks through this decorator.

<dl><dt>Parameters</dt>
<dd>

- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name to create the command with. By default this uses the function name unchanged.
- **cls** – The class to construct with. By default this is <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>. You usually do not change this.
- **attrs** – Keyword arguments to pass into the construction of the class denoted by <code>cls</code>.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – If the function is not a coroutine or is already a command.

</dd></dl></dd>
</dl><dl><dt>@discord.ext.commands.group(*name=...*, *cls=...*, ***attrs*)<a href="#discord.ext.commands.group" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that transforms a function into a <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>.

This is similar to the <a href="#discord.ext.commands.command" title="discord.ext.commands.command"><code>command()</code></a> decorator but the <code>cls</code> parameter is set to <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a> by default.

Changed in version 1.1: The <code>cls</code> parameter can now be passed.

</dd></dl><dl><dt>@discord.ext.commands.hybrid_command(*name=...*, ***, *with_app_command=True*, ***attrs*)<a href="#discord.ext.commands.hybrid_command" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that transforms a function into a <a href="#discord.ext.commands.HybridCommand" title="discord.ext.commands.HybridCommand"><code>HybridCommand</code></a>.

A hybrid command is one that functions both as a regular <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> and one that is also a <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Command" title="discord.app_commands.Command"><code>app_commands.Command</code></a>.

The callback being attached to the command must be representable as an application command callback. Converters are silently converted into a <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Transformer" title="discord.app_commands.Transformer"><code>Transformer</code></a> with a <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.AppCommandOptionType.string" title="discord.AppCommandOptionType.string"><code>discord.AppCommandOptionType.string</code></a> type.

Checks and error handlers are dispatched and called as-if they were commands similar to <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>. This means that they take <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a> as a parameter rather than <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a>.

All checks added using the <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> &amp; co. decorators are added into the function. There is no way to supply your own checks through this decorator.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **name** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The name to create the command with. By default this uses the function name unchanged.
- **with\_app\_command** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to register the command also as an application command.
- **\*\*attrs** – Keyword arguments to pass into the construction of the hybrid command.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – If the function is not a coroutine or is already a command.

</dd></dl></dd>
</dl><dl><dt>@discord.ext.commands.hybrid_group(*name=...*, ***, *with_app_command=True*, ***attrs*)<a href="#discord.ext.commands.hybrid_group" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that transforms a function into a <a href="#discord.ext.commands.HybridGroup" title="discord.ext.commands.HybridGroup"><code>HybridGroup</code></a>.

This is similar to the <a href="#discord.ext.commands.group" title="discord.ext.commands.group"><code>group()</code></a> decorator except it creates a hybrid group instead.

<dl><dt>Parameters</dt>
<dd>

- **name** (Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]) – The name to create the group with. By default this uses the function name unchanged.
- **with\_app\_command** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to register the command also as an application command.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – If the function is not a coroutine or is already a command.

</dd></dl></dd>
</dl>

### Command ¶

Attributes

- [aliases](#discord.ext.commands.Command.aliases)
- [brief](#discord.ext.commands.Command.brief)
- [callback](#discord.ext.commands.Command.callback)
- [checks](#discord.ext.commands.Command.checks)
- [clean\_params](#discord.ext.commands.Command.clean_params)
- [cog](#discord.ext.commands.Command.cog)
- [cog\_name](#discord.ext.commands.Command.cog_name)
- [cooldown](#discord.ext.commands.Command.cooldown)
- [cooldown\_after\_parsing](#discord.ext.commands.Command.cooldown_after_parsing)
- [description](#discord.ext.commands.Command.description)
- [enabled](#discord.ext.commands.Command.enabled)
- [extras](#discord.ext.commands.Command.extras)
- [full\_parent\_name](#discord.ext.commands.Command.full_parent_name)
- [help](#discord.ext.commands.Command.help)
- [hidden](#discord.ext.commands.Command.hidden)
- [ignore\_extra](#discord.ext.commands.Command.ignore_extra)
- [invoked\_subcommand](#discord.ext.commands.Command.invoked_subcommand)
- [name](#discord.ext.commands.Command.name)
- [parent](#discord.ext.commands.Command.parent)
- [parents](#discord.ext.commands.Command.parents)
- [qualified\_name](#discord.ext.commands.Command.qualified_name)
- [require\_var\_positional](#discord.ext.commands.Command.require_var_positional)
- [rest\_is\_raw](#discord.ext.commands.Command.rest_is_raw)
- [root\_parent](#discord.ext.commands.Command.root_parent)
- [short\_doc](#discord.ext.commands.Command.short_doc)
- [signature](#discord.ext.commands.Command.signature)
- [usage](#discord.ext.commands.Command.usage)

Methods

- async [\_\_call\_\_](#discord.ext.commands.Command.__call__)
- def [add\_check](#discord.ext.commands.Command.add_check)
- @ [after\_invoke](#discord.ext.commands.Command.after_invoke)
- @ [before\_invoke](#discord.ext.commands.Command.before_invoke)
- async [can\_run](#discord.ext.commands.Command.can_run)
- def [copy](#discord.ext.commands.Command.copy)
- @ [error](#discord.ext.commands.Command.error)
- def [get\_cooldown\_retry\_after](#discord.ext.commands.Command.get_cooldown_retry_after)
- def [has\_error\_handler](#discord.ext.commands.Command.has_error_handler)
- def [is\_on\_cooldown](#discord.ext.commands.Command.is_on_cooldown)
- def [remove\_check](#discord.ext.commands.Command.remove_check)
- def [reset\_cooldown](#discord.ext.commands.Command.reset_cooldown)
- def [update](#discord.ext.commands.Command.update)

<dl><dt>*class*discord.ext.commands.Command(**args*, ***kwargs*)<a href="#discord.ext.commands.Command" title="Permalink to this definition">¶</a></dt>
<dd>

A class that implements the protocol for a bot text command.

These are not created manually, instead they are created via the decorator or functional interface.

<dl><dt>name<a href="#discord.ext.commands.Command.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the command.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>callback<a href="#discord.ext.commands.Command.callback" title="Permalink to this definition">¶</a></dt>
<dd>

The coroutine that is executed when the command is called.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>

</dd></dl></dd>
</dl><dl><dt>help<a href="#discord.ext.commands.Command.help" title="Permalink to this definition">¶</a></dt>
<dd>

The long help text for the command.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>brief<a href="#discord.ext.commands.Command.brief" title="Permalink to this definition">¶</a></dt>
<dd>

The short help text for the command.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>usage<a href="#discord.ext.commands.Command.usage" title="Permalink to this definition">¶</a></dt>
<dd>

A replacement for arguments in the default help text.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>aliases<a href="#discord.ext.commands.Command.aliases" title="Permalink to this definition">¶</a></dt>
<dd>

The list of aliases the command can be invoked under.

<dl><dt>Type</dt>
<dd>

Union\[List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>], Tuple\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]]

</dd></dl></dd>
</dl><dl><dt>enabled<a href="#discord.ext.commands.Command.enabled" title="Permalink to this definition">¶</a></dt>
<dd>

A boolean that indicates if the command is currently enabled. If the command is invoked while it is disabled, then <a href="#discord.ext.commands.DisabledCommand" title="discord.ext.commands.DisabledCommand"><code>DisabledCommand</code></a> is raised to the <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> event. Defaults to <code>True</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>parent<a href="#discord.ext.commands.Command.parent" title="Permalink to this definition">¶</a></dt>
<dd>

The parent group that this command belongs to. <code>None</code> if there isn’t one.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>cog<a href="#discord.ext.commands.Command.cog" title="Permalink to this definition">¶</a></dt>
<dd>

The cog that this command belongs to. <code>None</code> if there isn’t one.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>]

</dd></dl></dd>
</dl><dl><dt>checks<a href="#discord.ext.commands.Command.checks" title="Permalink to this definition">¶</a></dt>
<dd>

A list of predicates that verifies if the command could be executed with the given <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a> as the sole parameter. If an exception is necessary to be thrown to signal failure, then one inherited from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> should be used. Note that if the checks fail then <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a> exception is raised to the <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> event.

<dl><dt>Type</dt>
<dd>

List\[Callable\[\[<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>], <a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]]

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.ext.commands.Command.description" title="Permalink to this definition">¶</a></dt>
<dd>

The message prefixed into the default help command.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>hidden<a href="#discord.ext.commands.Command.hidden" title="Permalink to this definition">¶</a></dt>
<dd>

If <code>True</code>, the default help command does not show this in the help output.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>rest_is_raw<a href="#discord.ext.commands.Command.rest_is_raw" title="Permalink to this definition">¶</a></dt>
<dd>

If <code>False</code> and a keyword-only argument is provided then the keyword only argument is stripped and handled as if it was a regular argument that handles <a href="#discord.ext.commands.MissingRequiredArgument" title="discord.ext.commands.MissingRequiredArgument"><code>MissingRequiredArgument</code></a> and default values in a regular matter rather than passing the rest completely raw. If <code>True</code> then the keyword-only argument will pass in the rest of the arguments in a completely raw matter. Defaults to <code>False</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>invoked_subcommand<a href="#discord.ext.commands.Command.invoked_subcommand" title="Permalink to this definition">¶</a></dt>
<dd>

The subcommand that was invoked, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>require_var_positional<a href="#discord.ext.commands.Command.require_var_positional" title="Permalink to this definition">¶</a></dt>
<dd>

If <code>True</code> and a variadic positional argument is specified, requires the user to specify at least one argument. Defaults to <code>False</code>.

New in version 1.5.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>ignore_extra<a href="#discord.ext.commands.Command.ignore_extra" title="Permalink to this definition">¶</a></dt>
<dd>

If <code>True</code>, ignores extraneous strings passed to a command if all its requirements are met (e.g. <code>?foo a b c</code> when only expecting <code>a</code> and <code>b</code>). Otherwise <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> and local error handlers are called with <a href="#discord.ext.commands.TooManyArguments" title="discord.ext.commands.TooManyArguments"><code>TooManyArguments</code></a>. Defaults to <code>True</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>cooldown_after_parsing<a href="#discord.ext.commands.Command.cooldown_after_parsing" title="Permalink to this definition">¶</a></dt>
<dd>

If <code>True</code>, cooldown processing is done after argument parsing, which calls converters. If <code>False</code> then cooldown processing is done first and then the converters are called second. Defaults to <code>False</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>extras<a href="#discord.ext.commands.Command.extras" title="Permalink to this definition">¶</a></dt>
<dd>

A dict of user provided extras to attach to the Command.

Note

This object may be copied by the library.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

New in version 2.0.

</dd></dl></dd>
</dl><dl><dt>@after_invoke<a href="#discord.ext.commands.Command.after_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a post-invoke hook.

A post-invoke hook is called directly after the command is called. This makes it a useful function to clean-up database connections or any type of clean up required.

This post-invoke hook takes a sole parameter, a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

See <a href="#discord.ext.commands.Bot.after_invoke" title="discord.ext.commands.Bot.after_invoke"><code>Bot.after_invoke()</code></a> for more info.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the post-invoke hook.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@before_invoke<a href="#discord.ext.commands.Command.before_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a pre-invoke hook.

A pre-invoke hook is called directly before the command is called. This makes it a useful function to set up database connections or any type of set up required.

This pre-invoke hook takes a sole parameter, a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

See <a href="#discord.ext.commands.Bot.before_invoke" title="discord.ext.commands.Bot.before_invoke"><code>Bot.before_invoke()</code></a> for more info.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the pre-invoke hook.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@error<a href="#discord.ext.commands.Command.error" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a local error handler.

A local error handler is an <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> event limited to a single command. However, the <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> is still invoked afterwards as the catch-all.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the local error handler.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>add_check(*func*, */*)<a href="#discord.ext.commands.Command.add_check" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a check to the command.

This is the non-decorator interface to <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a>.

New in version 1.3.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

See also

The <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> decorator

<dl><dt>Parameters</dt>
<dd>

**func** – The function that will be used as a check.

</dd></dl></dd>
</dl><dl><dt>remove_check(*func*, */*)<a href="#discord.ext.commands.Command.remove_check" title="Permalink to this definition">¶</a></dt>
<dd>

Removes a check from the command.

This function is idempotent and will not raise an exception if the function is not in the command’s checks.

New in version 1.3.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**func** – The function to remove from the checks.

</dd></dl></dd>
</dl><dl><dt>update(***kwargs*)<a href="#discord.ext.commands.Command.update" title="Permalink to this definition">¶</a></dt>
<dd>

Updates <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> instance with updated attribute.

This works similarly to the <a href="#discord.ext.commands.command" title="discord.ext.commands.command"><code>command()</code></a> decorator in terms of parameters in that they are passed to the <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> or subclass constructors, sans the name and callback.

</dd></dl><dl><dt>*await* __call__(*context*, */*, **args*, ***kwargs*)<a href="#discord.ext.commands.Command.__call__" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Calls the internal callback that the command holds.

Note

This bypasses all mechanisms – including checks, converters, invoke hooks, cooldowns, etc. You must take care to pass the proper arguments and types to this function.

New in version 1.3.

Changed in version 2.0: <code>context</code> parameter is now positional-only.

</dd></dl><dl><dt>copy()<a href="#discord.ext.commands.Command.copy" title="Permalink to this definition">¶</a></dt>
<dd>

Creates a copy of this command.

<dl><dt>Returns</dt>
<dd>

A new instance of this command.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*clean_params<a href="#discord.ext.commands.Command.clean_params" title="Permalink to this definition">¶</a></dt>
<dd>

Dict\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.ext.commands.Parameter" title="discord.ext.commands.Parameter"><code>Parameter</code></a>]: Retrieves the parameter dictionary without the context or self parameters.

Useful for inspecting signature.

</dd></dl><dl><dt>*property*cooldown<a href="#discord.ext.commands.Command.cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

The cooldown of a command when invoked or <code>None</code> if the command doesn’t have a registered cooldown.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Cooldown" title="discord.app_commands.Cooldown"><code>Cooldown</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*full_parent_name<a href="#discord.ext.commands.Command.full_parent_name" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the fully qualified parent command name.

This the base command name required to execute it. For example, in <code>?one two three</code> the parent name would be <code>one two</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parents<a href="#discord.ext.commands.Command.parents" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the parents of this command.

If the command has no parents then it returns an empty <a href="https://docs.python.org/3/library/stdtypes.html#list" title="(in Python v3.14)"><code>list</code></a>.

For example in commands <code>?a b c test</code>, the parents are <code>[c, b, a]</code>.

New in version 1.1.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*root_parent<a href="#discord.ext.commands.Command.root_parent" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the root parent of this command.

If the command has no parents then it returns <code>None</code>.

For example in commands <code>?a b c test</code>, the root parent is <code>a</code>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*qualified_name<a href="#discord.ext.commands.Command.qualified_name" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the fully qualified command name.

This is the full parent name with the command name as well. For example, in <code>?one two three</code> the qualified name would be <code>one two three</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>is_on_cooldown(*ctx*, */*)<a href="#discord.ext.commands.Command.is_on_cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

Checks whether the command is currently on cooldown.

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context to use when checking the commands cooldown status.

</dd><dt>Returns</dt>
<dd>

A boolean indicating if the command is on cooldown.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>reset_cooldown(*ctx*, */*)<a href="#discord.ext.commands.Command.reset_cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

Resets the cooldown on this command.

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context to reset the cooldown under.

</dd></dl></dd>
</dl><dl><dt>get_cooldown_retry_after(*ctx*, */*)<a href="#discord.ext.commands.Command.get_cooldown_retry_after" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the amount of seconds before this command can be tried again.

New in version 1.4.

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context to retrieve the cooldown from.

</dd><dt>Returns</dt>
<dd>

The amount of time left on this command’s cooldown in seconds. If this is <code>0.0</code> then the command isn’t on cooldown.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>

</dd></dl></dd>
</dl><dl><dt>has_error_handler()<a href="#discord.ext.commands.Command.has_error_handler" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Checks whether the command has an error handler registered.

New in version 1.7.

</dd></dl><dl><dt>*property*cog_name<a href="#discord.ext.commands.Command.cog_name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the cog this command belongs to, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*short_doc<a href="#discord.ext.commands.Command.short_doc" title="Permalink to this definition">¶</a></dt>
<dd>

Gets the “short” documentation of a command.

By default, this is the <a href="#discord.ext.commands.Command.brief" title="discord.ext.commands.Command.brief"><code>brief</code></a> attribute. If that lookup leads to an empty string then the first line of the <a href="#discord.ext.commands.Command.help" title="discord.ext.commands.Command.help"><code>help</code></a> attribute is used instead.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*signature<a href="#discord.ext.commands.Command.signature" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a POSIX-like signature useful for help command output.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* can_run(*ctx*, */*)<a href="#discord.ext.commands.Command.can_run" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Checks if the command can be executed by checking all the predicates inside the <a href="#discord.ext.commands.Command.checks" title="discord.ext.commands.Command.checks"><code>checks</code></a> attribute. This also checks whether the command is disabled.

Changed in version 1.3: Checks whether the command is disabled or not

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The ctx of the command currently being invoked.

</dd><dt>Raises</dt>
<dd>

<a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – Any command error that was raised during a check call will be propagated by this function.

</dd><dt>Returns</dt>
<dd>

A boolean indicating if the command can be invoked.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### Group ¶

Attributes

- [case\_insensitive](#discord.ext.commands.Group.case_insensitive)
- [clean\_params](#discord.ext.commands.Group.clean_params)
- [cog\_name](#discord.ext.commands.Group.cog_name)
- [commands](#discord.ext.commands.Group.commands)
- [cooldown](#discord.ext.commands.Group.cooldown)
- [full\_parent\_name](#discord.ext.commands.Group.full_parent_name)
- [invoke\_without\_command](#discord.ext.commands.Group.invoke_without_command)
- [parents](#discord.ext.commands.Group.parents)
- [qualified\_name](#discord.ext.commands.Group.qualified_name)
- [root\_parent](#discord.ext.commands.Group.root_parent)
- [short\_doc](#discord.ext.commands.Group.short_doc)
- [signature](#discord.ext.commands.Group.signature)

Methods

- def [add\_check](#discord.ext.commands.Group.add_check)
- def [add\_command](#discord.ext.commands.Group.add_command)
- @ [after\_invoke](#discord.ext.commands.Group.after_invoke)
- @ [before\_invoke](#discord.ext.commands.Group.before_invoke)
- async [can\_run](#discord.ext.commands.Group.can_run)
- @ [command](#discord.ext.commands.Group.command)
- def [copy](#discord.ext.commands.Group.copy)
- @ [error](#discord.ext.commands.Group.error)
- def [get\_command](#discord.ext.commands.Group.get_command)
- def [get\_cooldown\_retry\_after](#discord.ext.commands.Group.get_cooldown_retry_after)
- @ [group](#discord.ext.commands.Group.group)
- def [has\_error\_handler](#discord.ext.commands.Group.has_error_handler)
- def [is\_on\_cooldown](#discord.ext.commands.Group.is_on_cooldown)
- def [remove\_check](#discord.ext.commands.Group.remove_check)
- def [remove\_command](#discord.ext.commands.Group.remove_command)
- def [reset\_cooldown](#discord.ext.commands.Group.reset_cooldown)
- def [update](#discord.ext.commands.Group.update)
- def [walk\_commands](#discord.ext.commands.Group.walk_commands)

<dl><dt>*class*discord.ext.commands.Group(**args*, ***kwargs*)<a href="#discord.ext.commands.Group" title="Permalink to this definition">¶</a></dt>
<dd>

A class that implements a grouping protocol for commands to be executed as subcommands.

This class is a subclass of <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> and thus all options valid in <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> are valid in here as well.

<dl><dt>invoke_without_command<a href="#discord.ext.commands.Group.invoke_without_command" title="Permalink to this definition">¶</a></dt>
<dd>

Indicates if the group callback should begin parsing and invocation only if no subcommand was found. Useful for making it an error handling function to tell the user that no subcommand was found or to have different functionality in case no subcommand was found. If this is <code>False</code>, then the group callback will always be invoked first. This means that the checks and the parsing dictated by its parameters will be executed. Defaults to <code>False</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>case_insensitive<a href="#discord.ext.commands.Group.case_insensitive" title="Permalink to this definition">¶</a></dt>
<dd>

Indicates if the group’s commands should be case insensitive. Defaults to <code>False</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>@after_invoke<a href="#discord.ext.commands.Group.after_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a post-invoke hook.

A post-invoke hook is called directly after the command is called. This makes it a useful function to clean-up database connections or any type of clean up required.

This post-invoke hook takes a sole parameter, a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

See <a href="#discord.ext.commands.Bot.after_invoke" title="discord.ext.commands.Bot.after_invoke"><code>Bot.after_invoke()</code></a> for more info.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the post-invoke hook.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@before_invoke<a href="#discord.ext.commands.Group.before_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a pre-invoke hook.

A pre-invoke hook is called directly before the command is called. This makes it a useful function to set up database connections or any type of set up required.

This pre-invoke hook takes a sole parameter, a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

See <a href="#discord.ext.commands.Bot.before_invoke" title="discord.ext.commands.Bot.before_invoke"><code>Bot.before_invoke()</code></a> for more info.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the pre-invoke hook.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@command(**args*, ***kwargs*)<a href="#discord.ext.commands.Group.command" title="Permalink to this definition">¶</a></dt>
<dd>

A shortcut decorator that invokes <a href="#discord.ext.commands.command" title="discord.ext.commands.command"><code>command()</code></a> and adds it to the internal command list via <a href="#discord.ext.commands.GroupMixin.add_command" title="discord.ext.commands.GroupMixin.add_command"><code>add_command()</code></a>.

<dl><dt>Returns</dt>
<dd>

A decorator that converts the provided method into a Command, adds it to the bot, then returns it.

</dd><dt>Return type</dt>
<dd>

Callable\[…, <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>@error<a href="#discord.ext.commands.Group.error" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a local error handler.

A local error handler is an <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> event limited to a single command. However, the <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> is still invoked afterwards as the catch-all.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the local error handler.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@group(**args*, ***kwargs*)<a href="#discord.ext.commands.Group.group" title="Permalink to this definition">¶</a></dt>
<dd>

A shortcut decorator that invokes <a href="#discord.ext.commands.group" title="discord.ext.commands.group"><code>group()</code></a> and adds it to the internal command list via <a href="#discord.ext.commands.GroupMixin.add_command" title="discord.ext.commands.GroupMixin.add_command"><code>add_command()</code></a>.

<dl><dt>Returns</dt>
<dd>

A decorator that converts the provided method into a Group, adds it to the bot, then returns it.

</dd><dt>Return type</dt>
<dd>

Callable\[…, <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>copy()<a href="#discord.ext.commands.Group.copy" title="Permalink to this definition">¶</a></dt>
<dd>

Creates a copy of this <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>.

<dl><dt>Returns</dt>
<dd>

A new instance of this group.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>

</dd></dl></dd>
</dl><dl><dt>add_check(*func*, */*)<a href="#discord.ext.commands.Group.add_check" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a check to the command.

This is the non-decorator interface to <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a>.

New in version 1.3.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

See also

The <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> decorator

<dl><dt>Parameters</dt>
<dd>

**func** – The function that will be used as a check.

</dd></dl></dd>
</dl><dl><dt>add_command(*command*, */*)<a href="#discord.ext.commands.Group.add_command" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> into the internal list of commands.

This is usually not called, instead the <a href="#discord.ext.commands.GroupMixin.command" title="discord.ext.commands.GroupMixin.command"><code>command()</code></a> or <a href="#discord.ext.commands.GroupMixin.group" title="discord.ext.commands.GroupMixin.group"><code>group()</code></a> shortcut decorators are used instead.

Changed in version 1.4: Raise <a href="#discord.ext.commands.CommandRegistrationError" title="discord.ext.commands.CommandRegistrationError"><code>CommandRegistrationError</code></a> instead of generic <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientException" title="discord.ClientException"><code>ClientException</code></a>

Changed in version 2.0: <code>command</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command to add.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandRegistrationError" title="discord.ext.commands.CommandRegistrationError">**CommandRegistrationError**</a> – If the command or its alias is already registered by different command.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – If the command passed is not a subclass of <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>.

</dd></dl></dd>
</dl><dl><dt>*await* can_run(*ctx*, */*)<a href="#discord.ext.commands.Group.can_run" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Checks if the command can be executed by checking all the predicates inside the <a href="#discord.ext.commands.Command.checks" title="discord.ext.commands.Command.checks"><code>checks</code></a> attribute. This also checks whether the command is disabled.

Changed in version 1.3: Checks whether the command is disabled or not

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The ctx of the command currently being invoked.

</dd><dt>Raises</dt>
<dd>

<a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – Any command error that was raised during a check call will be propagated by this function.

</dd><dt>Returns</dt>
<dd>

A boolean indicating if the command can be invoked.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*clean_params<a href="#discord.ext.commands.Group.clean_params" title="Permalink to this definition">¶</a></dt>
<dd>

Dict\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.ext.commands.Parameter" title="discord.ext.commands.Parameter"><code>Parameter</code></a>]: Retrieves the parameter dictionary without the context or self parameters.

Useful for inspecting signature.

</dd></dl><dl><dt>*property*cog_name<a href="#discord.ext.commands.Group.cog_name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the cog this command belongs to, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*commands<a href="#discord.ext.commands.Group.commands" title="Permalink to this definition">¶</a></dt>
<dd>

A unique set of commands without aliases that are registered.

<dl><dt>Type</dt>
<dd>

Set\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*cooldown<a href="#discord.ext.commands.Group.cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

The cooldown of a command when invoked or <code>None</code> if the command doesn’t have a registered cooldown.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Cooldown" title="discord.app_commands.Cooldown"><code>Cooldown</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*full_parent_name<a href="#discord.ext.commands.Group.full_parent_name" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the fully qualified parent command name.

This the base command name required to execute it. For example, in <code>?one two three</code> the parent name would be <code>one two</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>get_command(*name*, */*)<a href="#discord.ext.commands.Group.get_command" title="Permalink to this definition">¶</a></dt>
<dd>

Get a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> from the internal list of commands.

This could also be used as a way to get aliases.

The name could be fully qualified (e.g. <code>'foo bar'</code>) will get the subcommand <code>bar</code> of the group command <code>foo</code>. If a subcommand is not found then <code>None</code> is returned just as usual.

Changed in version 2.0: <code>name</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the command to get.

</dd><dt>Returns</dt>
<dd>

The command that was requested. If not found, returns <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_cooldown_retry_after(*ctx*, */*)<a href="#discord.ext.commands.Group.get_cooldown_retry_after" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the amount of seconds before this command can be tried again.

New in version 1.4.

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context to retrieve the cooldown from.

</dd><dt>Returns</dt>
<dd>

The amount of time left on this command’s cooldown in seconds. If this is <code>0.0</code> then the command isn’t on cooldown.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>

</dd></dl></dd>
</dl><dl><dt>has_error_handler()<a href="#discord.ext.commands.Group.has_error_handler" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Checks whether the command has an error handler registered.

New in version 1.7.

</dd></dl><dl><dt>is_on_cooldown(*ctx*, */*)<a href="#discord.ext.commands.Group.is_on_cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

Checks whether the command is currently on cooldown.

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context to use when checking the commands cooldown status.

</dd><dt>Returns</dt>
<dd>

A boolean indicating if the command is on cooldown.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parents<a href="#discord.ext.commands.Group.parents" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the parents of this command.

If the command has no parents then it returns an empty <a href="https://docs.python.org/3/library/stdtypes.html#list" title="(in Python v3.14)"><code>list</code></a>.

For example in commands <code>?a b c test</code>, the parents are <code>[c, b, a]</code>.

New in version 1.1.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*qualified_name<a href="#discord.ext.commands.Group.qualified_name" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the fully qualified command name.

This is the full parent name with the command name as well. For example, in <code>?one two three</code> the qualified name would be <code>one two three</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>remove_check(*func*, */*)<a href="#discord.ext.commands.Group.remove_check" title="Permalink to this definition">¶</a></dt>
<dd>

Removes a check from the command.

This function is idempotent and will not raise an exception if the function is not in the command’s checks.

New in version 1.3.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**func** – The function to remove from the checks.

</dd></dl></dd>
</dl><dl><dt>remove_command(*name*, */*)<a href="#discord.ext.commands.Group.remove_command" title="Permalink to this definition">¶</a></dt>
<dd>

Remove a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> from the internal list of commands.

This could also be used as a way to remove aliases.

Changed in version 2.0: <code>name</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the command to remove.

</dd><dt>Returns</dt>
<dd>

The command that was removed. If the name is not valid then <code>None</code> is returned instead.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>reset_cooldown(*ctx*, */*)<a href="#discord.ext.commands.Group.reset_cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

Resets the cooldown on this command.

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context to reset the cooldown under.

</dd></dl></dd>
</dl><dl><dt>*property*root_parent<a href="#discord.ext.commands.Group.root_parent" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the root parent of this command.

If the command has no parents then it returns <code>None</code>.

For example in commands <code>?a b c test</code>, the root parent is <code>a</code>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*short_doc<a href="#discord.ext.commands.Group.short_doc" title="Permalink to this definition">¶</a></dt>
<dd>

Gets the “short” documentation of a command.

By default, this is the <a href="#discord.ext.commands.Command.brief" title="discord.ext.commands.Command.brief"><code>brief</code></a> attribute. If that lookup leads to an empty string then the first line of the <a href="#discord.ext.commands.Command.help" title="discord.ext.commands.Command.help"><code>help</code></a> attribute is used instead.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*signature<a href="#discord.ext.commands.Group.signature" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a POSIX-like signature useful for help command output.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>update(***kwargs*)<a href="#discord.ext.commands.Group.update" title="Permalink to this definition">¶</a></dt>
<dd>

Updates <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> instance with updated attribute.

This works similarly to the <a href="#discord.ext.commands.command" title="discord.ext.commands.command"><code>command()</code></a> decorator in terms of parameters in that they are passed to the <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> or subclass constructors, sans the name and callback.

</dd></dl><dl><dt>*for ... in* walk_commands()<a href="#discord.ext.commands.Group.walk_commands" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all commands and subcommands.

Changed in version 1.4: Duplicates due to aliases are no longer returned

<dl><dt>Yields</dt>
<dd>

Union\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>, <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>] – A command or group from the internal list of commands.

</dd></dl></dd>
</dl></dd>
</dl>

### GroupMixin ¶

Attributes

- [all\_commands](#discord.ext.commands.GroupMixin.all_commands)
- [case\_insensitive](#discord.ext.commands.GroupMixin.case_insensitive)
- [commands](#discord.ext.commands.GroupMixin.commands)

Methods

- def [add\_command](#discord.ext.commands.GroupMixin.add_command)
- @ [command](#discord.ext.commands.GroupMixin.command)
- def [get\_command](#discord.ext.commands.GroupMixin.get_command)
- @ [group](#discord.ext.commands.GroupMixin.group)
- def [remove\_command](#discord.ext.commands.GroupMixin.remove_command)
- def [walk\_commands](#discord.ext.commands.GroupMixin.walk_commands)

<dl><dt>*class*discord.ext.commands.GroupMixin(**args*, ***kwargs*)<a href="#discord.ext.commands.GroupMixin" title="Permalink to this definition">¶</a></dt>
<dd>

A mixin that implements common functionality for classes that behave similar to <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a> and are allowed to register commands.

<dl><dt>all_commands<a href="#discord.ext.commands.GroupMixin.all_commands" title="Permalink to this definition">¶</a></dt>
<dd>

A mapping of command name to <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> objects.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

</dd></dl></dd>
</dl><dl><dt>case_insensitive<a href="#discord.ext.commands.GroupMixin.case_insensitive" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the commands should be case insensitive. Defaults to <code>False</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>@command(**args*, ***kwargs*)<a href="#discord.ext.commands.GroupMixin.command" title="Permalink to this definition">¶</a></dt>
<dd>

A shortcut decorator that invokes <a href="#discord.ext.commands.command" title="discord.ext.commands.command"><code>command()</code></a> and adds it to the internal command list via <a href="#discord.ext.commands.GroupMixin.add_command" title="discord.ext.commands.GroupMixin.add_command"><code>add_command()</code></a>.

<dl><dt>Returns</dt>
<dd>

A decorator that converts the provided method into a Command, adds it to the bot, then returns it.

</dd><dt>Return type</dt>
<dd>

Callable\[…, <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>@group(**args*, ***kwargs*)<a href="#discord.ext.commands.GroupMixin.group" title="Permalink to this definition">¶</a></dt>
<dd>

A shortcut decorator that invokes <a href="#discord.ext.commands.group" title="discord.ext.commands.group"><code>group()</code></a> and adds it to the internal command list via <a href="#discord.ext.commands.GroupMixin.add_command" title="discord.ext.commands.GroupMixin.add_command"><code>add_command()</code></a>.

<dl><dt>Returns</dt>
<dd>

A decorator that converts the provided method into a Group, adds it to the bot, then returns it.

</dd><dt>Return type</dt>
<dd>

Callable\[…, <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*commands<a href="#discord.ext.commands.GroupMixin.commands" title="Permalink to this definition">¶</a></dt>
<dd>

A unique set of commands without aliases that are registered.

<dl><dt>Type</dt>
<dd>

Set\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>add_command(*command*, */*)<a href="#discord.ext.commands.GroupMixin.add_command" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> into the internal list of commands.

This is usually not called, instead the <a href="#discord.ext.commands.GroupMixin.command" title="discord.ext.commands.GroupMixin.command"><code>command()</code></a> or <a href="#discord.ext.commands.GroupMixin.group" title="discord.ext.commands.GroupMixin.group"><code>group()</code></a> shortcut decorators are used instead.

Changed in version 1.4: Raise <a href="#discord.ext.commands.CommandRegistrationError" title="discord.ext.commands.CommandRegistrationError"><code>CommandRegistrationError</code></a> instead of generic <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientException" title="discord.ClientException"><code>ClientException</code></a>

Changed in version 2.0: <code>command</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command to add.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandRegistrationError" title="discord.ext.commands.CommandRegistrationError">**CommandRegistrationError**</a> – If the command or its alias is already registered by different command.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – If the command passed is not a subclass of <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>.

</dd></dl></dd>
</dl><dl><dt>remove_command(*name*, */*)<a href="#discord.ext.commands.GroupMixin.remove_command" title="Permalink to this definition">¶</a></dt>
<dd>

Remove a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> from the internal list of commands.

This could also be used as a way to remove aliases.

Changed in version 2.0: <code>name</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the command to remove.

</dd><dt>Returns</dt>
<dd>

The command that was removed. If the name is not valid then <code>None</code> is returned instead.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>*for ... in* walk_commands()<a href="#discord.ext.commands.GroupMixin.walk_commands" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all commands and subcommands.

Changed in version 1.4: Duplicates due to aliases are no longer returned

<dl><dt>Yields</dt>
<dd>

Union\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>, <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>] – A command or group from the internal list of commands.

</dd></dl></dd>
</dl><dl><dt>get_command(*name*, */*)<a href="#discord.ext.commands.GroupMixin.get_command" title="Permalink to this definition">¶</a></dt>
<dd>

Get a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> from the internal list of commands.

This could also be used as a way to get aliases.

The name could be fully qualified (e.g. <code>'foo bar'</code>) will get the subcommand <code>bar</code> of the group command <code>foo</code>. If a subcommand is not found then <code>None</code> is returned just as usual.

Changed in version 2.0: <code>name</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the command to get.

</dd><dt>Returns</dt>
<dd>

The command that was requested. If not found, returns <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl></dd>
</dl>

### HybridCommand ¶

Methods

- @ [after\_invoke](#discord.ext.commands.HybridCommand.after_invoke)
- @ [autocomplete](#discord.ext.commands.HybridCommand.autocomplete)
- @ [before\_invoke](#discord.ext.commands.HybridCommand.before_invoke)
- async [can\_run](#discord.ext.commands.HybridCommand.can_run)
- @ [error](#discord.ext.commands.HybridCommand.error)

<dl><dt>*class*discord.ext.commands.HybridCommand(**args*, ***kwargs*)<a href="#discord.ext.commands.HybridCommand" title="Permalink to this definition">¶</a></dt>
<dd>

A class that is both an application command and a regular text command.

This has the same parameters and attributes as a regular <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>. However, it also doubles as an <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Command" title="discord.app_commands.Command"><code>application command</code></a>. In order for this to work, the callbacks must have the same subset that is supported by application commands.

These are not created manually, instead they are created via the decorator or functional interface.

New in version 2.0.

<dl><dt>@after_invoke<a href="#discord.ext.commands.HybridCommand.after_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a post-invoke hook.

A post-invoke hook is called directly after the command is called. This makes it a useful function to clean-up database connections or any type of clean up required.

This post-invoke hook takes a sole parameter, a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

See <a href="#discord.ext.commands.Bot.after_invoke" title="discord.ext.commands.Bot.after_invoke"><code>Bot.after_invoke()</code></a> for more info.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the post-invoke hook.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@autocomplete(*name*)<a href="#discord.ext.commands.HybridCommand.autocomplete" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as an autocomplete prompt for a parameter.

This is the same as <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Command.autocomplete" title="discord.app_commands.Command.autocomplete"><code>autocomplete()</code></a>. It is only applicable for the application command and doesn’t do anything if the command is a regular command.

Note

Similar to the <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Command.autocomplete" title="discord.app_commands.Command.autocomplete"><code>autocomplete()</code></a> method, this takes <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a> as a parameter rather than a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The parameter name to register as autocomplete.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine or the parameter is not found or of an invalid type.

</dd></dl></dd>
</dl><dl><dt>@before_invoke<a href="#discord.ext.commands.HybridCommand.before_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a pre-invoke hook.

A pre-invoke hook is called directly before the command is called. This makes it a useful function to set up database connections or any type of set up required.

This pre-invoke hook takes a sole parameter, a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

See <a href="#discord.ext.commands.Bot.before_invoke" title="discord.ext.commands.Bot.before_invoke"><code>Bot.before_invoke()</code></a> for more info.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the pre-invoke hook.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@error<a href="#discord.ext.commands.HybridCommand.error" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a local error handler.

A local error handler is an <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> event limited to a single command. However, the <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> is still invoked afterwards as the catch-all.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the local error handler.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>*await* can_run(*ctx*, */*)<a href="#discord.ext.commands.HybridCommand.can_run" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Checks if the command can be executed by checking all the predicates inside the <a href="#discord.ext.commands.Command.checks" title="discord.ext.commands.Command.checks"><code>checks</code></a> attribute. This also checks whether the command is disabled.

Changed in version 1.3: Checks whether the command is disabled or not

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The ctx of the command currently being invoked.

</dd><dt>Raises</dt>
<dd>

<a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – Any command error that was raised during a check call will be propagated by this function.

</dd><dt>Returns</dt>
<dd>

A boolean indicating if the command can be invoked.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### HybridGroup ¶

Attributes

- [clean\_params](#discord.ext.commands.HybridGroup.clean_params)
- [cog\_name](#discord.ext.commands.HybridGroup.cog_name)
- [commands](#discord.ext.commands.HybridGroup.commands)
- [cooldown](#discord.ext.commands.HybridGroup.cooldown)
- [fallback](#discord.ext.commands.HybridGroup.fallback)
- [fallback\_locale](#discord.ext.commands.HybridGroup.fallback_locale)
- [full\_parent\_name](#discord.ext.commands.HybridGroup.full_parent_name)
- [parents](#discord.ext.commands.HybridGroup.parents)
- [qualified\_name](#discord.ext.commands.HybridGroup.qualified_name)
- [root\_parent](#discord.ext.commands.HybridGroup.root_parent)
- [short\_doc](#discord.ext.commands.HybridGroup.short_doc)
- [signature](#discord.ext.commands.HybridGroup.signature)

Methods

- def [add\_check](#discord.ext.commands.HybridGroup.add_check)
- def [add\_command](#discord.ext.commands.HybridGroup.add_command)
- @ [after\_invoke](#discord.ext.commands.HybridGroup.after_invoke)
- @ [autocomplete](#discord.ext.commands.HybridGroup.autocomplete)
- @ [before\_invoke](#discord.ext.commands.HybridGroup.before_invoke)
- async [can\_run](#discord.ext.commands.HybridGroup.can_run)
- @ [command](#discord.ext.commands.HybridGroup.command)
- def [copy](#discord.ext.commands.HybridGroup.copy)
- @ [error](#discord.ext.commands.HybridGroup.error)
- def [get\_command](#discord.ext.commands.HybridGroup.get_command)
- def [get\_cooldown\_retry\_after](#discord.ext.commands.HybridGroup.get_cooldown_retry_after)
- @ [group](#discord.ext.commands.HybridGroup.group)
- def [has\_error\_handler](#discord.ext.commands.HybridGroup.has_error_handler)
- def [is\_on\_cooldown](#discord.ext.commands.HybridGroup.is_on_cooldown)
- def [remove\_check](#discord.ext.commands.HybridGroup.remove_check)
- def [remove\_command](#discord.ext.commands.HybridGroup.remove_command)
- def [reset\_cooldown](#discord.ext.commands.HybridGroup.reset_cooldown)
- def [update](#discord.ext.commands.HybridGroup.update)
- def [walk\_commands](#discord.ext.commands.HybridGroup.walk_commands)

<dl><dt>*class*discord.ext.commands.HybridGroup(**args*, ***kwargs*)<a href="#discord.ext.commands.HybridGroup" title="Permalink to this definition">¶</a></dt>
<dd>

A class that is both an application command group and a regular text group.

This has the same parameters and attributes as a regular <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>. However, it also doubles as an <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Group" title="discord.app_commands.Group"><code>application command group</code></a>. Note that application commands groups cannot have callbacks associated with them, so the callback is only called if it’s not invoked as an application command.

Hybrid groups will always have <a href="#discord.ext.commands.Group.invoke_without_command" title="discord.ext.commands.Group.invoke_without_command"><code>Group.invoke_without_command</code></a> set to <code>True</code>.

These are not created manually, instead they are created via the decorator or functional interface.

New in version 2.0.

<dl><dt>fallback<a href="#discord.ext.commands.HybridGroup.fallback" title="Permalink to this definition">¶</a></dt>
<dd>

The command name to use as a fallback for the application command. Since application command groups cannot be invoked, this creates a subcommand within the group that can be invoked with the given group callback. If <code>None</code> then no fallback command is given. Defaults to <code>None</code>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>fallback_locale<a href="#discord.ext.commands.HybridGroup.fallback_locale" title="Permalink to this definition">¶</a></dt>
<dd>

The fallback command name’s locale string, if available.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]

</dd></dl></dd>
</dl><dl><dt>@after_invoke<a href="#discord.ext.commands.HybridGroup.after_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a post-invoke hook.

A post-invoke hook is called directly after the command is called. This makes it a useful function to clean-up database connections or any type of clean up required.

This post-invoke hook takes a sole parameter, a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

See <a href="#discord.ext.commands.Bot.after_invoke" title="discord.ext.commands.Bot.after_invoke"><code>Bot.after_invoke()</code></a> for more info.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the post-invoke hook.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@autocomplete(*name*)<a href="#discord.ext.commands.HybridGroup.autocomplete" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as an autocomplete prompt for a parameter.

This is the same as <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Command.autocomplete" title="discord.app_commands.Command.autocomplete"><code>autocomplete()</code></a>. It is only applicable for the application command and doesn’t do anything if the command is a regular command.

This is only available if the group has a fallback application command registered.

Note

Similar to the <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Command.autocomplete" title="discord.app_commands.Command.autocomplete"><code>autocomplete()</code></a> method, this takes <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a> as a parameter rather than a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The parameter name to register as autocomplete.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine or the parameter is not found or of an invalid type.

</dd></dl></dd>
</dl><dl><dt>@before_invoke<a href="#discord.ext.commands.HybridGroup.before_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a pre-invoke hook.

A pre-invoke hook is called directly before the command is called. This makes it a useful function to set up database connections or any type of set up required.

This pre-invoke hook takes a sole parameter, a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

See <a href="#discord.ext.commands.Bot.before_invoke" title="discord.ext.commands.Bot.before_invoke"><code>Bot.before_invoke()</code></a> for more info.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the pre-invoke hook.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@command(**args*, ***kwargs*)<a href="#discord.ext.commands.HybridGroup.command" title="Permalink to this definition">¶</a></dt>
<dd>

A shortcut decorator that invokes <a href="#discord.ext.commands.hybrid_command" title="discord.ext.commands.hybrid_command"><code>hybrid_command()</code></a> and adds it to the internal command list via <a href="#discord.ext.commands.HybridGroup.add_command" title="discord.ext.commands.HybridGroup.add_command"><code>add_command()</code></a>.

<dl><dt>Returns</dt>
<dd>

A decorator that converts the provided method into a Command, adds it to the bot, then returns it.

</dd><dt>Return type</dt>
<dd>

Callable\[…, <a href="#discord.ext.commands.HybridCommand" title="discord.ext.commands.HybridCommand"><code>HybridCommand</code></a>]

</dd></dl></dd>
</dl><dl><dt>@error<a href="#discord.ext.commands.HybridGroup.error" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a local error handler.

A local error handler is an <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> event limited to a single command. However, the <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> is still invoked afterwards as the catch-all.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**coro** (<a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>) – The coroutine to register as the local error handler.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The coroutine passed is not actually a coroutine.

</dd></dl></dd>
</dl><dl><dt>@group(**args*, ***kwargs*)<a href="#discord.ext.commands.HybridGroup.group" title="Permalink to this definition">¶</a></dt>
<dd>

A shortcut decorator that invokes <a href="#discord.ext.commands.hybrid_group" title="discord.ext.commands.hybrid_group"><code>hybrid_group()</code></a> and adds it to the internal command list via <a href="#discord.ext.commands.GroupMixin.add_command" title="discord.ext.commands.GroupMixin.add_command"><code>add_command()</code></a>.

<dl><dt>Returns</dt>
<dd>

A decorator that converts the provided method into a Group, adds it to the bot, then returns it.

</dd><dt>Return type</dt>
<dd>

Callable\[…, <a href="#discord.ext.commands.HybridGroup" title="discord.ext.commands.HybridGroup"><code>HybridGroup</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* can_run(*ctx*, */*)<a href="#discord.ext.commands.HybridGroup.can_run" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Checks if the command can be executed by checking all the predicates inside the <a href="#discord.ext.commands.Command.checks" title="discord.ext.commands.Command.checks"><code>checks</code></a> attribute. This also checks whether the command is disabled.

Changed in version 1.3: Checks whether the command is disabled or not

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The ctx of the command currently being invoked.

</dd><dt>Raises</dt>
<dd>

<a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – Any command error that was raised during a check call will be propagated by this function.

</dd><dt>Returns</dt>
<dd>

A boolean indicating if the command can be invoked.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>add_check(*func*, */*)<a href="#discord.ext.commands.HybridGroup.add_check" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a check to the command.

This is the non-decorator interface to <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a>.

New in version 1.3.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

See also

The <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> decorator

<dl><dt>Parameters</dt>
<dd>

**func** – The function that will be used as a check.

</dd></dl></dd>
</dl><dl><dt>add_command(*command*, */*)<a href="#discord.ext.commands.HybridGroup.add_command" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a <a href="#discord.ext.commands.HybridCommand" title="discord.ext.commands.HybridCommand"><code>HybridCommand</code></a> into the internal list of commands.

This is usually not called, instead the <a href="#discord.ext.commands.GroupMixin.command" title="discord.ext.commands.GroupMixin.command"><code>command()</code></a> or <a href="#discord.ext.commands.GroupMixin.group" title="discord.ext.commands.GroupMixin.group"><code>group()</code></a> shortcut decorators are used instead.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.HybridCommand" title="discord.ext.commands.HybridCommand"><code>HybridCommand</code></a>) – The command to add.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandRegistrationError" title="discord.ext.commands.CommandRegistrationError">**CommandRegistrationError**</a> – If the command or its alias is already registered by different command.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – If the command passed is not a subclass of <a href="#discord.ext.commands.HybridCommand" title="discord.ext.commands.HybridCommand"><code>HybridCommand</code></a>.

</dd></dl></dd>
</dl><dl><dt>*property*clean_params<a href="#discord.ext.commands.HybridGroup.clean_params" title="Permalink to this definition">¶</a></dt>
<dd>

Dict\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.ext.commands.Parameter" title="discord.ext.commands.Parameter"><code>Parameter</code></a>]: Retrieves the parameter dictionary without the context or self parameters.

Useful for inspecting signature.

</dd></dl><dl><dt>*property*cog_name<a href="#discord.ext.commands.HybridGroup.cog_name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the cog this command belongs to, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*commands<a href="#discord.ext.commands.HybridGroup.commands" title="Permalink to this definition">¶</a></dt>
<dd>

A unique set of commands without aliases that are registered.

<dl><dt>Type</dt>
<dd>

Set\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*cooldown<a href="#discord.ext.commands.HybridGroup.cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

The cooldown of a command when invoked or <code>None</code> if the command doesn’t have a registered cooldown.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Cooldown" title="discord.app_commands.Cooldown"><code>Cooldown</code></a>]

</dd></dl></dd>
</dl><dl><dt>copy()<a href="#discord.ext.commands.HybridGroup.copy" title="Permalink to this definition">¶</a></dt>
<dd>

Creates a copy of this <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>.

<dl><dt>Returns</dt>
<dd>

A new instance of this group.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*full_parent_name<a href="#discord.ext.commands.HybridGroup.full_parent_name" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the fully qualified parent command name.

This the base command name required to execute it. For example, in <code>?one two three</code> the parent name would be <code>one two</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>get_command(*name*, */*)<a href="#discord.ext.commands.HybridGroup.get_command" title="Permalink to this definition">¶</a></dt>
<dd>

Get a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> from the internal list of commands.

This could also be used as a way to get aliases.

The name could be fully qualified (e.g. <code>'foo bar'</code>) will get the subcommand <code>bar</code> of the group command <code>foo</code>. If a subcommand is not found then <code>None</code> is returned just as usual.

Changed in version 2.0: <code>name</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the command to get.

</dd><dt>Returns</dt>
<dd>

The command that was requested. If not found, returns <code>None</code>.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_cooldown_retry_after(*ctx*, */*)<a href="#discord.ext.commands.HybridGroup.get_cooldown_retry_after" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the amount of seconds before this command can be tried again.

New in version 1.4.

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context to retrieve the cooldown from.

</dd><dt>Returns</dt>
<dd>

The amount of time left on this command’s cooldown in seconds. If this is <code>0.0</code> then the command isn’t on cooldown.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>

</dd></dl></dd>
</dl><dl><dt>has_error_handler()<a href="#discord.ext.commands.HybridGroup.has_error_handler" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Checks whether the command has an error handler registered.

New in version 1.7.

</dd></dl><dl><dt>is_on_cooldown(*ctx*, */*)<a href="#discord.ext.commands.HybridGroup.is_on_cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

Checks whether the command is currently on cooldown.

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context to use when checking the commands cooldown status.

</dd><dt>Returns</dt>
<dd>

A boolean indicating if the command is on cooldown.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*parents<a href="#discord.ext.commands.HybridGroup.parents" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the parents of this command.

If the command has no parents then it returns an empty <a href="https://docs.python.org/3/library/stdtypes.html#list" title="(in Python v3.14)"><code>list</code></a>.

For example in commands <code>?a b c test</code>, the parents are <code>[c, b, a]</code>.

New in version 1.1.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*qualified_name<a href="#discord.ext.commands.HybridGroup.qualified_name" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the fully qualified command name.

This is the full parent name with the command name as well. For example, in <code>?one two three</code> the qualified name would be <code>one two three</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>remove_check(*func*, */*)<a href="#discord.ext.commands.HybridGroup.remove_check" title="Permalink to this definition">¶</a></dt>
<dd>

Removes a check from the command.

This function is idempotent and will not raise an exception if the function is not in the command’s checks.

New in version 1.3.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**func** – The function to remove from the checks.

</dd></dl></dd>
</dl><dl><dt>reset_cooldown(*ctx*, */*)<a href="#discord.ext.commands.HybridGroup.reset_cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

Resets the cooldown on this command.

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context to reset the cooldown under.

</dd></dl></dd>
</dl><dl><dt>*property*root_parent<a href="#discord.ext.commands.HybridGroup.root_parent" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the root parent of this command.

If the command has no parents then it returns <code>None</code>.

For example in commands <code>?a b c test</code>, the root parent is <code>a</code>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*short_doc<a href="#discord.ext.commands.HybridGroup.short_doc" title="Permalink to this definition">¶</a></dt>
<dd>

Gets the “short” documentation of a command.

By default, this is the <a href="#discord.ext.commands.Command.brief" title="discord.ext.commands.Command.brief"><code>brief</code></a> attribute. If that lookup leads to an empty string then the first line of the <a href="#discord.ext.commands.Command.help" title="discord.ext.commands.Command.help"><code>help</code></a> attribute is used instead.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*signature<a href="#discord.ext.commands.HybridGroup.signature" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a POSIX-like signature useful for help command output.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>update(***kwargs*)<a href="#discord.ext.commands.HybridGroup.update" title="Permalink to this definition">¶</a></dt>
<dd>

Updates <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> instance with updated attribute.

This works similarly to the <a href="#discord.ext.commands.command" title="discord.ext.commands.command"><code>command()</code></a> decorator in terms of parameters in that they are passed to the <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> or subclass constructors, sans the name and callback.

</dd></dl><dl><dt>*for ... in* walk_commands()<a href="#discord.ext.commands.HybridGroup.walk_commands" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through all commands and subcommands.

Changed in version 1.4: Duplicates due to aliases are no longer returned

<dl><dt>Yields</dt>
<dd>

Union\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>, <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>] – A command or group from the internal list of commands.

</dd></dl></dd>
</dl><dl><dt>remove_command(*name*, */*)<a href="#discord.ext.commands.HybridGroup.remove_command" title="Permalink to this definition">¶</a></dt>
<dd>

Remove a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> from the internal list of commands.

This could also be used as a way to remove aliases.

Changed in version 2.0: <code>name</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the command to remove.

</dd><dt>Returns</dt>
<dd>

The command that was removed. If the name is not valid then <code>None</code> is returned instead.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl></dd>
</dl>

## Cogs ¶

### Cog ¶

Attributes

- [app\_command](#discord.ext.commands.Cog.app_command)
- [description](#discord.ext.commands.Cog.description)
- [qualified\_name](#discord.ext.commands.Cog.qualified_name)

Methods

- cls [Cog.listener](#discord.ext.commands.Cog.listener)
- def [bot\_check](#discord.ext.commands.Cog.bot_check)
- def [bot\_check\_once](#discord.ext.commands.Cog.bot_check_once)
- async [cog\_after\_invoke](#discord.ext.commands.Cog.cog_after_invoke)
- async [cog\_app\_command\_error](#discord.ext.commands.Cog.cog_app_command_error)
- async [cog\_before\_invoke](#discord.ext.commands.Cog.cog_before_invoke)
- def [cog\_check](#discord.ext.commands.Cog.cog_check)
- async [cog\_command\_error](#discord.ext.commands.Cog.cog_command_error)
- async [cog\_load](#discord.ext.commands.Cog.cog_load)
- async [cog\_unload](#discord.ext.commands.Cog.cog_unload)
- def [get\_app\_commands](#discord.ext.commands.Cog.get_app_commands)
- def [get\_commands](#discord.ext.commands.Cog.get_commands)
- def [get\_listeners](#discord.ext.commands.Cog.get_listeners)
- def [has\_app\_command\_error\_handler](#discord.ext.commands.Cog.has_app_command_error_handler)
- def [has\_error\_handler](#discord.ext.commands.Cog.has_error_handler)
- def [interaction\_check](#discord.ext.commands.Cog.interaction_check)
- def [walk\_app\_commands](#discord.ext.commands.Cog.walk_app_commands)
- def [walk\_commands](#discord.ext.commands.Cog.walk_commands)

<dl><dt>*class*discord.ext.commands.Cog(**args*, ***kwargs*)<a href="#discord.ext.commands.Cog" title="Permalink to this definition">¶</a></dt>
<dd>

The base class that all cogs must inherit from.

A cog is a collection of commands, listeners, and optional state to help group commands together. More information on them can be found on the <a href="https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html#ext-commands-cogs">Cogs</a> page.

When inheriting from this class, the options shown in <a href="#discord.ext.commands.CogMeta" title="discord.ext.commands.CogMeta"><code>CogMeta</code></a> are equally valid here.

<dl><dt>get_commands()<a href="#discord.ext.commands.Cog.get_commands" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the commands that are defined inside this cog.

This does *not* include <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Command" title="discord.app_commands.Command"><code>discord.app_commands.Command</code></a> or <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Group" title="discord.app_commands.Group"><code>discord.app_commands.Group</code></a> instances.

<dl><dt>Returns</dt>
<dd>

A <a href="https://docs.python.org/3/library/stdtypes.html#list" title="(in Python v3.14)"><code>list</code></a> of <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>s that are defined inside this cog, not including subcommands.

</dd><dt>Return type</dt>
<dd>

List\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_app_commands()<a href="#discord.ext.commands.Cog.get_app_commands" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the app commands that are defined inside this cog.

<dl><dt>Returns</dt>
<dd>

A <a href="https://docs.python.org/3/library/stdtypes.html#list" title="(in Python v3.14)"><code>list</code></a> of <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Command" title="discord.app_commands.Command"><code>discord.app_commands.Command</code></a>s and <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Group" title="discord.app_commands.Group"><code>discord.app_commands.Group</code></a>s that are defined inside this cog, not including subcommands.

</dd><dt>Return type</dt>
<dd>

List\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Command" title="discord.app_commands.Command"><code>discord.app_commands.Command</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Group" title="discord.app_commands.Group"><code>discord.app_commands.Group</code></a>]]

</dd></dl></dd>
</dl><dl><dt>*property*qualified_name<a href="#discord.ext.commands.Cog.qualified_name" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the cog’s specified name, not the class name.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*description<a href="#discord.ext.commands.Cog.description" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the cog’s description, typically the cleaned docstring.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*for ... in* walk_commands()<a href="#discord.ext.commands.Cog.walk_commands" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through this cog’s commands and subcommands.

<dl><dt>Yields</dt>
<dd>

Union\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>, <a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>] – A command or group from the cog.

</dd></dl></dd>
</dl><dl><dt>*for ... in* walk_app_commands()<a href="#discord.ext.commands.Cog.walk_app_commands" title="Permalink to this definition">¶</a></dt>
<dd>

An iterator that recursively walks through this cog’s app commands and subcommands.

<dl><dt>Yields</dt>
<dd>

Union\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Command" title="discord.app_commands.Command"><code>discord.app_commands.Command</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Group" title="discord.app_commands.Group"><code>discord.app_commands.Group</code></a>] – An app command or group from the cog.

</dd></dl></dd>
</dl><dl><dt>*property*app_command<a href="#discord.ext.commands.Cog.app_command" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the associated group with this cog.

This is only available if inheriting from <a href="#discord.ext.commands.GroupCog" title="discord.ext.commands.GroupCog"><code>GroupCog</code></a>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Group" title="discord.app_commands.Group"><code>discord.app_commands.Group</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_listeners()<a href="#discord.ext.commands.Cog.get_listeners" title="Permalink to this definition">¶</a></dt>
<dd>

Returns a <a href="https://docs.python.org/3/library/stdtypes.html#list" title="(in Python v3.14)"><code>list</code></a> of (name, function) listener pairs that are defined in this cog.

<dl><dt>Returns</dt>
<dd>

The listeners defined in this cog.

</dd><dt>Return type</dt>
<dd>

List\[Tuple\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>]]

</dd></dl></dd>
</dl><dl><dt>*classmethod* listener(*name=...*)<a href="#discord.ext.commands.Cog.listener" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that marks a function as a listener.

This is the cog equivalent of <a href="#discord.ext.commands.Bot.listen" title="discord.ext.commands.Bot.listen"><code>Bot.listen()</code></a>.

<dl><dt>Parameters</dt>
<dd>

**name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The name of the event being listened to. If not provided, it defaults to the function’s name.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The function is not a coroutine function or a string was not passed as the name.

</dd></dl></dd>
</dl><dl><dt>has_error_handler()<a href="#discord.ext.commands.Cog.has_error_handler" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Checks whether the cog has an error handler.

New in version 1.7.

</dd></dl><dl><dt>has_app_command_error_handler()<a href="#discord.ext.commands.Cog.has_app_command_error_handler" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>: Checks whether the cog has an app error handler.

New in version 2.1.

</dd></dl><dl><dt>*await* cog_load()<a href="#discord.ext.commands.Cog.cog_load" title="Permalink to this definition">¶</a></dt>
<dd>

This function *could be a* <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A special method that is called when the cog gets loaded.

Subclasses must replace this if they want special asynchronous loading behaviour. Note that the <code>__init__</code> special method does not allow asynchronous code to run inside it, thus this is helpful for setting up code that needs to be asynchronous.

New in version 2.0.

</dd></dl><dl><dt>*await* cog_unload()<a href="#discord.ext.commands.Cog.cog_unload" title="Permalink to this definition">¶</a></dt>
<dd>

This function *could be a* <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A special method that is called when the cog gets removed.

Subclasses must replace this if they want special unloading behaviour.

Exceptions raised in this method are ignored during extension unloading.

Changed in version 2.0: This method can now be a <a href="https://docs.python.org/3/glossary.html#term-coroutine" title="(in Python v3.14)">coroutine</a>.

</dd></dl><dl><dt>bot_check_once(*ctx*)<a href="#discord.ext.commands.Cog.bot_check_once" title="Permalink to this definition">¶</a></dt>
<dd>

A special method that registers as a <a href="#discord.ext.commands.Bot.check_once" title="discord.ext.commands.Bot.check_once"><code>Bot.check_once()</code></a> check.

This function **can** be a coroutine and must take a sole parameter, <code>ctx</code>, to represent the <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

</dd></dl><dl><dt>bot_check(*ctx*)<a href="#discord.ext.commands.Cog.bot_check" title="Permalink to this definition">¶</a></dt>
<dd>

A special method that registers as a <a href="#discord.ext.commands.Bot.check" title="discord.ext.commands.Bot.check"><code>Bot.check()</code></a> check.

This function **can** be a coroutine and must take a sole parameter, <code>ctx</code>, to represent the <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

</dd></dl><dl><dt>cog_check(*ctx*)<a href="#discord.ext.commands.Cog.cog_check" title="Permalink to this definition">¶</a></dt>
<dd>

A special method that registers as a <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> for every command and subcommand in this cog.

This function **can** be a coroutine and must take a sole parameter, <code>ctx</code>, to represent the <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>.

</dd></dl><dl><dt>interaction_check(*interaction*, */*)<a href="#discord.ext.commands.Cog.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

A special method that registers as a <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.check" title="discord.app_commands.check"><code>discord.app_commands.check()</code></a> for every app command and subcommand in this cog.

This function **can** be a coroutine and must take a sole parameter, <code>interaction</code>, to represent the <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>.

New in version 2.0.

</dd></dl><dl><dt>*await* cog_command_error(*ctx*, *error*)<a href="#discord.ext.commands.Cog.cog_command_error" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A special method that is called whenever an error is dispatched inside this cog.

This is similar to <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> except only applying to the commands inside this cog.

This **must** be a coroutine.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context where the error happened.
- **error** (<a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>) – The error that happened.

</dd></dl></dd>
</dl><dl><dt>*await* cog_app_command_error(*interaction*, *error*)<a href="#discord.ext.commands.Cog.cog_app_command_error" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A special method that is called whenever an error within an application command is dispatched inside this cog.

This is similar to <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.CommandTree.on_error" title="discord.app_commands.CommandTree.on_error"><code>discord.app_commands.CommandTree.on_error()</code></a> except only applying to the application commands inside this cog.

This **must** be a coroutine.

<dl><dt>Parameters</dt>
<dd>

- **interaction** (<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>) – The interaction that is being handled.
- **error** (<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>) – The exception that was raised.

</dd></dl></dd>
</dl><dl><dt>*await* cog_before_invoke(*ctx*)<a href="#discord.ext.commands.Cog.cog_before_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A special method that acts as a cog local pre-invoke hook.

This is similar to <a href="#discord.ext.commands.Command.before_invoke" title="discord.ext.commands.Command.before_invoke"><code>Command.before_invoke()</code></a>.

This **must** be a coroutine.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context.

</dd></dl></dd>
</dl><dl><dt>*await* cog_after_invoke(*ctx*)<a href="#discord.ext.commands.Cog.cog_after_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A special method that acts as a cog local post-invoke hook.

This is similar to <a href="#discord.ext.commands.Command.after_invoke" title="discord.ext.commands.Command.after_invoke"><code>Command.after_invoke()</code></a>.

This **must** be a coroutine.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context.

</dd></dl></dd>
</dl></dd>
</dl>

### GroupCog ¶

Methods

- def [interaction\_check](#discord.ext.commands.GroupCog.interaction_check)

<dl><dt>*class*discord.ext.commands.GroupCog(**args*, ***kwargs*)<a href="#discord.ext.commands.GroupCog" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a cog that also doubles as a parent <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Group" title="discord.app_commands.Group"><code>discord.app_commands.Group</code></a> for the application commands defined within it.

This inherits from <a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a> and the options in <a href="#discord.ext.commands.CogMeta" title="discord.ext.commands.CogMeta"><code>CogMeta</code></a> also apply to this. See the <a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a> documentation for methods.

Decorators such as <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.guild_only" title="discord.app_commands.guild_only"><code>guild_only()</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.guilds" title="discord.app_commands.guilds"><code>guilds()</code></a>, and <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.default_permissions" title="discord.app_commands.default_permissions"><code>default_permissions()</code></a> will apply to the group if used on top of the cog.

Hybrid commands will also be added to the Group, giving the ability to categorize slash commands into groups, while keeping the prefix-style command as a root-level command.

For example:

```
from discord import app_commands
from discord.ext import commands

@app_commands.guild_only()
class MyCog(commands.GroupCog, group_name='my-cog'):
    pass

```

New in version 2.0.

<dl><dt>interaction_check(*interaction*, */*)<a href="#discord.ext.commands.GroupCog.interaction_check" title="Permalink to this definition">¶</a></dt>
<dd>

A special method that registers as a <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.check" title="discord.app_commands.check"><code>discord.app_commands.check()</code></a> for every app command and subcommand in this cog.

This function **can** be a coroutine and must take a sole parameter, <code>interaction</code>, to represent the <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>.

New in version 2.0.

</dd></dl></dd>
</dl>

### CogMeta ¶

Attributes

- [command\_attrs](#discord.ext.commands.CogMeta.command_attrs)
- [description](#discord.ext.commands.CogMeta.description)
- [group\_auto\_locale\_strings](#discord.ext.commands.CogMeta.group_auto_locale_strings)
- [group\_description](#discord.ext.commands.CogMeta.group_description)
- [group\_extras](#discord.ext.commands.CogMeta.group_extras)
- [group\_name](#discord.ext.commands.CogMeta.group_name)
- [group\_nsfw](#discord.ext.commands.CogMeta.group_nsfw)
- [name](#discord.ext.commands.CogMeta.name)

<dl><dt>*class*discord.ext.commands.CogMeta(**args*, ***kwargs*)<a href="#discord.ext.commands.CogMeta" title="Permalink to this definition">¶</a></dt>
<dd>

A metaclass for defining a cog.

Note that you should probably not use this directly. It is exposed purely for documentation purposes along with making custom metaclasses to intermix with other metaclasses such as the <a href="https://docs.python.org/3/library/abc.html#abc.ABCMeta" title="(in Python v3.14)"><code>abc.ABCMeta</code></a> metaclass.

For example, to create an abstract cog mixin class, the following would be done.

```
import abc

class CogABCMeta(commands.CogMeta, abc.ABCMeta):
    pass

class SomeMixin(metaclass=abc.ABCMeta):
    pass

class SomeCogMixin(SomeMixin, commands.Cog, metaclass=CogABCMeta):
    pass

```

Note

When passing an attribute of a metaclass that is documented below, note that you must pass it as a keyword-only argument to the class creation like the following example:

```
class MyCog(commands.Cog, name='My Cog'):
    pass

```

<dl><dt>name<a href="#discord.ext.commands.CogMeta.name" title="Permalink to this definition">¶</a></dt>
<dd>

The cog name. By default, it is the name of the class with no modification.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.ext.commands.CogMeta.description" title="Permalink to this definition">¶</a></dt>
<dd>

The cog description. By default, it is the cleaned docstring of the class.

New in version 1.6.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>command_attrs<a href="#discord.ext.commands.CogMeta.command_attrs" title="Permalink to this definition">¶</a></dt>
<dd>

A list of attributes to apply to every command inside this cog. The dictionary is passed into the <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> options at <code>__init__</code>. If you specify attributes inside the command attribute in the class, it will override the one specified inside this attribute. For example:

```
class MyCog(commands.Cog, command_attrs=dict(hidden=True)):
    @commands.command()
    async def foo(self, ctx):
        pass # hidden -> True

    @commands.command(hidden=False)
    async def bar(self, ctx):
        pass # hidden -> False

```

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

</dd></dl></dd>
</dl><dl><dt>group_name<a href="#discord.ext.commands.CogMeta.group_name" title="Permalink to this definition">¶</a></dt>
<dd>

The group name of a cog. This is only applicable for <a href="#discord.ext.commands.GroupCog" title="discord.ext.commands.GroupCog"><code>GroupCog</code></a> instances. By default, it’s the same value as <a href="#discord.ext.commands.CogMeta.name" title="discord.ext.commands.CogMeta.name"><code>name</code></a>.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]

</dd></dl></dd>
</dl><dl><dt>group_description<a href="#discord.ext.commands.CogMeta.group_description" title="Permalink to this definition">¶</a></dt>
<dd>

The group description of a cog. This is only applicable for <a href="#discord.ext.commands.GroupCog" title="discord.ext.commands.GroupCog"><code>GroupCog</code></a> instances. By default, it’s the same value as <a href="#discord.ext.commands.CogMeta.description" title="discord.ext.commands.CogMeta.description"><code>description</code></a>.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a>]

</dd></dl></dd>
</dl><dl><dt>group_nsfw<a href="#discord.ext.commands.CogMeta.group_nsfw" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the application command group is NSFW. This is only applicable for <a href="#discord.ext.commands.GroupCog" title="discord.ext.commands.GroupCog"><code>GroupCog</code></a> instances. By default, it’s <code>False</code>.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>group_auto_locale_strings<a href="#discord.ext.commands.CogMeta.group_auto_locale_strings" title="Permalink to this definition">¶</a></dt>
<dd>

If this is set to <code>True</code>, then all translatable strings will implicitly be wrapped into <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.locale_str" title="discord.app_commands.locale_str"><code>locale_str</code></a> rather than <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>. Defaults to <code>True</code>.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>group_extras<a href="#discord.ext.commands.CogMeta.group_extras" title="Permalink to this definition">¶</a></dt>
<dd>

A dictionary that can be used to store extraneous data. This is only applicable for <a href="#discord.ext.commands.GroupCog" title="discord.ext.commands.GroupCog"><code>GroupCog</code></a> instances. The library will not touch any values or keys within this dictionary.

New in version 2.1.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

## Help Commands ¶

### HelpCommand ¶

Attributes

- [cog](#discord.ext.commands.HelpCommand.cog)
- [command\_attrs](#discord.ext.commands.HelpCommand.command_attrs)
- [context](#discord.ext.commands.HelpCommand.context)
- [invoked\_with](#discord.ext.commands.HelpCommand.invoked_with)
- [show\_hidden](#discord.ext.commands.HelpCommand.show_hidden)
- [verify\_checks](#discord.ext.commands.HelpCommand.verify_checks)

Methods

- def [add\_check](#discord.ext.commands.HelpCommand.add_check)
- async [command\_callback](#discord.ext.commands.HelpCommand.command_callback)
- def [command\_not\_found](#discord.ext.commands.HelpCommand.command_not_found)
- async [filter\_commands](#discord.ext.commands.HelpCommand.filter_commands)
- def [get\_bot\_mapping](#discord.ext.commands.HelpCommand.get_bot_mapping)
- def [get\_command\_signature](#discord.ext.commands.HelpCommand.get_command_signature)
- def [get\_destination](#discord.ext.commands.HelpCommand.get_destination)
- def [get\_max\_size](#discord.ext.commands.HelpCommand.get_max_size)
- async [on\_help\_command\_error](#discord.ext.commands.HelpCommand.on_help_command_error)
- async [prepare\_help\_command](#discord.ext.commands.HelpCommand.prepare_help_command)
- def [remove\_check](#discord.ext.commands.HelpCommand.remove_check)
- def [remove\_mentions](#discord.ext.commands.HelpCommand.remove_mentions)
- async [send\_bot\_help](#discord.ext.commands.HelpCommand.send_bot_help)
- async [send\_cog\_help](#discord.ext.commands.HelpCommand.send_cog_help)
- async [send\_command\_help](#discord.ext.commands.HelpCommand.send_command_help)
- async [send\_error\_message](#discord.ext.commands.HelpCommand.send_error_message)
- async [send\_group\_help](#discord.ext.commands.HelpCommand.send_group_help)
- def [subcommand\_not\_found](#discord.ext.commands.HelpCommand.subcommand_not_found)

<dl><dt>*class*discord.ext.commands.HelpCommand(**args*, ***kwargs*)<a href="#discord.ext.commands.HelpCommand" title="Permalink to this definition">¶</a></dt>
<dd>

The base implementation for help command formatting.

Note

Internally instances of this class are deep copied every time the command itself is invoked to prevent a race condition mentioned in <a href="https://github.com/Rapptz/discord.py/issues/2123">GH-2123</a>.

This means that relying on the state of this class to be the same between command invocations would not work as expected.

<dl><dt>context<a href="#discord.ext.commands.HelpCommand.context" title="Permalink to this definition">¶</a></dt>
<dd>

The context that invoked this help formatter. This is generally set after the help command assigned, <a href="#discord.ext.commands.HelpCommand.command_callback" title="discord.ext.commands.HelpCommand.command_callback"><code>command_callback()</code></a>, has been called.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>]

</dd></dl></dd>
</dl><dl><dt>show_hidden<a href="#discord.ext.commands.HelpCommand.show_hidden" title="Permalink to this definition">¶</a></dt>
<dd>

Specifies if hidden commands should be shown in the output. Defaults to <code>False</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>verify_checks<a href="#discord.ext.commands.HelpCommand.verify_checks" title="Permalink to this definition">¶</a></dt>
<dd>

Specifies if commands should have their <a href="#discord.ext.commands.Command.checks" title="discord.ext.commands.Command.checks"><code>Command.checks</code></a> called and verified. If <code>True</code>, always calls <a href="#discord.ext.commands.Command.checks" title="discord.ext.commands.Command.checks"><code>Command.checks</code></a>. If <code>None</code>, only calls <a href="#discord.ext.commands.Command.checks" title="discord.ext.commands.Command.checks"><code>Command.checks</code></a> in a guild setting. If <code>False</code>, never calls <a href="#discord.ext.commands.Command.checks" title="discord.ext.commands.Command.checks"><code>Command.checks</code></a>. Defaults to <code>True</code>.

Changed in version 1.7.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]

</dd></dl></dd>
</dl><dl><dt>command_attrs<a href="#discord.ext.commands.HelpCommand.command_attrs" title="Permalink to this definition">¶</a></dt>
<dd>

A dictionary of options to pass in for the construction of the help command. This allows you to change the command behaviour without actually changing the implementation of the command. The attributes will be the same as the ones passed in the <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> constructor.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

</dd></dl></dd>
</dl><dl><dt>add_check(*func*, */*)<a href="#discord.ext.commands.HelpCommand.add_check" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a check to the help command.

New in version 1.4.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

See also

The <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> decorator

<dl><dt>Parameters</dt>
<dd>

**func** – The function that will be used as a check.

</dd></dl></dd>
</dl><dl><dt>remove_check(*func*, */*)<a href="#discord.ext.commands.HelpCommand.remove_check" title="Permalink to this definition">¶</a></dt>
<dd>

Removes a check from the help command.

This function is idempotent and will not raise an exception if the function is not in the command’s checks.

New in version 1.4.

Changed in version 2.0: <code>func</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**func** – The function to remove from the checks.

</dd></dl></dd>
</dl><dl><dt>get_bot_mapping()<a href="#discord.ext.commands.HelpCommand.get_bot_mapping" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the bot mapping passed to <a href="#discord.ext.commands.HelpCommand.send_bot_help" title="discord.ext.commands.HelpCommand.send_bot_help"><code>send_bot_help()</code></a>.

</dd></dl><dl><dt>*property*invoked_with<a href="#discord.ext.commands.HelpCommand.invoked_with" title="Permalink to this definition">¶</a></dt>
<dd>

Similar to <a href="#discord.ext.commands.Context.invoked_with" title="discord.ext.commands.Context.invoked_with"><code>Context.invoked_with</code></a> except properly handles the case where <a href="#discord.ext.commands.Context.send_help" title="discord.ext.commands.Context.send_help"><code>Context.send_help()</code></a> is used.

If the help command was used regularly then this returns the <a href="#discord.ext.commands.Context.invoked_with" title="discord.ext.commands.Context.invoked_with"><code>Context.invoked_with</code></a> attribute. Otherwise, if it the help command was called using <a href="#discord.ext.commands.Context.send_help" title="discord.ext.commands.Context.send_help"><code>Context.send_help()</code></a> then it returns the internal command name of the help command.

<dl><dt>Returns</dt>
<dd>

The command name that triggered this invocation.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_command_signature(*command*, */*)<a href="#discord.ext.commands.HelpCommand.get_command_signature" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the signature portion of the help page.

Changed in version 2.0: <code>command</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command to get the signature of.

</dd><dt>Returns</dt>
<dd>

The signature for the command.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>remove_mentions(*string*, */*)<a href="#discord.ext.commands.HelpCommand.remove_mentions" title="Permalink to this definition">¶</a></dt>
<dd>

Removes mentions from the string to prevent abuse.

This includes <code>@everyone</code>, <code>@here</code>, member mentions and role mentions.

Changed in version 2.0: <code>string</code> parameter is now positional-only.

<dl><dt>Returns</dt>
<dd>

The string with mentions removed.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*cog<a href="#discord.ext.commands.HelpCommand.cog" title="Permalink to this definition">¶</a></dt>
<dd>

A property for retrieving or setting the cog for the help command.

When a cog is set for the help command, it is as-if the help command belongs to that cog. All cog special methods will apply to the help command and it will be automatically unset on unload.

To unbind the cog from the help command, you can set it to <code>None</code>.

<dl><dt>Returns</dt>
<dd>

The cog that is currently set for the help command.

</dd><dt>Return type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>]

</dd></dl></dd>
</dl><dl><dt>command_not_found(*string*, */*)<a href="#discord.ext.commands.HelpCommand.command_not_found" title="Permalink to this definition">¶</a></dt>
<dd>

This function *could be a* <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A method called when a command is not found in the help command. This is useful to override for i18n.

Defaults to <code>No command called {0} found.</code>

Changed in version 2.0: <code>string</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**string** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The string that contains the invalid command. Note that this has had mentions removed to prevent abuse.

</dd><dt>Returns</dt>
<dd>

The string to use when a command has not been found.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>subcommand_not_found(*command*, *string*, */*)<a href="#discord.ext.commands.HelpCommand.subcommand_not_found" title="Permalink to this definition">¶</a></dt>
<dd>

This function *could be a* <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A method called when a command did not have a subcommand requested in the help command. This is useful to override for i18n.

Defaults to either:

- <dl><dt><code>'Command "{command.qualified_name}" has no subcommands.'</code></dt><dd>
  - If there is no subcommand in the <code>command</code> parameter.</dd></dl>
- <dl><dt><code>'Command "{command.qualified_name}" has no subcommand named {string}'</code></dt><dd>
  - If the <code>command</code> parameter has subcommands but not one named <code>string</code>.</dd></dl>

Changed in version 2.0: <code>command</code> and <code>string</code> parameters are now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command that did not have the subcommand requested.
- **string** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The string that contains the invalid subcommand. Note that this has had mentions removed to prevent abuse.

</dd><dt>Returns</dt>
<dd>

The string to use when the command did not have the subcommand requested.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* filter_commands(*commands*, */*, ***, *sort=False*, *key=None*)<a href="#discord.ext.commands.HelpCommand.filter_commands" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Returns a filtered list of commands and optionally sorts them.

This takes into account the <a href="#discord.ext.commands.HelpCommand.verify_checks" title="discord.ext.commands.HelpCommand.verify_checks"><code>verify_checks</code></a> and <a href="#discord.ext.commands.HelpCommand.show_hidden" title="discord.ext.commands.HelpCommand.show_hidden"><code>show_hidden</code></a> attributes.

Changed in version 2.0: <code>commands</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **commands** (Iterable\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]) – An iterable of commands that are getting filtered.
- **sort** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to sort the result.
- **key** (Optional\[Callable\[\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>], Any]]) – An optional key function to pass to <a href="https://docs.python.org/3/library/functions.html#sorted" title="(in Python v3.14)"><code>sorted()</code></a> that takes a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> as its sole parameter. If <code>sort</code> is passed as <code>True</code> then this will default as the command name.

</dd><dt>Returns</dt>
<dd>

A list of commands that passed the filter.

</dd><dt>Return type</dt>
<dd>

List\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>get_max_size(*commands*, */*)<a href="#discord.ext.commands.HelpCommand.get_max_size" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the largest name length of the specified command list.

Changed in version 2.0: <code>commands</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**commands** (Sequence\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]) – A sequence of commands to check for the largest size.

</dd><dt>Returns</dt>
<dd>

The maximum width of the commands.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>get_destination()<a href="#discord.ext.commands.HelpCommand.get_destination" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable" title="discord.abc.Messageable"><code>Messageable</code></a> where the help command will be output.

You can override this method to customise the behaviour.

By default this returns the context’s channel.

<dl><dt>Returns</dt>
<dd>

The destination where the help command will be output.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable" title="discord.abc.Messageable"><code>abc.Messageable</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* send_error_message(*error*, */*)<a href="#discord.ext.commands.HelpCommand.send_error_message" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Handles the implementation when an error happens in the help command. For example, the result of <a href="#discord.ext.commands.HelpCommand.command_not_found" title="discord.ext.commands.HelpCommand.command_not_found"><code>command_not_found()</code></a> will be passed here.

You can override this method to customise the behaviour.

By default, this sends the error message to the destination specified by <a href="#discord.ext.commands.HelpCommand.get_destination" title="discord.ext.commands.HelpCommand.get_destination"><code>get_destination()</code></a>.

Note

You can access the invocation context with <a href="#discord.ext.commands.HelpCommand.context" title="discord.ext.commands.HelpCommand.context"><code>HelpCommand.context</code></a>.

Changed in version 2.0: <code>error</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**error** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The error message to display to the user. Note that this has had mentions removed to prevent abuse.

</dd></dl></dd>
</dl><dl><dt>*await* on_help_command_error(*ctx*, *error*, */*)<a href="#discord.ext.commands.HelpCommand.on_help_command_error" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The help command’s error handler, as specified by <a href="https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#ext-commands-error-handler">Error Handling</a>.

Useful to override if you need some specific behaviour when the error handler is called.

By default this method does nothing and just propagates to the default error handlers.

Changed in version 2.0: <code>ctx</code> and <code>error</code> parameters are now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context.
- **error** (<a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>) – The error that was raised.

</dd></dl></dd>
</dl><dl><dt>*await* send_bot_help(*mapping*, */*)<a href="#discord.ext.commands.HelpCommand.send_bot_help" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Handles the implementation of the bot command page in the help command. This function is called when the help command is called with no arguments.

It should be noted that this method does not return anything – rather the actual message sending should be done inside this method. Well behaved subclasses should use <a href="#discord.ext.commands.HelpCommand.get_destination" title="discord.ext.commands.HelpCommand.get_destination"><code>get_destination()</code></a> to know where to send, as this is a customisation point for other users.

You can override this method to customise the behaviour.

Note

You can access the invocation context with <a href="#discord.ext.commands.HelpCommand.context" title="discord.ext.commands.HelpCommand.context"><code>HelpCommand.context</code></a>.

Also, the commands in the mapping are not filtered. To do the filtering you will have to call <a href="#discord.ext.commands.HelpCommand.filter_commands" title="discord.ext.commands.HelpCommand.filter_commands"><code>filter_commands()</code></a> yourself.

Changed in version 2.0: <code>mapping</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**mapping** (Mapping\[Optional\[<a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>], List\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]]) – A mapping of cogs to commands that have been requested by the user for help. The key of the mapping is the <a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a> that the command belongs to, or <code>None</code> if there isn’t one, and the value is a list of commands that belongs to that cog.

</dd></dl></dd>
</dl><dl><dt>*await* send_cog_help(*cog*, */*)<a href="#discord.ext.commands.HelpCommand.send_cog_help" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Handles the implementation of the cog page in the help command. This function is called when the help command is called with a cog as the argument.

It should be noted that this method does not return anything – rather the actual message sending should be done inside this method. Well behaved subclasses should use <a href="#discord.ext.commands.HelpCommand.get_destination" title="discord.ext.commands.HelpCommand.get_destination"><code>get_destination()</code></a> to know where to send, as this is a customisation point for other users.

You can override this method to customise the behaviour.

Note

You can access the invocation context with <a href="#discord.ext.commands.HelpCommand.context" title="discord.ext.commands.HelpCommand.context"><code>HelpCommand.context</code></a>.

To get the commands that belong to this cog see <a href="#discord.ext.commands.Cog.get_commands" title="discord.ext.commands.Cog.get_commands"><code>Cog.get_commands()</code></a>. The commands returned not filtered. To do the filtering you will have to call <a href="#discord.ext.commands.HelpCommand.filter_commands" title="discord.ext.commands.HelpCommand.filter_commands"><code>filter_commands()</code></a> yourself.

Changed in version 2.0: <code>cog</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**cog** (<a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>) – The cog that was requested for help.

</dd></dl></dd>
</dl><dl><dt>*await* send_group_help(*group*, */*)<a href="#discord.ext.commands.HelpCommand.send_group_help" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Handles the implementation of the group page in the help command. This function is called when the help command is called with a group as the argument.

It should be noted that this method does not return anything – rather the actual message sending should be done inside this method. Well behaved subclasses should use <a href="#discord.ext.commands.HelpCommand.get_destination" title="discord.ext.commands.HelpCommand.get_destination"><code>get_destination()</code></a> to know where to send, as this is a customisation point for other users.

You can override this method to customise the behaviour.

Note

You can access the invocation context with <a href="#discord.ext.commands.HelpCommand.context" title="discord.ext.commands.HelpCommand.context"><code>HelpCommand.context</code></a>.

To get the commands that belong to this group without aliases see <a href="#discord.ext.commands.Group.commands" title="discord.ext.commands.Group.commands"><code>Group.commands</code></a>. The commands returned not filtered. To do the filtering you will have to call <a href="#discord.ext.commands.HelpCommand.filter_commands" title="discord.ext.commands.HelpCommand.filter_commands"><code>filter_commands()</code></a> yourself.

Changed in version 2.0: <code>group</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**group** (<a href="#discord.ext.commands.Group" title="discord.ext.commands.Group"><code>Group</code></a>) – The group that was requested for help.

</dd></dl></dd>
</dl><dl><dt>*await* send_command_help(*command*, */*)<a href="#discord.ext.commands.HelpCommand.send_command_help" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Handles the implementation of the single command page in the help command.

It should be noted that this method does not return anything – rather the actual message sending should be done inside this method. Well behaved subclasses should use <a href="#discord.ext.commands.HelpCommand.get_destination" title="discord.ext.commands.HelpCommand.get_destination"><code>get_destination()</code></a> to know where to send, as this is a customisation point for other users.

You can override this method to customise the behaviour.

Note

You can access the invocation context with <a href="#discord.ext.commands.HelpCommand.context" title="discord.ext.commands.HelpCommand.context"><code>HelpCommand.context</code></a>.

Showing Help

There are certain attributes and methods that are helpful for a help command to show such as the following:

- <a href="#discord.ext.commands.Command.help" title="discord.ext.commands.Command.help"><code>Command.help</code></a>
- <a href="#discord.ext.commands.Command.brief" title="discord.ext.commands.Command.brief"><code>Command.brief</code></a>
- <a href="#discord.ext.commands.Command.short_doc" title="discord.ext.commands.Command.short_doc"><code>Command.short_doc</code></a>
- <a href="#discord.ext.commands.Command.description" title="discord.ext.commands.Command.description"><code>Command.description</code></a>
- <a href="#discord.ext.commands.HelpCommand.get_command_signature" title="discord.ext.commands.HelpCommand.get_command_signature"><code>get_command_signature()</code></a>

There are more than just these attributes but feel free to play around with these to help you get started to get the output that you want.

Changed in version 2.0: <code>command</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command that was requested for help.

</dd></dl></dd>
</dl><dl><dt>*await* prepare_help_command(*ctx*, *command=None*, */*)<a href="#discord.ext.commands.HelpCommand.prepare_help_command" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A low level method that can be used to prepare the help command before it does anything. For example, if you need to prepare some state in your subclass before the command does its processing then this would be the place to do it.

The default implementation does nothing.

Note

This is called *inside* the help command callback body. So all the usual rules that happen inside apply here as well.

Changed in version 2.0: <code>ctx</code> and <code>command</code> parameters are now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context.
- **command** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The argument passed to the help command.

</dd></dl></dd>
</dl><dl><dt>*await* command_callback(*ctx*, */*, ***, *command=None*)<a href="#discord.ext.commands.HelpCommand.command_callback" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The actual implementation of the help command.

It is not recommended to override this method and instead change the behaviour through the methods that actually get dispatched.

- <a href="#discord.ext.commands.HelpCommand.send_bot_help" title="discord.ext.commands.HelpCommand.send_bot_help"><code>send_bot_help()</code></a>
- <a href="#discord.ext.commands.HelpCommand.send_cog_help" title="discord.ext.commands.HelpCommand.send_cog_help"><code>send_cog_help()</code></a>
- <a href="#discord.ext.commands.HelpCommand.send_group_help" title="discord.ext.commands.HelpCommand.send_group_help"><code>send_group_help()</code></a>
- <a href="#discord.ext.commands.HelpCommand.send_command_help" title="discord.ext.commands.HelpCommand.send_command_help"><code>send_command_help()</code></a>
- <a href="#discord.ext.commands.HelpCommand.get_destination" title="discord.ext.commands.HelpCommand.get_destination"><code>get_destination()</code></a>
- <a href="#discord.ext.commands.HelpCommand.command_not_found" title="discord.ext.commands.HelpCommand.command_not_found"><code>command_not_found()</code></a>
- <a href="#discord.ext.commands.HelpCommand.subcommand_not_found" title="discord.ext.commands.HelpCommand.subcommand_not_found"><code>subcommand_not_found()</code></a>
- <a href="#discord.ext.commands.HelpCommand.send_error_message" title="discord.ext.commands.HelpCommand.send_error_message"><code>send_error_message()</code></a>
- <a href="#discord.ext.commands.HelpCommand.on_help_command_error" title="discord.ext.commands.HelpCommand.on_help_command_error"><code>on_help_command_error()</code></a>
- <a href="#discord.ext.commands.HelpCommand.prepare_help_command" title="discord.ext.commands.HelpCommand.prepare_help_command"><code>prepare_help_command()</code></a>

Changed in version 2.0: <code>ctx</code> parameter is now positional-only.

</dd></dl></dd>
</dl>

### DefaultHelpCommand ¶

Attributes

- [arguments\_heading](#discord.ext.commands.DefaultHelpCommand.arguments_heading)
- [commands\_heading](#discord.ext.commands.DefaultHelpCommand.commands_heading)
- [default\_argument\_description](#discord.ext.commands.DefaultHelpCommand.default_argument_description)
- [dm\_help](#discord.ext.commands.DefaultHelpCommand.dm_help)
- [dm\_help\_threshold](#discord.ext.commands.DefaultHelpCommand.dm_help_threshold)
- [indent](#discord.ext.commands.DefaultHelpCommand.indent)
- [no\_category](#discord.ext.commands.DefaultHelpCommand.no_category)
- [paginator](#discord.ext.commands.DefaultHelpCommand.paginator)
- [show\_parameter\_descriptions](#discord.ext.commands.DefaultHelpCommand.show_parameter_descriptions)
- [sort\_commands](#discord.ext.commands.DefaultHelpCommand.sort_commands)
- [width](#discord.ext.commands.DefaultHelpCommand.width)

Methods

- def [add\_command\_arguments](#discord.ext.commands.DefaultHelpCommand.add_command_arguments)
- def [add\_command\_formatting](#discord.ext.commands.DefaultHelpCommand.add_command_formatting)
- def [add\_indented\_commands](#discord.ext.commands.DefaultHelpCommand.add_indented_commands)
- def [get\_command\_signature](#discord.ext.commands.DefaultHelpCommand.get_command_signature)
- def [get\_destination](#discord.ext.commands.DefaultHelpCommand.get_destination)
- def [get\_ending\_note](#discord.ext.commands.DefaultHelpCommand.get_ending_note)
- async [send\_pages](#discord.ext.commands.DefaultHelpCommand.send_pages)
- def [shorten\_text](#discord.ext.commands.DefaultHelpCommand.shorten_text)

<dl><dt>*class*discord.ext.commands.DefaultHelpCommand(**args*, ***kwargs*)<a href="#discord.ext.commands.DefaultHelpCommand" title="Permalink to this definition">¶</a></dt>
<dd>

The implementation of the default help command.

This inherits from <a href="#discord.ext.commands.HelpCommand" title="discord.ext.commands.HelpCommand"><code>HelpCommand</code></a>.

It extends it with the following attributes.

<dl><dt>width<a href="#discord.ext.commands.DefaultHelpCommand.width" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of characters that fit in a line. Defaults to 80.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>sort_commands<a href="#discord.ext.commands.DefaultHelpCommand.sort_commands" title="Permalink to this definition">¶</a></dt>
<dd>

Whether to sort the commands in the output alphabetically. Defaults to <code>True</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>dm_help<a href="#discord.ext.commands.DefaultHelpCommand.dm_help" title="Permalink to this definition">¶</a></dt>
<dd>

A tribool that indicates if the help command should DM the user instead of sending it to the channel it received it from. If the boolean is set to <code>True</code>, then all help output is DM’d. If <code>False</code>, none of the help output is DM’d. If <code>None</code>, then the bot will only DM when the help message becomes too long (dictated by more than <a href="#discord.ext.commands.DefaultHelpCommand.dm_help_threshold" title="discord.ext.commands.DefaultHelpCommand.dm_help_threshold"><code>dm_help_threshold</code></a> characters). Defaults to <code>False</code>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]

</dd></dl></dd>
</dl><dl><dt>dm_help_threshold<a href="#discord.ext.commands.DefaultHelpCommand.dm_help_threshold" title="Permalink to this definition">¶</a></dt>
<dd>

The number of characters the paginator must accumulate before getting DM’d to the user if <a href="#discord.ext.commands.DefaultHelpCommand.dm_help" title="discord.ext.commands.DefaultHelpCommand.dm_help"><code>dm_help</code></a> is set to <code>None</code>. Defaults to 1000.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>indent<a href="#discord.ext.commands.DefaultHelpCommand.indent" title="Permalink to this definition">¶</a></dt>
<dd>

How much to indent the commands from a heading. Defaults to <code>2</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>arguments_heading<a href="#discord.ext.commands.DefaultHelpCommand.arguments_heading" title="Permalink to this definition">¶</a></dt>
<dd>

The arguments list’s heading string used when the help command is invoked with a command name. Useful for i18n. Defaults to <code>"Arguments:"</code>. Shown when <a href="#discord.ext.commands.DefaultHelpCommand.show_parameter_descriptions" title="discord.ext.commands.DefaultHelpCommand.show_parameter_descriptions"><code>show_parameter_descriptions</code></a> is <code>True</code>.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>show_parameter_descriptions<a href="#discord.ext.commands.DefaultHelpCommand.show_parameter_descriptions" title="Permalink to this definition">¶</a></dt>
<dd>

Whether to show the parameter descriptions. Defaults to <code>True</code>. Setting this to <code>False</code> will revert to showing the <a href="#discord.ext.commands.Command.signature" title="discord.ext.commands.Command.signature"><code>signature</code></a> instead.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>commands_heading<a href="#discord.ext.commands.DefaultHelpCommand.commands_heading" title="Permalink to this definition">¶</a></dt>
<dd>

The command list’s heading string used when the help command is invoked with a category name. Useful for i18n. Defaults to <code>"Commands:"</code>

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>default_argument_description<a href="#discord.ext.commands.DefaultHelpCommand.default_argument_description" title="Permalink to this definition">¶</a></dt>
<dd>

The default argument description string used when the argument’s <a href="#discord.ext.commands.Parameter.description" title="discord.ext.commands.Parameter.description"><code>description</code></a> is <code>None</code>. Useful for i18n. Defaults to <code>"No description given."</code>

New in version 2.0.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>no_category<a href="#discord.ext.commands.DefaultHelpCommand.no_category" title="Permalink to this definition">¶</a></dt>
<dd>

The string used when there is a command which does not belong to any category(cog). Useful for i18n. Defaults to <code>"No Category"</code>

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>paginator<a href="#discord.ext.commands.DefaultHelpCommand.paginator" title="Permalink to this definition">¶</a></dt>
<dd>

The paginator used to paginate the help command output.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.Paginator" title="discord.ext.commands.Paginator"><code>Paginator</code></a>

</dd></dl></dd>
</dl><dl><dt>shorten_text(*text*, */*)<a href="#discord.ext.commands.DefaultHelpCommand.shorten_text" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>: Shortens text to fit into the <a href="#discord.ext.commands.DefaultHelpCommand.width" title="discord.ext.commands.DefaultHelpCommand.width"><code>width</code></a>.

Changed in version 2.0: <code>text</code> parameter is now positional-only.

</dd></dl><dl><dt>get_ending_note()<a href="#discord.ext.commands.DefaultHelpCommand.get_ending_note" title="Permalink to this definition">¶</a></dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>: Returns help command’s ending note. This is mainly useful to override for i18n purposes.

</dd></dl><dl><dt>get_command_signature(*command*, */*)<a href="#discord.ext.commands.DefaultHelpCommand.get_command_signature" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the signature portion of the help page.

Calls <a href="#discord.ext.commands.HelpCommand.get_command_signature" title="discord.ext.commands.HelpCommand.get_command_signature"><code>get_command_signature()</code></a> if <a href="#discord.ext.commands.DefaultHelpCommand.show_parameter_descriptions" title="discord.ext.commands.DefaultHelpCommand.show_parameter_descriptions"><code>show_parameter_descriptions</code></a> is <code>False</code> else returns a modified signature where the command parameters are not shown.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command to get the signature of.

</dd><dt>Returns</dt>
<dd>

The signature for the command.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>add_indented_commands(*commands*, */*, ***, *heading*, *max_size=None*)<a href="#discord.ext.commands.DefaultHelpCommand.add_indented_commands" title="Permalink to this definition">¶</a></dt>
<dd>

Indents a list of commands after the specified heading.

The formatting is added to the <a href="#discord.ext.commands.DefaultHelpCommand.paginator" title="discord.ext.commands.DefaultHelpCommand.paginator"><code>paginator</code></a>.

The default implementation is the command name indented by <a href="#discord.ext.commands.DefaultHelpCommand.indent" title="discord.ext.commands.DefaultHelpCommand.indent"><code>indent</code></a> spaces, padded to <code>max_size</code> followed by the command’s <a href="#discord.ext.commands.Command.short_doc" title="discord.ext.commands.Command.short_doc"><code>Command.short_doc</code></a> and then shortened to fit into the <a href="#discord.ext.commands.DefaultHelpCommand.width" title="discord.ext.commands.DefaultHelpCommand.width"><code>width</code></a>.

Changed in version 2.0: <code>commands</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **commands** (Sequence\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]) – A list of commands to indent for output.
- **heading** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The heading to add to the output. This is only added if the list of commands is greater than 0.
- **max\_size** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The max size to use for the gap between indents. If unspecified, calls <a href="#discord.ext.commands.HelpCommand.get_max_size" title="discord.ext.commands.HelpCommand.get_max_size"><code>get_max_size()</code></a> on the commands parameter.

</dd></dl></dd>
</dl><dl><dt>add_command_arguments(*command*, */*)<a href="#discord.ext.commands.DefaultHelpCommand.add_command_arguments" title="Permalink to this definition">¶</a></dt>
<dd>

Indents a list of command arguments after the <a href="#discord.ext.commands.DefaultHelpCommand.arguments_heading" title="discord.ext.commands.DefaultHelpCommand.arguments_heading"><code>arguments_heading</code></a>.

The default implementation is the argument <a href="#discord.ext.commands.Parameter.name" title="discord.ext.commands.Parameter.name"><code>name</code></a> indented by <a href="#discord.ext.commands.DefaultHelpCommand.indent" title="discord.ext.commands.DefaultHelpCommand.indent"><code>indent</code></a> spaces, padded to <code>max_size</code> using <a href="#discord.ext.commands.HelpCommand.get_max_size" title="discord.ext.commands.HelpCommand.get_max_size"><code>get_max_size()</code></a> followed by the argument’s <a href="#discord.ext.commands.Parameter.description" title="discord.ext.commands.Parameter.description"><code>description</code></a> or <a href="#discord.ext.commands.DefaultHelpCommand.default_argument_description" title="discord.ext.commands.DefaultHelpCommand.default_argument_description"><code>default_argument_description</code></a> and then shortened to fit into the <a href="#discord.ext.commands.DefaultHelpCommand.width" title="discord.ext.commands.DefaultHelpCommand.width"><code>width</code></a> and then <a href="#discord.ext.commands.Parameter.displayed_default" title="discord.ext.commands.Parameter.displayed_default"><code>displayed_default</code></a> between () if one is present after that.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command to list the arguments for.

</dd></dl></dd>
</dl><dl><dt>*await* send_pages()<a href="#discord.ext.commands.DefaultHelpCommand.send_pages" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A helper utility to send the page output from <a href="#discord.ext.commands.DefaultHelpCommand.paginator" title="discord.ext.commands.DefaultHelpCommand.paginator"><code>paginator</code></a> to the destination.

</dd></dl><dl><dt>add_command_formatting(*command*, */*)<a href="#discord.ext.commands.DefaultHelpCommand.add_command_formatting" title="Permalink to this definition">¶</a></dt>
<dd>

A utility function to format the non-indented block of commands and groups.

Changed in version 2.0: <code>command</code> parameter is now positional-only.

Changed in version 2.0: <a href="#discord.ext.commands.DefaultHelpCommand.add_command_arguments" title="discord.ext.commands.DefaultHelpCommand.add_command_arguments"><code>add_command_arguments()</code></a> is now called if <a href="#discord.ext.commands.DefaultHelpCommand.show_parameter_descriptions" title="discord.ext.commands.DefaultHelpCommand.show_parameter_descriptions"><code>show_parameter_descriptions</code></a> is <code>True</code>.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command to format.

</dd></dl></dd>
</dl><dl><dt>get_destination()<a href="#discord.ext.commands.DefaultHelpCommand.get_destination" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable" title="discord.abc.Messageable"><code>Messageable</code></a> where the help command will be output.

You can override this method to customise the behaviour.

By default this returns the context’s channel.

<dl><dt>Returns</dt>
<dd>

The destination where the help command will be output.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable" title="discord.abc.Messageable"><code>abc.Messageable</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### MinimalHelpCommand ¶

Attributes

- [aliases\_heading](#discord.ext.commands.MinimalHelpCommand.aliases_heading)
- [commands\_heading](#discord.ext.commands.MinimalHelpCommand.commands_heading)
- [dm\_help](#discord.ext.commands.MinimalHelpCommand.dm_help)
- [dm\_help\_threshold](#discord.ext.commands.MinimalHelpCommand.dm_help_threshold)
- [no\_category](#discord.ext.commands.MinimalHelpCommand.no_category)
- [paginator](#discord.ext.commands.MinimalHelpCommand.paginator)
- [sort\_commands](#discord.ext.commands.MinimalHelpCommand.sort_commands)

Methods

- def [add\_aliases\_formatting](#discord.ext.commands.MinimalHelpCommand.add_aliases_formatting)
- def [add\_bot\_commands\_formatting](#discord.ext.commands.MinimalHelpCommand.add_bot_commands_formatting)
- def [add\_command\_formatting](#discord.ext.commands.MinimalHelpCommand.add_command_formatting)
- def [add\_subcommand\_formatting](#discord.ext.commands.MinimalHelpCommand.add_subcommand_formatting)
- def [get\_command\_signature](#discord.ext.commands.MinimalHelpCommand.get_command_signature)
- def [get\_destination](#discord.ext.commands.MinimalHelpCommand.get_destination)
- def [get\_ending\_note](#discord.ext.commands.MinimalHelpCommand.get_ending_note)
- def [get\_opening\_note](#discord.ext.commands.MinimalHelpCommand.get_opening_note)
- async [send\_pages](#discord.ext.commands.MinimalHelpCommand.send_pages)

<dl><dt>*class*discord.ext.commands.MinimalHelpCommand(**args*, ***kwargs*)<a href="#discord.ext.commands.MinimalHelpCommand" title="Permalink to this definition">¶</a></dt>
<dd>

An implementation of a help command with minimal output.

This inherits from <a href="#discord.ext.commands.HelpCommand" title="discord.ext.commands.HelpCommand"><code>HelpCommand</code></a>.

<dl><dt>sort_commands<a href="#discord.ext.commands.MinimalHelpCommand.sort_commands" title="Permalink to this definition">¶</a></dt>
<dd>

Whether to sort the commands in the output alphabetically. Defaults to <code>True</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>commands_heading<a href="#discord.ext.commands.MinimalHelpCommand.commands_heading" title="Permalink to this definition">¶</a></dt>
<dd>

The command list’s heading string used when the help command is invoked with a category name. Useful for i18n. Defaults to <code>"Commands"</code>

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>aliases_heading<a href="#discord.ext.commands.MinimalHelpCommand.aliases_heading" title="Permalink to this definition">¶</a></dt>
<dd>

The alias list’s heading string used to list the aliases of the command. Useful for i18n. Defaults to <code>"Aliases:"</code>.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>dm_help<a href="#discord.ext.commands.MinimalHelpCommand.dm_help" title="Permalink to this definition">¶</a></dt>
<dd>

A tribool that indicates if the help command should DM the user instead of sending it to the channel it received it from. If the boolean is set to <code>True</code>, then all help output is DM’d. If <code>False</code>, none of the help output is DM’d. If <code>None</code>, then the bot will only DM when the help message becomes too long (dictated by more than <a href="#discord.ext.commands.MinimalHelpCommand.dm_help_threshold" title="discord.ext.commands.MinimalHelpCommand.dm_help_threshold"><code>dm_help_threshold</code></a> characters). Defaults to <code>False</code>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]

</dd></dl></dd>
</dl><dl><dt>dm_help_threshold<a href="#discord.ext.commands.MinimalHelpCommand.dm_help_threshold" title="Permalink to this definition">¶</a></dt>
<dd>

The number of characters the paginator must accumulate before getting DM’d to the user if <a href="#discord.ext.commands.MinimalHelpCommand.dm_help" title="discord.ext.commands.MinimalHelpCommand.dm_help"><code>dm_help</code></a> is set to <code>None</code>. Defaults to 1000.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl><dl><dt>no_category<a href="#discord.ext.commands.MinimalHelpCommand.no_category" title="Permalink to this definition">¶</a></dt>
<dd>

The string used when there is a command which does not belong to any category(cog). Useful for i18n. Defaults to <code>"No Category"</code>

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>paginator<a href="#discord.ext.commands.MinimalHelpCommand.paginator" title="Permalink to this definition">¶</a></dt>
<dd>

The paginator used to paginate the help command output.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.Paginator" title="discord.ext.commands.Paginator"><code>Paginator</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* send_pages()<a href="#discord.ext.commands.MinimalHelpCommand.send_pages" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A helper utility to send the page output from <a href="#discord.ext.commands.MinimalHelpCommand.paginator" title="discord.ext.commands.MinimalHelpCommand.paginator"><code>paginator</code></a> to the destination.

</dd></dl><dl><dt>get_opening_note()<a href="#discord.ext.commands.MinimalHelpCommand.get_opening_note" title="Permalink to this definition">¶</a></dt>
<dd>

Returns help command’s opening note. This is mainly useful to override for i18n purposes.

The default implementation returns

```
Use `{prefix}{command_name} [command]` for more info on a command.
You can also use `{prefix}{command_name} [category]` for more info on a category.

```

<dl><dt>Returns</dt>
<dd>

The help command opening note.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>get_command_signature(*command*, */*)<a href="#discord.ext.commands.MinimalHelpCommand.get_command_signature" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves the signature portion of the help page.

Changed in version 2.0: <code>command</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command to get the signature of.

</dd><dt>Returns</dt>
<dd>

The signature for the command.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>get_ending_note()<a href="#discord.ext.commands.MinimalHelpCommand.get_ending_note" title="Permalink to this definition">¶</a></dt>
<dd>

Return the help command’s ending note. This is mainly useful to override for i18n purposes.

The default implementation does nothing.

<dl><dt>Returns</dt>
<dd>

The help command ending note.

</dd><dt>Return type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>add_bot_commands_formatting(*commands*, *heading*, */*)<a href="#discord.ext.commands.MinimalHelpCommand.add_bot_commands_formatting" title="Permalink to this definition">¶</a></dt>
<dd>

Adds the minified bot heading with commands to the output.

The formatting should be added to the <a href="#discord.ext.commands.MinimalHelpCommand.paginator" title="discord.ext.commands.MinimalHelpCommand.paginator"><code>paginator</code></a>.

The default implementation is a bold underline heading followed by commands separated by an EN SPACE (U+2002) in the next line.

Changed in version 2.0: <code>commands</code> and <code>heading</code> parameters are now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **commands** (Sequence\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]) – A list of commands that belong to the heading.
- **heading** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The heading to add to the line.

</dd></dl></dd>
</dl><dl><dt>add_subcommand_formatting(*command*, */*)<a href="#discord.ext.commands.MinimalHelpCommand.add_subcommand_formatting" title="Permalink to this definition">¶</a></dt>
<dd>

Adds formatting information on a subcommand.

The formatting should be added to the <a href="#discord.ext.commands.MinimalHelpCommand.paginator" title="discord.ext.commands.MinimalHelpCommand.paginator"><code>paginator</code></a>.

The default implementation is the prefix and the <a href="#discord.ext.commands.Command.qualified_name" title="discord.ext.commands.Command.qualified_name"><code>Command.qualified_name</code></a> optionally followed by an En dash and the command’s <a href="#discord.ext.commands.Command.short_doc" title="discord.ext.commands.Command.short_doc"><code>Command.short_doc</code></a>.

Changed in version 2.0: <code>command</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command to show information of.

</dd></dl></dd>
</dl><dl><dt>add_aliases_formatting(*aliases*, */*)<a href="#discord.ext.commands.MinimalHelpCommand.add_aliases_formatting" title="Permalink to this definition">¶</a></dt>
<dd>

Adds the formatting information on a command’s aliases.

The formatting should be added to the <a href="#discord.ext.commands.MinimalHelpCommand.paginator" title="discord.ext.commands.MinimalHelpCommand.paginator"><code>paginator</code></a>.

The default implementation is the <a href="#discord.ext.commands.MinimalHelpCommand.aliases_heading" title="discord.ext.commands.MinimalHelpCommand.aliases_heading"><code>aliases_heading</code></a> bolded followed by a comma separated list of aliases.

This is not called if there are no aliases to format.

Changed in version 2.0: <code>aliases</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**aliases** (Sequence\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – A list of aliases to format.

</dd></dl></dd>
</dl><dl><dt>add_command_formatting(*command*, */*)<a href="#discord.ext.commands.MinimalHelpCommand.add_command_formatting" title="Permalink to this definition">¶</a></dt>
<dd>

A utility function to format commands and groups.

Changed in version 2.0: <code>command</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command to format.

</dd></dl></dd>
</dl><dl><dt>get_destination()<a href="#discord.ext.commands.MinimalHelpCommand.get_destination" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable" title="discord.abc.Messageable"><code>Messageable</code></a> where the help command will be output.

You can override this method to customise the behaviour.

By default this returns the context’s channel.

<dl><dt>Returns</dt>
<dd>

The destination where the help command will be output.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable" title="discord.abc.Messageable"><code>abc.Messageable</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### Paginator ¶

Attributes

- [linesep](#discord.ext.commands.Paginator.linesep)
- [max\_size](#discord.ext.commands.Paginator.max_size)
- [pages](#discord.ext.commands.Paginator.pages)
- [prefix](#discord.ext.commands.Paginator.prefix)
- [suffix](#discord.ext.commands.Paginator.suffix)

Methods

- def [add\_line](#discord.ext.commands.Paginator.add_line)
- def [clear](#discord.ext.commands.Paginator.clear)
- def [close\_page](#discord.ext.commands.Paginator.close_page)

<dl><dt>*class*discord.ext.commands.Paginator(*prefix='```'*, *suffix='```'*, *max_size=2000*, *linesep='\n'*)<a href="#discord.ext.commands.Paginator" title="Permalink to this definition">¶</a></dt>
<dd>

A class that aids in paginating code blocks for Discord messages.

<dl><dt>len(x)</dt>
<dd>

Returns the total number of characters in the paginator.

</dd></dl>

<dl><dt>prefix<a href="#discord.ext.commands.Paginator.prefix" title="Permalink to this definition">¶</a></dt>
<dd>

The prefix inserted to every page. e.g. three backticks, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>suffix<a href="#discord.ext.commands.Paginator.suffix" title="Permalink to this definition">¶</a></dt>
<dd>

The suffix appended at the end of every page. e.g. three backticks, if any.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>max_size<a href="#discord.ext.commands.Paginator.max_size" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum amount of codepoints allowed in a page.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>linesep<a href="#discord.ext.commands.Paginator.linesep" title="Permalink to this definition">¶</a></dt>
<dd><dl><dt>The character string inserted between lines. e.g. a newline character.</dt>
<dd>

New in version 1.7.

</dd></dl><dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>clear()<a href="#discord.ext.commands.Paginator.clear" title="Permalink to this definition">¶</a></dt>
<dd>

Clears the paginator to have no pages.

</dd></dl><dl><dt>add_line(*line=''*, ***, *empty=False*)<a href="#discord.ext.commands.Paginator.add_line" title="Permalink to this definition">¶</a></dt>
<dd>

Adds a line to the current page.

If the line exceeds the <a href="#discord.ext.commands.Paginator.max_size" title="discord.ext.commands.Paginator.max_size"><code>max_size</code></a> then an exception is raised.

<dl><dt>Parameters</dt>
<dd>

- **line** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The line to add.
- **empty** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Indicates if another empty line should be added.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#RuntimeError" title="(in Python v3.14)">**RuntimeError**</a> – The line was too big for the current <a href="#discord.ext.commands.Paginator.max_size" title="discord.ext.commands.Paginator.max_size"><code>max_size</code></a>.

</dd></dl></dd>
</dl><dl><dt>close_page()<a href="#discord.ext.commands.Paginator.close_page" title="Permalink to this definition">¶</a></dt>
<dd>

Prematurely terminate a page.

</dd></dl><dl><dt>*property*pages<a href="#discord.ext.commands.Paginator.pages" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the rendered list of pages.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl></dd>
</dl>

## Enums ¶

<dl><dt>*class*discord.ext.commands.BucketType<a href="#discord.ext.commands.BucketType" title="Permalink to this definition">¶</a></dt>
<dd>

Specifies a type of bucket for, e.g. a cooldown.

<dl><dt>default<a href="#discord.ext.commands.BucketType.default" title="Permalink to this definition">¶</a></dt>
<dd>

The default bucket operates on a global basis.

</dd></dl><dl><dt>user<a href="#discord.ext.commands.BucketType.user" title="Permalink to this definition">¶</a></dt>
<dd>

The user bucket operates on a per-user basis.

</dd></dl><dl><dt>guild<a href="#discord.ext.commands.BucketType.guild" title="Permalink to this definition">¶</a></dt>
<dd>

The guild bucket operates on a per-guild basis.

</dd></dl><dl><dt>channel<a href="#discord.ext.commands.BucketType.channel" title="Permalink to this definition">¶</a></dt>
<dd>

The channel bucket operates on a per-channel basis.

</dd></dl><dl><dt>member<a href="#discord.ext.commands.BucketType.member" title="Permalink to this definition">¶</a></dt>
<dd>

The member bucket operates on a per-member basis.

</dd></dl><dl><dt>category<a href="#discord.ext.commands.BucketType.category" title="Permalink to this definition">¶</a></dt>
<dd>

The category bucket operates on a per-category basis.

</dd></dl><dl><dt>role<a href="#discord.ext.commands.BucketType.role" title="Permalink to this definition">¶</a></dt>
<dd>

The role bucket operates on a per-role basis.

New in version 1.3.

</dd></dl></dd>
</dl>

## Checks ¶

<dl><dt>@discord.ext.commands.check(*predicate*)<a href="#discord.ext.commands.check" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that adds a check to the <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> or its subclasses. These checks could be accessed via <a href="#discord.ext.commands.Command.checks" title="discord.ext.commands.Command.checks"><code>Command.checks</code></a>.

These checks should be predicates that take in a single parameter taking a <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>. If the check returns a <code>False</code>-like value then during invocation a <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a> exception is raised and sent to the <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> event.

If an exception should be thrown in the predicate then it should be a subclass of <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>. Any exception not subclassed from it will be propagated while those subclassed will be sent to <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a>.

A special attribute named <code>predicate</code> is bound to the value returned by this decorator to retrieve the predicate passed to the decorator. This allows the following introspection and chaining to be done:

```
def owner_or_permissions(**perms):
    original = commands.has_permissions(**perms).predicate
    async def extended_check(ctx):
        if ctx.guild is None:
            return False
        return ctx.guild.owner_id == ctx.author.id or await original(ctx)
    return commands.check(extended_check)

```

Note

The function returned by <code>predicate</code> is **always** a coroutine, even if the original function was not a coroutine.

Changed in version 1.3: The <code>predicate</code> attribute was added.

Examples

Creating a basic check to see if the command invoker is you.

```
def check_if_it_is_me(ctx):
    return ctx.message.author.id == 85309593344815104

@bot.command()
@commands.check(check_if_it_is_me)
async def only_for_me(ctx):
    await ctx.send('I know you!')

```

Transforming common checks into its own decorator:

```
def is_me():
    def predicate(ctx):
        return ctx.message.author.id == 85309593344815104
    return commands.check(predicate)

@bot.command()
@is_me()
async def only_me(ctx):
    await ctx.send('Only you!')

```

Changed in version 2.0: <code>predicate</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**predicate** (Callable\[\[<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>], <a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]) – The predicate to check if the command should be invoked.

</dd></dl></dd>
</dl><dl><dt>@discord.ext.commands.check_any(**checks*)<a href="#discord.ext.commands.check_any" title="Permalink to this definition">¶</a></dt>
<dd>

A <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> that is added that checks if any of the checks passed will pass, i.e. using logical OR.

If all checks fail then <a href="#discord.ext.commands.CheckAnyFailure" title="discord.ext.commands.CheckAnyFailure"><code>CheckAnyFailure</code></a> is raised to signal the failure. It inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

Note

The <code>predicate</code> attribute for this function **is** a coroutine.

New in version 1.3.

<dl><dt>Parameters</dt>
<dd>

**\*checks** (Callable\[\[<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>], <a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]) – An argument list of checks that have been decorated with the <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> decorator.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – A check passed has not been decorated with the <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> decorator.

</dd></dl>

Examples

Creating a basic check to see if it’s the bot owner or the server owner:

```
def is_guild_owner():
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)

@bot.command()
@commands.check_any(commands.is_owner(), is_guild_owner())
async def only_for_owners(ctx):
    await ctx.send('Hello mister owner!')

```

</dd></dl><dl><dt>@discord.ext.commands.has_role(*item*)<a href="#discord.ext.commands.has_role" title="Permalink to this definition">¶</a></dt>
<dd>

A <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> that is added that checks if the member invoking the command has the role specified via the name or ID specified.

If a string is specified, you must give the exact name of the role, including caps and spelling.

If an integer is specified, you must give the exact snowflake ID of the role.

If the message is invoked in a private message context then the check will return <code>False</code>.

This check raises one of two special exceptions, <a href="#discord.ext.commands.MissingRole" title="discord.ext.commands.MissingRole"><code>MissingRole</code></a> if the user is missing a role, or <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> if it is used in a private message. Both inherit from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

Changed in version 1.1: Raise <a href="#discord.ext.commands.MissingRole" title="discord.ext.commands.MissingRole"><code>MissingRole</code></a> or <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> instead of generic <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

Changed in version 2.0: <code>item</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

**item** (Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The name or ID of the role to check.

</dd></dl></dd>
</dl><dl><dt>@discord.ext.commands.has_permissions(***perms*)<a href="#discord.ext.commands.has_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

A <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> that is added that checks if the member has all of the permissions necessary.

Note that this check operates on the current channel permissions, not the guild wide permissions.

The permissions passed in must be exactly like the properties shown under <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>discord.Permissions</code></a>.

This check raises a special exception, <a href="#discord.ext.commands.MissingPermissions" title="discord.ext.commands.MissingPermissions"><code>MissingPermissions</code></a> that is inherited from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

<dl><dt>Parameters</dt>
<dd>

**perms** – An argument list of permissions to check for.

</dd></dl>

Example

```
@bot.command()
@commands.has_permissions(manage_messages=True)
async def test(ctx):
    await ctx.send('You can manage messages.')

```

</dd></dl><dl><dt>@discord.ext.commands.has_guild_permissions(***perms*)<a href="#discord.ext.commands.has_guild_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

Similar to <a href="#discord.ext.commands.has_permissions" title="discord.ext.commands.has_permissions"><code>has_permissions()</code></a>, but operates on guild wide permissions instead of the current channel permissions.

If this check is called in a DM context, it will raise an exception, <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a>.

New in version 1.3.

</dd></dl><dl><dt>@discord.ext.commands.has_any_role(**items*)<a href="#discord.ext.commands.has_any_role" title="Permalink to this definition">¶</a></dt>
<dd>

A <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> that is added that checks if the member invoking the command has **any** of the roles specified. This means that if they have one out of the three roles specified, then this check will return <code>True</code>.

Similar to <a href="#discord.ext.commands.has_role" title="discord.ext.commands.has_role"><code>has_role()</code></a>, the names or IDs passed in must be exact.

This check raises one of two special exceptions, <a href="#discord.ext.commands.MissingAnyRole" title="discord.ext.commands.MissingAnyRole"><code>MissingAnyRole</code></a> if the user is missing all roles, or <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> if it is used in a private message. Both inherit from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

Changed in version 1.1: Raise <a href="#discord.ext.commands.MissingAnyRole" title="discord.ext.commands.MissingAnyRole"><code>MissingAnyRole</code></a> or <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> instead of generic <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

<dl><dt>Parameters</dt>
<dd>

**items** (List\[Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]]) – An argument list of names or IDs to check that the member has roles wise.

</dd></dl>

Example

```
@bot.command()
@commands.has_any_role('Library Devs', 'Moderators', 492212595072434186)
async def cool(ctx):
    await ctx.send('You are cool indeed')

```

</dd></dl><dl><dt>@discord.ext.commands.bot_has_role(*item*)<a href="#discord.ext.commands.bot_has_role" title="Permalink to this definition">¶</a></dt>
<dd>

Similar to <a href="#discord.ext.commands.has_role" title="discord.ext.commands.has_role"><code>has_role()</code></a> except checks if the bot itself has the role.

This check raises one of two special exceptions, <a href="#discord.ext.commands.BotMissingRole" title="discord.ext.commands.BotMissingRole"><code>BotMissingRole</code></a> if the bot is missing the role, or <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> if it is used in a private message. Both inherit from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

Changed in version 1.1: Raise <a href="#discord.ext.commands.BotMissingRole" title="discord.ext.commands.BotMissingRole"><code>BotMissingRole</code></a> or <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> instead of generic <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

Changed in version 2.0: <code>item</code> parameter is now positional-only.

</dd></dl><dl><dt>@discord.ext.commands.bot_has_permissions(***perms*)<a href="#discord.ext.commands.bot_has_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

Similar to <a href="#discord.ext.commands.has_permissions" title="discord.ext.commands.has_permissions"><code>has_permissions()</code></a> except checks if the bot itself has the permissions listed.

This check raises a special exception, <a href="#discord.ext.commands.BotMissingPermissions" title="discord.ext.commands.BotMissingPermissions"><code>BotMissingPermissions</code></a> that is inherited from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

</dd></dl><dl><dt>@discord.ext.commands.bot_has_guild_permissions(***perms*)<a href="#discord.ext.commands.bot_has_guild_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

Similar to <a href="#discord.ext.commands.has_guild_permissions" title="discord.ext.commands.has_guild_permissions"><code>has_guild_permissions()</code></a>, but checks the bot members guild permissions.

New in version 1.3.

</dd></dl><dl><dt>@discord.ext.commands.bot_has_any_role(**items*)<a href="#discord.ext.commands.bot_has_any_role" title="Permalink to this definition">¶</a></dt>
<dd>

Similar to <a href="#discord.ext.commands.has_any_role" title="discord.ext.commands.has_any_role"><code>has_any_role()</code></a> except checks if the bot itself has any of the roles listed.

This check raises one of two special exceptions, <a href="#discord.ext.commands.BotMissingAnyRole" title="discord.ext.commands.BotMissingAnyRole"><code>BotMissingAnyRole</code></a> if the bot is missing all roles, or <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> if it is used in a private message. Both inherit from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

Changed in version 1.1: Raise <a href="#discord.ext.commands.BotMissingAnyRole" title="discord.ext.commands.BotMissingAnyRole"><code>BotMissingAnyRole</code></a> or <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> instead of generic checkfailure

</dd></dl><dl><dt>@discord.ext.commands.cooldown(*rate*, *per*, *type=discord.ext.commands.BucketType.default*)<a href="#discord.ext.commands.cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that adds a cooldown to a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>

A cooldown allows a command to only be used a specific amount of times in a specific time frame. These cooldowns can be based either on a per-guild, per-channel, per-user, per-role or global basis. Denoted by the third argument of <code>type</code> which must be of enum type <a href="#discord.ext.commands.BucketType" title="discord.ext.commands.BucketType"><code>BucketType</code></a>.

If a cooldown is triggered, then <a href="#discord.ext.commands.CommandOnCooldown" title="discord.ext.commands.CommandOnCooldown"><code>CommandOnCooldown</code></a> is triggered in <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> and the local error handler.

A command can only have a single cooldown.

<dl><dt>Parameters</dt>
<dd>

- **rate** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The number of times a command can be used before triggering a cooldown.
- **per** (<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>) – The amount of seconds to wait for a cooldown when it’s been triggered.
- **type** (Union\[<a href="#discord.ext.commands.BucketType" title="discord.ext.commands.BucketType"><code>BucketType</code></a>, Callable\[\[<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>], Any]]) –

  The type of cooldown to have. If callable, should return a key for the mapping.

  Changed in version 1.7: Callables are now supported for custom bucket types.

  Changed in version 2.0: When passing a callable, it now needs to accept <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a> rather than <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a> as its only argument.

</dd></dl></dd>
</dl><dl><dt>@discord.ext.commands.dynamic_cooldown(*cooldown*, *type*)<a href="#discord.ext.commands.dynamic_cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that adds a dynamic cooldown to a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>

This differs from <a href="#discord.ext.commands.cooldown" title="discord.ext.commands.cooldown"><code>cooldown()</code></a> in that it takes a function that accepts a single parameter of type <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a> and must return a <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Cooldown" title="discord.app_commands.Cooldown"><code>Cooldown</code></a> or <code>None</code>. If <code>None</code> is returned then that cooldown is effectively bypassed.

A cooldown allows a command to only be used a specific amount of times in a specific time frame. These cooldowns can be based either on a per-guild, per-channel, per-user, per-role or global basis. Denoted by the third argument of <code>type</code> which must be of enum type <a href="#discord.ext.commands.BucketType" title="discord.ext.commands.BucketType"><code>BucketType</code></a>.

If a cooldown is triggered, then <a href="#discord.ext.commands.CommandOnCooldown" title="discord.ext.commands.CommandOnCooldown"><code>CommandOnCooldown</code></a> is triggered in <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> and the local error handler.

A command can only have a single cooldown.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **cooldown** (Callable\[\[<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>], Optional\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Cooldown" title="discord.app_commands.Cooldown"><code>Cooldown</code></a>]]) – A function that takes a message and returns a cooldown that will apply to this invocation or <code>None</code> if the cooldown should be bypassed.
- **type** (<a href="#discord.ext.commands.BucketType" title="discord.ext.commands.BucketType"><code>BucketType</code></a>) – The type of cooldown to have.

</dd></dl></dd>
</dl><dl><dt>@discord.ext.commands.max_concurrency(*number*, *per=discord.ext.commands.BucketType.default*, ***, *wait=False*)<a href="#discord.ext.commands.max_concurrency" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that adds a maximum concurrency to a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> or its subclasses.

This enables you to only allow a certain number of command invocations at the same time, for example if a command takes too long or if only one user can use it at a time. This differs from a cooldown in that there is no set waiting period or token bucket – only a set number of people can run the command.

New in version 1.3.

<dl><dt>Parameters</dt>
<dd>

- **number** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The maximum number of invocations of this command that can be running at the same time.
- **per** (<a href="#discord.ext.commands.BucketType" title="discord.ext.commands.BucketType"><code>BucketType</code></a>) – The bucket that this concurrency is based on, e.g. <code>BucketType.guild</code> would allow it to be used up to <code>number</code> times per guild.
- **wait** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether the command should wait for the queue to be over. If this is set to <code>False</code> then instead of waiting until the command can run again, the command raises <a href="#discord.ext.commands.MaxConcurrencyReached" title="discord.ext.commands.MaxConcurrencyReached"><code>MaxConcurrencyReached</code></a> to its error handler. If this is set to <code>True</code> then the command waits until it can be executed.

</dd></dl></dd>
</dl><dl><dt>@discord.ext.commands.before_invoke(*coro*)<a href="#discord.ext.commands.before_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a pre-invoke hook.

This allows you to refer to one before invoke hook for several commands that do not have to be within the same cog.

New in version 1.4.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

Example

```
async def record_usage(ctx):
    print(ctx.author, 'used', ctx.command, 'at', ctx.message.created_at)

@bot.command()
@commands.before_invoke(record_usage)
async def who(ctx): # Output: <User> used who at <Time>
    await ctx.send('i am a bot')

class What(commands.Cog):

    @commands.before_invoke(record_usage)
    @commands.command()
    async def when(self, ctx): # Output: <User> used when at <Time>
        await ctx.send(f'and i have existed since {ctx.bot.user.created_at}')

    @commands.command()
    async def where(self, ctx): # Output: <Nothing>
        await ctx.send('on Discord')

    @commands.command()
    async def why(self, ctx): # Output: <Nothing>
        await ctx.send('because someone made me')

```

</dd></dl><dl><dt>@discord.ext.commands.after_invoke(*coro*)<a href="#discord.ext.commands.after_invoke" title="Permalink to this definition">¶</a></dt>
<dd>

A decorator that registers a coroutine as a post-invoke hook.

This allows you to refer to one after invoke hook for several commands that do not have to be within the same cog.

New in version 1.4.

Changed in version 2.0: <code>coro</code> parameter is now positional-only.

</dd></dl><dl><dt>@discord.ext.commands.guild_only()<a href="#discord.ext.commands.guild_only" title="Permalink to this definition">¶</a></dt>
<dd>

A <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> that indicates this command must only be used in a guild context only. Basically, no private messages are allowed when using the command.

This check raises a special exception, <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> that is inherited from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

If used on hybrid commands, this will be equivalent to the <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.guild_only" title="discord.app_commands.guild_only"><code>discord.app_commands.guild_only()</code></a> decorator. In an unsupported context, such as a subcommand, this will still fallback to applying the check.

</dd></dl><dl><dt>@discord.ext.commands.dm_only()<a href="#discord.ext.commands.dm_only" title="Permalink to this definition">¶</a></dt>
<dd>

A <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> that indicates this command must only be used in a DM context. Only private messages are allowed when using the command.

This check raises a special exception, <a href="#discord.ext.commands.PrivateMessageOnly" title="discord.ext.commands.PrivateMessageOnly"><code>PrivateMessageOnly</code></a> that is inherited from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 1.1.

</dd></dl><dl><dt>@discord.ext.commands.is_owner()<a href="#discord.ext.commands.is_owner" title="Permalink to this definition">¶</a></dt>
<dd>

A <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> that checks if the person invoking this command is the owner of the bot.

This is powered by <a href="#discord.ext.commands.Bot.is_owner" title="discord.ext.commands.Bot.is_owner"><code>Bot.is_owner()</code></a>.

This check raises a special exception, <a href="#discord.ext.commands.NotOwner" title="discord.ext.commands.NotOwner"><code>NotOwner</code></a> that is derived from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

</dd></dl><dl><dt>@discord.ext.commands.is_nsfw()<a href="#discord.ext.commands.is_nsfw" title="Permalink to this definition">¶</a></dt>
<dd>

A <a href="#discord.ext.commands.check" title="discord.ext.commands.check"><code>check()</code></a> that checks if the channel is a NSFW channel.

This check raises a special exception, <a href="#discord.ext.commands.NSFWChannelRequired" title="discord.ext.commands.NSFWChannelRequired"><code>NSFWChannelRequired</code></a> that is derived from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

If used on hybrid commands, this will be equivalent to setting the application command’s <code>nsfw</code> attribute to <code>True</code>. In an unsupported context, such as a subcommand, this will still fallback to applying the check.

Changed in version 1.1: Raise <a href="#discord.ext.commands.NSFWChannelRequired" title="discord.ext.commands.NSFWChannelRequired"><code>NSFWChannelRequired</code></a> instead of generic <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>. DM channels will also now pass this check.

</dd></dl>

## Context ¶

Attributes

- [args](#discord.ext.commands.Context.args)
- [author](#discord.ext.commands.Context.author)
- [bot](#discord.ext.commands.Context.bot)
- [bot\_permissions](#discord.ext.commands.Context.bot_permissions)
- [channel](#discord.ext.commands.Context.channel)
- [clean\_prefix](#discord.ext.commands.Context.clean_prefix)
- [cog](#discord.ext.commands.Context.cog)
- [command](#discord.ext.commands.Context.command)
- [command\_failed](#discord.ext.commands.Context.command_failed)
- [current\_argument](#discord.ext.commands.Context.current_argument)
- [current\_parameter](#discord.ext.commands.Context.current_parameter)
- [filesize\_limit](#discord.ext.commands.Context.filesize_limit)
- [guild](#discord.ext.commands.Context.guild)
- [interaction](#discord.ext.commands.Context.interaction)
- [invoked\_parents](#discord.ext.commands.Context.invoked_parents)
- [invoked\_subcommand](#discord.ext.commands.Context.invoked_subcommand)
- [invoked\_with](#discord.ext.commands.Context.invoked_with)
- [kwargs](#discord.ext.commands.Context.kwargs)
- [me](#discord.ext.commands.Context.me)
- [message](#discord.ext.commands.Context.message)
- [permissions](#discord.ext.commands.Context.permissions)
- [prefix](#discord.ext.commands.Context.prefix)
- [subcommand\_passed](#discord.ext.commands.Context.subcommand_passed)
- [valid](#discord.ext.commands.Context.valid)
- [voice\_client](#discord.ext.commands.Context.voice_client)

Methods

- cls [Context.from\_interaction](#discord.ext.commands.Context.from_interaction)
- async [defer](#discord.ext.commands.Context.defer)
- async [fetch\_message](#discord.ext.commands.Context.fetch_message)
- async for [history](#discord.ext.commands.Context.history)
- async [invoke](#discord.ext.commands.Context.invoke)
- def [pins](#discord.ext.commands.Context.pins)
- async [reinvoke](#discord.ext.commands.Context.reinvoke)
- async [reply](#discord.ext.commands.Context.reply)
- async [send](#discord.ext.commands.Context.send)
- async [send\_help](#discord.ext.commands.Context.send_help)
- def [typing](#discord.ext.commands.Context.typing)

<dl><dt>*class*discord.ext.commands.Context(***, *message*, *bot*, *view*, *args=...*, *kwargs=...*, *prefix=None*, *command=None*, *invoked_with=None*, *invoked_parents=...*, *invoked_subcommand=None*, *subcommand_passed=None*, *command_failed=False*, *current_parameter=None*, *current_argument=None*, *interaction=None*)<a href="#discord.ext.commands.Context" title="Permalink to this definition">¶</a></dt>
<dd>

Represents the context in which a command is being invoked under.

This class contains a lot of meta data to help you understand more about the invocation context. This class is not created manually and is instead passed around to commands as the first parameter.

This class implements the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable" title="discord.abc.Messageable"><code>Messageable</code></a> ABC.

<dl><dt>message<a href="#discord.ext.commands.Context.message" title="Permalink to this definition">¶</a></dt>
<dd>

The message that triggered the command being executed.

Note

In the case of an interaction based context, this message is “synthetic” and does not actually exist. Therefore, the ID on it is invalid similar to ephemeral messages.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>

</dd></dl></dd>
</dl><dl><dt>bot<a href="#discord.ext.commands.Context.bot" title="Permalink to this definition">¶</a></dt>
<dd>

The bot that contains the command being executed.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.Bot" title="discord.ext.commands.Bot"><code>Bot</code></a>

</dd></dl></dd>
</dl><dl><dt>args<a href="#discord.ext.commands.Context.args" title="Permalink to this definition">¶</a></dt>
<dd>

The list of transformed arguments that were passed into the command. If this is accessed during the <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> event then this list could be incomplete.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#list" title="(in Python v3.14)"><code>list</code></a>

</dd></dl></dd>
</dl><dl><dt>kwargs<a href="#discord.ext.commands.Context.kwargs" title="Permalink to this definition">¶</a></dt>
<dd>

A dictionary of transformed arguments that were passed into the command. Similar to <a href="#discord.ext.commands.Context.args" title="discord.ext.commands.Context.args"><code>args</code></a>, if this is accessed in the <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a> event then this dict could be incomplete.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#dict" title="(in Python v3.14)"><code>dict</code></a>

</dd></dl></dd>
</dl><dl><dt>current_parameter<a href="#discord.ext.commands.Context.current_parameter" title="Permalink to this definition">¶</a></dt>
<dd>

The parameter that is currently being inspected and converted. This is only of use for within converters.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Parameter" title="discord.ext.commands.Parameter"><code>Parameter</code></a>]

</dd></dl></dd>
</dl><dl><dt>current_argument<a href="#discord.ext.commands.Context.current_argument" title="Permalink to this definition">¶</a></dt>
<dd>

The argument string of the <a href="#discord.ext.commands.Context.current_parameter" title="discord.ext.commands.Context.current_parameter"><code>current_parameter</code></a> that is currently being converted. This is only of use for within converters.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>interaction<a href="#discord.ext.commands.Context.interaction" title="Permalink to this definition">¶</a></dt>
<dd>

The interaction associated with this context.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction" title="discord.Interaction"><code>Interaction</code></a>]

</dd></dl></dd>
</dl><dl><dt>prefix<a href="#discord.ext.commands.Context.prefix" title="Permalink to this definition">¶</a></dt>
<dd>

The prefix that was used to invoke the command. For interaction based contexts, this is <code>/</code> for slash commands and <code>\u200b</code> for context menu commands.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>command<a href="#discord.ext.commands.Context.command" title="Permalink to this definition">¶</a></dt>
<dd>

The command that is being invoked currently.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>invoked_with<a href="#discord.ext.commands.Context.invoked_with" title="Permalink to this definition">¶</a></dt>
<dd>

The command name that triggered this invocation. Useful for finding out which alias called the command.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>invoked_parents<a href="#discord.ext.commands.Context.invoked_parents" title="Permalink to this definition">¶</a></dt>
<dd>

The command names of the parents that triggered this invocation. Useful for finding out which aliases called the command.

For example in commands <code>?a b c test</code>, the invoked parents are <code>['a', 'b', 'c']</code>.

New in version 1.7.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>invoked_subcommand<a href="#discord.ext.commands.Context.invoked_subcommand" title="Permalink to this definition">¶</a></dt>
<dd>

The subcommand that was invoked. If no valid subcommand was invoked then this is equal to <code>None</code>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>]

</dd></dl></dd>
</dl><dl><dt>subcommand_passed<a href="#discord.ext.commands.Context.subcommand_passed" title="Permalink to this definition">¶</a></dt>
<dd>

The string that was attempted to call a subcommand. This does not have to point to a valid registered subcommand and could just point to a nonsense string. If nothing was passed to attempt a call to a subcommand then this is set to <code>None</code>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>command_failed<a href="#discord.ext.commands.Context.command_failed" title="Permalink to this definition">¶</a></dt>
<dd>

A boolean that indicates if the command failed to be parsed, checked, or invoked.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*async with* typing(***, *ephemeral=False*)<a href="#discord.ext.commands.Context.typing" title="Permalink to this definition">¶</a></dt>
<dd>

Returns an asynchronous context manager that allows you to send a typing indicator to the destination for an indefinite period of time, or 10 seconds if the context manager is called using <code>await</code>.

In an interaction based context, this is equivalent to a <a href="#discord.ext.commands.Context.defer" title="discord.ext.commands.Context.defer"><code>defer()</code></a> call and does not do any typing calls.

Example Usage:

```
async with channel.typing():
    # simulate something heavy
    await asyncio.sleep(20)

await channel.send('Done!')

```

Example Usage:

```
await channel.typing()
# Do some computational magic for about 10 seconds
await channel.send('Done!')

```

Changed in version 2.0: This no longer works with the <code>with</code> syntax, <code>async with</code> must be used instead.

Changed in version 2.0: Added functionality to <code>await</code> the context manager to send a typing indicator for 10 seconds.

<dl><dt>Parameters</dt>
<dd>

**ephemeral** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

Indicates whether the deferred message will eventually be ephemeral. Only valid for interaction based contexts.

New in version 2.0.

</dd></dl></dd>
</dl><dl><dt>*classmethod await* from_interaction(*interaction*, */*)<a href="#discord.ext.commands.Context.from_interaction" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Creates a context from a <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a>. This only works on application command based interactions, such as slash commands or context menus.

On slash command based interactions this creates a synthetic <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a> that points to an ephemeral message that the command invoker has executed. This means that <a href="#discord.ext.commands.Context.author" title="discord.ext.commands.Context.author"><code>Context.author</code></a> returns the member that invoked the command.

In a message context menu based interaction, the <a href="#discord.ext.commands.Context.message" title="discord.ext.commands.Context.message"><code>Context.message</code></a> attribute is the message that the command is being executed on. This means that <a href="#discord.ext.commands.Context.author" title="discord.ext.commands.Context.author"><code>Context.author</code></a> returns the author of the message being targetted. To get the member that invoked the command then <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction.user" title="discord.Interaction.user"><code>discord.Interaction.user</code></a> should be used instead.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

**interaction** (<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction" title="discord.Interaction"><code>discord.Interaction</code></a>) – The interaction to create a context with.

</dd><dt>Raises</dt>
<dd>

- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The interaction does not have a valid command.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The interaction client is not derived from <a href="#discord.ext.commands.Bot" title="discord.ext.commands.Bot"><code>Bot</code></a> or <a href="#discord.ext.commands.AutoShardedBot" title="discord.ext.commands.AutoShardedBot"><code>AutoShardedBot</code></a>.

</dd></dl></dd>
</dl><dl><dt>*await* invoke(*command*, */*, **args*, ***kwargs*)<a href="#discord.ext.commands.Context.invoke" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Calls a command with the arguments given.

This is useful if you want to just call the callback that a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a> holds internally.

Note

This does not handle converters, checks, cooldowns, pre-invoke, or after-invoke hooks in any matter. It calls the internal callback directly as-if it was a regular function.

You must take care in passing the proper arguments when using this function.

Changed in version 2.0: <code>command</code> parameter is now positional-only.

<dl><dt>Parameters</dt>
<dd>

- **command** (<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>) – The command that is going to be called.
- **\*args** – The arguments to use.
- **\*\*kwargs** – The keyword arguments to use.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – The command argument to invoke is missing.

</dd></dl></dd>
</dl><dl><dt>*await* reinvoke(***, *call_hooks=False*, *restart=True*)<a href="#discord.ext.commands.Context.reinvoke" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Calls the command again.

This is similar to <a href="#discord.ext.commands.Context.invoke" title="discord.ext.commands.Context.invoke"><code>invoke()</code></a> except that it bypasses checks, cooldowns, and error handlers.

Note

If you want to bypass <a href="#discord.ext.commands.UserInputError" title="discord.ext.commands.UserInputError"><code>UserInputError</code></a> derived exceptions, it is recommended to use the regular <a href="#discord.ext.commands.Context.invoke" title="discord.ext.commands.Context.invoke"><code>invoke()</code></a> as it will work more naturally. After all, this will end up using the old arguments the user has used and will thus just fail again.

<dl><dt>Parameters</dt>
<dd>

- **call\_hooks** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to call the before and after invoke hooks.
- **restart** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether to start the call chain from the very beginning or where we left off (i.e. the command that caused the error). The default is to start where we left off.

</dd><dt>Raises</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The context to reinvoke is not valid.

</dd></dl></dd>
</dl><dl><dt>*property*valid<a href="#discord.ext.commands.Context.valid" title="Permalink to this definition">¶</a></dt>
<dd>

Checks if the invocation context is valid to be invoked with.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*clean_prefix<a href="#discord.ext.commands.Context.clean_prefix" title="Permalink to this definition">¶</a></dt>
<dd>

The cleaned up invoke prefix. i.e. mentions are <code>@name</code> instead of <code>&lt;@id&gt;</code>.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*cog<a href="#discord.ext.commands.Context.cog" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the cog associated with this context’s command. None if it does not exist.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*filesize_limit<a href="#discord.ext.commands.Context.filesize_limit" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the maximum number of bytes files can have when uploaded to this guild or DM channel associated with this context.

New in version 2.3.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>guild<a href="#discord.ext.commands.Context.guild" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the guild associated with this context’s command. None if not available.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>]

</dd></dl></dd>
</dl><dl><dt>channel<a href="#discord.ext.commands.Context.channel" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the channel associated with this context’s command. Shorthand for <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.channel" title="discord.Message.channel"><code>Message.channel</code></a>.

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable" title="discord.abc.Messageable"><code>abc.Messageable</code></a>]

</dd></dl></dd>
</dl><dl><dt>author<a href="#discord.ext.commands.Context.author" title="Permalink to this definition">¶</a></dt>
<dd>

Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a>]: Returns the author associated with this context’s command. Shorthand for <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.author" title="discord.Message.author"><code>Message.author</code></a>

</dd></dl><dl><dt>me<a href="#discord.ext.commands.Context.me" title="Permalink to this definition">¶</a></dt>
<dd>

Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientUser" title="discord.ClientUser"><code>ClientUser</code></a>]: Similar to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.me" title="discord.Guild.me"><code>Guild.me</code></a> except it may return the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientUser" title="discord.ClientUser"><code>ClientUser</code></a> in private message contexts.

</dd></dl><dl><dt>permissions<a href="#discord.ext.commands.Context.permissions" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the resolved permissions for the invoking user in this channel. Shorthand for <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel.permissions_for" title="discord.abc.GuildChannel.permissions_for"><code>abc.GuildChannel.permissions_for()</code></a> or <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction.permissions" title="discord.Interaction.permissions"><code>Interaction.permissions</code></a>.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>

</dd></dl></dd>
</dl><dl><dt>bot_permissions<a href="#discord.ext.commands.Context.bot_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

Returns the resolved permissions for the bot in this channel. Shorthand for <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel.permissions_for" title="discord.abc.GuildChannel.permissions_for"><code>abc.GuildChannel.permissions_for()</code></a> or <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.Interaction.app_permissions" title="discord.Interaction.app_permissions"><code>Interaction.app_permissions</code></a>.

For interaction-based commands, this will reflect the effective permissions for <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a> calls, which may differ from calls through other <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable" title="discord.abc.Messageable"><code>abc.Messageable</code></a> endpoints, like <a href="#discord.ext.commands.Context.channel" title="discord.ext.commands.Context.channel"><code>channel</code></a>.

Notably, sending messages, embedding links, and attaching files are always permitted, while reading messages might not be.

New in version 2.0.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions" title="discord.Permissions"><code>Permissions</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*voice_client<a href="#discord.ext.commands.Context.voice_client" title="Permalink to this definition">¶</a></dt>
<dd>

A shortcut to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild.voice_client" title="discord.Guild.voice_client"><code>Guild.voice_client</code></a>, if applicable.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.VoiceProtocol" title="discord.VoiceProtocol"><code>VoiceProtocol</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* send_help(*entity=&lt;bot&gt;*)<a href="#discord.ext.commands.Context.send_help" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Shows the help command for the specified entity if given. The entity can be a command or a cog.

If no entity is given, then it’ll show help for the entire bot.

If the entity is a string, then it looks up whether it’s a <a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a> or a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>.

Note

Due to the way this function works, instead of returning something similar to <a href="#discord.ext.commands.HelpCommand.command_not_found" title="discord.ext.commands.HelpCommand.command_not_found"><code>command_not_found()</code></a> this returns <code>None</code> on bad input or no help command.

<dl><dt>Parameters</dt>
<dd>

**entity** (Optional\[Union\[<a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>, <a href="#discord.ext.commands.Cog" title="discord.ext.commands.Cog"><code>Cog</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]]) – The entity to show help for.

</dd><dt>Returns</dt>
<dd>

The result of the help command, if any.

</dd><dt>Return type</dt>
<dd>

Any

</dd></dl></dd>
</dl><dl><dt>*await* fetch_message(*id*, */*)<a href="#discord.ext.commands.Context.fetch_message" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Retrieves a single <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a> from the destination.

<dl><dt>Parameters</dt>
<dd>

**id** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The message ID to look for.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.NotFound" title="discord.NotFound">**NotFound**</a> – The specified message was not found.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the permissions required to get a message.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the message failed.

</dd><dt>Returns</dt>
<dd>

The message asked for.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>

</dd></dl></dd>
</dl><dl><dt>*async for ... in* history(***, *limit=100*, *before=None*, *after=None*, *around=None*, *oldest_first=None*)<a href="#discord.ext.commands.Context.history" title="Permalink to this definition">¶</a></dt>
<dd>

Returns an <a href="https://docs.python.org/3/glossary.html#term-asynchronous-iterator" title="(in Python v3.14)">asynchronous iterator</a> that enables receiving the destination’s message history.

You must have <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.read_message_history" title="discord.Permissions.read_message_history"><code>read_message_history</code></a> to do this.

Examples

Usage

```
counter = 0
async for message in channel.history(limit=200):
    if message.author == client.user:
        counter += 1

```

Flattening into a list:

```
messages = [message async for message in channel.history(limit=123)]
# messages is now a list of Message...

```

All parameters are optional.

<dl><dt>Parameters</dt>
<dd>

- **limit** (Optional\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]) – The number of messages to retrieve. If <code>None</code>, retrieves every message in the channel. Note, however, that this would make it a slow operation.
- **before** (Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>, <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>]]) – Retrieve messages before this date or message. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
- **after** (Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>, <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>]]) – Retrieve messages after this date or message. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.
- **around** (Optional\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>Snowflake</code></a>, <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>]]) – Retrieve messages around this date or message. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time. When using this argument, the maximum limit is 101. Note that if the limit is an even number then this will return at most limit + 1 messages.
- **oldest\_first** (Optional\[<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]) – If set to <code>True</code>, return messages in oldest-&gt;newest order. Defaults to <code>True</code> if <code>after</code> is specified, otherwise <code>False</code>.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have permissions to get channel message history.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – The request to get message history failed.

</dd><dt>Yields</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a> – The message with the message data parsed.

</dd></dl></dd>
</dl><dl><dt>pins(***, *limit=50*, *before=None*, *oldest_first=False*)<a href="#discord.ext.commands.Context.pins" title="Permalink to this definition">¶</a></dt>
<dd>

Retrieves an <a href="https://docs.python.org/3/glossary.html#term-asynchronous-iterator" title="(in Python v3.14)">asynchronous iterator</a> of the pinned messages in the channel.

You must have <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.view_channel" title="discord.Permissions.view_channel"><code>view_channel</code></a> and <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Permissions.read_message_history" title="discord.Permissions.read_message_history"><code>read_message_history</code></a> in order to use this.

Changed in version 2.6: Due to a change in Discord’s API, this now returns a paginated iterator instead of a list.

For backwards compatibility, you can still retrieve a list of pinned messages by using <code>await</code> on the returned object. This is however deprecated.

Note

Due to a limitation with the Discord API, the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a> object returned by this method does not contain complete <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.reactions" title="discord.Message.reactions"><code>Message.reactions</code></a> data.

Examples

Usage

```
counter = 0
async for message in channel.pins(limit=250):
    counter += 1

```

Flattening into a list:

```
messages = [message async for message in channel.pins(limit=50)]
# messages is now a list of Message...

```

All parameters are optional.

<dl><dt>Parameters</dt>
<dd>

- **limit** (*Optional**\[*<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)">*int*</a>*]*) –

  The number of pinned messages to retrieve. If <code>None</code>, it retrieves every pinned message in the channel. Note, however, that this would make it a slow operation. Defaults to <code>50</code>.

  New in version 2.6.
- **before** (Optional\[Union\[<a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Snowflake" title="discord.abc.Snowflake"><code>abc.Snowflake</code></a>]]) –

  Retrieve pinned messages before this time or snowflake. If a datetime is provided, it is recommended to use a UTC aware datetime. If the datetime is naive, it is assumed to be local time.

  New in version 2.6.
- **oldest\_first** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  If set to <code>True</code>, return messages in oldest pin-&gt;newest pin order. Defaults to <code>False</code>.

  New in version 2.6.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the permission to retrieve pinned messages.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Retrieving the pinned messages failed.

</dd><dt>Yields</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a> – The pinned message with <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.pinned_at" title="discord.Message.pinned_at"><code>Message.pinned_at</code></a> set.

</dd></dl></dd>
</dl><dl><dt>*await* reply(*content=None*, ***kwargs*)<a href="#discord.ext.commands.Context.reply" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

A shortcut method to <a href="#discord.ext.commands.Context.send" title="discord.ext.commands.Context.send"><code>send()</code></a> to reply to the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a> referenced by this context.

For interaction based contexts, this is the same as <a href="#discord.ext.commands.Context.send" title="discord.ext.commands.Context.send"><code>send()</code></a>.

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
</dl><dl><dt>*await* defer(***, *ephemeral=False*)<a href="#discord.ext.commands.Context.defer" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Defers the interaction based contexts.

This is typically used when the interaction is acknowledged and a secondary action will be done later.

If this isn’t an interaction based context then it does nothing.

<dl><dt>Parameters</dt>
<dd>

**ephemeral** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Indicates whether the deferred message will eventually be ephemeral.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Deferring the interaction failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.InteractionResponded" title="discord.InteractionResponded">**InteractionResponded**</a> – This interaction has already been responded to before.

</dd></dl></dd>
</dl><dl><dt>*await* send(*content=None*, ***, *tts=False*, *embed=None*, *embeds=None*, *file=None*, *files=None*, *stickers=None*, *delete_after=None*, *nonce=None*, *allowed_mentions=None*, *reference=None*, *mention_author=None*, *view=None*, *suppress_embeds=False*, *ephemeral=False*, *silent=False*, *poll=None*)<a href="#discord.ext.commands.Context.send" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Sends a message to the destination with the content given.

This works similarly to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.Messageable.send" title="discord.abc.Messageable.send"><code>send()</code></a> for non-interaction contexts.

For interaction based contexts this does one of the following:

- <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.InteractionResponse.send_message" title="discord.InteractionResponse.send_message"><code>discord.InteractionResponse.send_message()</code></a> if no response has been given.
- A followup message if a response has been given.
- Regular send if the interaction has expired

Changed in version 2.0: This function will now raise <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)"><code>TypeError</code></a> or <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)"><code>ValueError</code></a> instead of <code>InvalidArgument</code>.

<dl><dt>Parameters</dt>
<dd>

- **content** (Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – The content of the message to send.
- **tts** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Indicates if the message should be sent using text-to-speech.
- **embed** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed" title="discord.Embed"><code>Embed</code></a>) – The rich embed for the content.
- **file** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>File</code></a>) – The file to upload.
- **files** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.File" title="discord.File"><code>File</code></a>]) – A list of files to upload. Must be a maximum of 10.
- **nonce** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The nonce to use for sending this message. If the message was successfully sent, then the message will have a nonce with this value.
- **delete\_after** (<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>) – If provided, the number of seconds to wait in the background before deleting the message we just sent. If the deletion fails, then it is silently ignored.
- **allowed\_mentions** (<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AllowedMentions" title="discord.AllowedMentions"><code>AllowedMentions</code></a>) –

  Controls the mentions being processed in this message. If this is passed, then the object is merged with <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client.allowed_mentions" title="discord.Client.allowed_mentions"><code>allowed_mentions</code></a>. The merging behaviour only overrides attributes that have been explicitly passed to the object, otherwise it uses the attributes set in <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client.allowed_mentions" title="discord.Client.allowed_mentions"><code>allowed_mentions</code></a>. If no object is passed at all then the defaults given by <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Client.allowed_mentions" title="discord.Client.allowed_mentions"><code>allowed_mentions</code></a> are used instead.

  New in version 1.4.
- **reference** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MessageReference" title="discord.MessageReference"><code>MessageReference</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialMessage" title="discord.PartialMessage"><code>PartialMessage</code></a>]) –

  A reference to the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a> to which you are replying, this can be created using <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.to_reference" title="discord.Message.to_reference"><code>to_reference()</code></a> or passed directly as a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>. You can control whether this mentions the author of the referenced message using the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AllowedMentions.replied_user" title="discord.AllowedMentions.replied_user"><code>replied_user</code></a> attribute of <code>allowed_mentions</code> or by setting <code>mention_author</code>.

  This is ignored for interaction based contexts.

  New in version 1.6.
- **mention\_author** (Optional\[<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]) –

  If set, overrides the <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.AllowedMentions.replied_user" title="discord.AllowedMentions.replied_user"><code>replied_user</code></a> attribute of <code>allowed_mentions</code>. This is ignored for interaction based contexts.

  New in version 1.6.
- **view** (Union\[<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.View" title="discord.ui.View"><code>discord.ui.View</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.LayoutView" title="discord.ui.LayoutView"><code>discord.ui.LayoutView</code></a>]) –

  A Discord UI View to add to the message.

  New in version 2.0.
- **embeds** (List\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Embed" title="discord.Embed"><code>Embed</code></a>]) –

  A list of embeds to upload. Must be a maximum of 10.

  New in version 2.0.
- **stickers** (Sequence\[Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.GuildSticker" title="discord.GuildSticker"><code>GuildSticker</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.StickerItem" title="discord.StickerItem"><code>StickerItem</code></a>]]) –

  A list of stickers to upload. Must be a maximum of 3. This is ignored for interaction based contexts.

  New in version 2.0.
- **suppress\_embeds** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether to suppress embeds for the message. This sends the message without any embeds if set to <code>True</code>.

  New in version 2.0.
- **ephemeral** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Indicates if the message should only be visible to the user who started the interaction. If a view is sent with an ephemeral message and it has no timeout set then the timeout is set to 15 minutes. **This is only applicable in contexts with an interaction**.

  New in version 2.0.
- **silent** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether to suppress push and desktop notifications for the message. This will increment the mention counter in the UI, but will not actually send a notification.

  New in version 2.2.
- **poll** (Optional\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Poll" title="discord.Poll"><code>Poll</code></a>]) –

  The poll to send with this message.

  New in version 2.4.

  Changed in version 2.6: This can now be <code>None</code> and defaults to <code>None</code> instead of <code>MISSING</code>.

</dd><dt>Raises</dt>
<dd>

- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.HTTPException" title="discord.HTTPException">**HTTPException**</a> – Sending the message failed.
- <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Forbidden" title="discord.Forbidden">**Forbidden**</a> – You do not have the proper permissions to send the message.
- <a href="https://docs.python.org/3/library/exceptions.html#ValueError" title="(in Python v3.14)">**ValueError**</a> – The <code>files</code> list is not of the appropriate size.
- <a href="https://docs.python.org/3/library/exceptions.html#TypeError" title="(in Python v3.14)">**TypeError**</a> – You specified both <code>file</code> and <code>files</code>, or you specified both <code>embed</code> and <code>embeds</code>, or the <code>reference</code> object is not a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MessageReference" title="discord.MessageReference"><code>MessageReference</code></a> or <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialMessage" title="discord.PartialMessage"><code>PartialMessage</code></a>.

</dd><dt>Returns</dt>
<dd>

The message that was sent.

</dd><dt>Return type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>Message</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

## Converters ¶

Methods

- async [convert](#discord.ext.commands.Converter.convert)

<dl><dt>*class*discord.ext.commands.Converter(**args*, ***kwargs*)<a href="#discord.ext.commands.Converter" title="Permalink to this definition">¶</a></dt>
<dd>

The base class of custom converters that require the <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a> to be passed to be useful.

This allows you to implement converters that function similar to the special cased <code>discord</code> classes.

Classes that derive from this should override the <a href="#discord.ext.commands.Converter.convert" title="discord.ext.commands.Converter.convert"><code>convert()</code></a> method to do its conversion logic. This method must be a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine" title="(in Python v3.14)">coroutine</a>.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.Converter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.ObjectConverter.convert)

<dl><dt>*class*discord.ext.commands.ObjectConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.ObjectConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Object" title="discord.Object"><code>Object</code></a>.

The argument must follow the valid ID or mention formats (e.g. <code>&lt;@80088516616269824&gt;</code>).

New in version 2.0.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by member, role, or channel mention.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.ObjectConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.MemberConverter.convert)

<dl><dt>*class*discord.ext.commands.MemberConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.MemberConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Member" title="discord.Member"><code>Member</code></a>.

All lookups are via the local guild. If in a DM context, then the lookup is done by the global cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by mention.
3. Lookup by username#discriminator (deprecated).
4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
5. Lookup by user name.
6. Lookup by global name.
7. Lookup by guild nickname.

Changed in version 1.5: Raise <a href="#discord.ext.commands.MemberNotFound" title="discord.ext.commands.MemberNotFound"><code>MemberNotFound</code></a> instead of generic <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

Changed in version 1.5.1: This converter now lazily fetches members from the gateway and HTTP APIs, optionally caching the result if <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.MemberCacheFlags.joined" title="discord.MemberCacheFlags.joined"><code>MemberCacheFlags.joined</code></a> is enabled.

Deprecated since version 2.3: Looking up users by discriminator will be removed in a future version due to the removal of discriminators in an API change.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.MemberConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.UserConverter.convert)

<dl><dt>*class*discord.ext.commands.UserConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.UserConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.User" title="discord.User"><code>User</code></a>.

All lookups are via the global user cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by mention.
3. Lookup by username#discriminator (deprecated).
4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
5. Lookup by user name.
6. Lookup by global name.

Changed in version 1.5: Raise <a href="#discord.ext.commands.UserNotFound" title="discord.ext.commands.UserNotFound"><code>UserNotFound</code></a> instead of generic <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

Changed in version 1.6: This converter now lazily fetches users from the HTTP APIs if an ID is passed and it’s not available in cache.

Deprecated since version 2.3: Looking up users by discriminator will be removed in a future version due to the removal of discriminators in an API change.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.UserConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.MessageConverter.convert)

<dl><dt>*class*discord.ext.commands.MessageConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.MessageConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message" title="discord.Message"><code>discord.Message</code></a>.

New in version 1.1.

The lookup strategy is as follows (in order):

1. Lookup by “{channel ID}-{message ID}” (retrieved by shift-clicking on “Copy ID”)
2. Lookup by message ID (the message **must** be in the context channel)
3. Lookup by message URL

Changed in version 1.5: Raise <a href="#discord.ext.commands.ChannelNotFound" title="discord.ext.commands.ChannelNotFound"><code>ChannelNotFound</code></a>, <a href="#discord.ext.commands.MessageNotFound" title="discord.ext.commands.MessageNotFound"><code>MessageNotFound</code></a> or <a href="#discord.ext.commands.ChannelNotReadable" title="discord.ext.commands.ChannelNotReadable"><code>ChannelNotReadable</code></a> instead of generic <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.MessageConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.PartialMessageConverter.convert)

<dl><dt>*class*discord.ext.commands.PartialMessageConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.PartialMessageConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialMessage" title="discord.PartialMessage"><code>discord.PartialMessage</code></a>.

New in version 1.7.

The creation strategy is as follows (in order):

1. By “{channel ID}-{message ID}” (retrieved by shift-clicking on “Copy ID”)
2. By message ID (The message is assumed to be in the context channel.)
3. By message URL

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.PartialMessageConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.GuildChannelConverter.convert)

<dl><dt>*class*discord.ext.commands.GuildChannelConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.GuildChannelConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>GuildChannel</code></a>.

All lookups are via the local guild. If in a DM context, then the lookup is done by the global cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by mention.
3. Lookup by channel URL.
4. Lookup by name.

New in version 2.0.

Changed in version 2.4: Add lookup by channel URL, accessed via “Copy Link” in the Discord client within channels.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.GuildChannelConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.TextChannelConverter.convert)

<dl><dt>*class*discord.ext.commands.TextChannelConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.TextChannelConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.TextChannel" title="discord.TextChannel"><code>TextChannel</code></a>.

All lookups are via the local guild. If in a DM context, then the lookup is done by the global cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by mention.
3. Lookup by channel URL.
4. Lookup by name

Changed in version 1.5: Raise <a href="#discord.ext.commands.ChannelNotFound" title="discord.ext.commands.ChannelNotFound"><code>ChannelNotFound</code></a> instead of generic <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

Changed in version 2.4: Add lookup by channel URL, accessed via “Copy Link” in the Discord client within channels.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.TextChannelConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.VoiceChannelConverter.convert)

<dl><dt>*class*discord.ext.commands.VoiceChannelConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.VoiceChannelConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.VoiceChannel" title="discord.VoiceChannel"><code>VoiceChannel</code></a>.

All lookups are via the local guild. If in a DM context, then the lookup is done by the global cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by mention.
3. Lookup by channel URL.
4. Lookup by name

Changed in version 1.5: Raise <a href="#discord.ext.commands.ChannelNotFound" title="discord.ext.commands.ChannelNotFound"><code>ChannelNotFound</code></a> instead of generic <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

Changed in version 2.4: Add lookup by channel URL, accessed via “Copy Link” in the Discord client within channels.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.VoiceChannelConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.StageChannelConverter.convert)

<dl><dt>*class*discord.ext.commands.StageChannelConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.StageChannelConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.StageChannel" title="discord.StageChannel"><code>StageChannel</code></a>.

New in version 1.7.

All lookups are via the local guild. If in a DM context, then the lookup is done by the global cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by mention.
3. Lookup by channel URL.
4. Lookup by name

Changed in version 2.4: Add lookup by channel URL, accessed via “Copy Link” in the Discord client within channels.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.StageChannelConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.CategoryChannelConverter.convert)

<dl><dt>*class*discord.ext.commands.CategoryChannelConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.CategoryChannelConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.CategoryChannel" title="discord.CategoryChannel"><code>CategoryChannel</code></a>.

All lookups are via the local guild. If in a DM context, then the lookup is done by the global cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by mention.
3. Lookup by channel URL.
4. Lookup by name

Changed in version 2.4: Add lookup by channel URL, accessed via “Copy Link” in the Discord client within channels.

Changed in version 1.5: Raise <a href="#discord.ext.commands.ChannelNotFound" title="discord.ext.commands.ChannelNotFound"><code>ChannelNotFound</code></a> instead of generic <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.CategoryChannelConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.ForumChannelConverter.convert)

<dl><dt>*class*discord.ext.commands.ForumChannelConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.ForumChannelConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ForumChannel" title="discord.ForumChannel"><code>ForumChannel</code></a>.

All lookups are via the local guild. If in a DM context, then the lookup is done by the global cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by mention.
3. Lookup by channel URL.
4. Lookup by name

New in version 2.0.

Changed in version 2.4: Add lookup by channel URL, accessed via “Copy Link” in the Discord client within channels.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.ForumChannelConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.InviteConverter.convert)

<dl><dt>*class*discord.ext.commands.InviteConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.InviteConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Invite" title="discord.Invite"><code>Invite</code></a>.

This is done via an HTTP request using <a href="#discord.ext.commands.Bot.fetch_invite" title="discord.ext.commands.Bot.fetch_invite"><code>Bot.fetch_invite()</code></a>.

Changed in version 1.5: Raise <a href="#discord.ext.commands.BadInviteArgument" title="discord.ext.commands.BadInviteArgument"><code>BadInviteArgument</code></a> instead of generic <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.InviteConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.GuildConverter.convert)

<dl><dt>*class*discord.ext.commands.GuildConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.GuildConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Guild" title="discord.Guild"><code>Guild</code></a>.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).

New in version 1.7.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.GuildConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.RoleConverter.convert)

<dl><dt>*class*discord.ext.commands.RoleConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.RoleConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Role" title="discord.Role"><code>Role</code></a>.

All lookups are via the local guild. If in a DM context, the converter raises <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> exception.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by mention.
3. Lookup by name

Changed in version 1.5: Raise <a href="#discord.ext.commands.RoleNotFound" title="discord.ext.commands.RoleNotFound"><code>RoleNotFound</code></a> instead of generic <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.RoleConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.GameConverter.convert)

<dl><dt>*class*discord.ext.commands.GameConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.GameConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Game" title="discord.Game"><code>Game</code></a>.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.GameConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.ColourConverter.convert)

<dl><dt>*class*discord.ext.commands.ColourConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.ColourConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Colour" title="discord.Colour"><code>Colour</code></a>.

Changed in version 1.5: Add an alias named ColorConverter

The following formats are accepted:

- <code>0x&lt;hex&gt;</code>
- <code>#&lt;hex&gt;</code>
- <code>0x#&lt;hex&gt;</code>
- <code>rgb(&lt;number&gt;, &lt;number&gt;, &lt;number&gt;)</code>
- Any of the <code>classmethod</code> in <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Colour" title="discord.Colour"><code>Colour</code></a>
  > - The <code>_</code> in the name can be optionally replaced with spaces.

Like CSS, <code>&lt;number&gt;</code> can be either 0-255 or 0-100% and <code>&lt;hex&gt;</code> can be either a 6 digit hex number or a 3 digit hex shortcut (e.g. #fff).

Changed in version 1.5: Raise <a href="#discord.ext.commands.BadColourArgument" title="discord.ext.commands.BadColourArgument"><code>BadColourArgument</code></a> instead of generic <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

Changed in version 1.7: Added support for <code>rgb</code> function and 3-digit hex shortcuts

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.ColourConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.EmojiConverter.convert)

<dl><dt>*class*discord.ext.commands.EmojiConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.EmojiConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Emoji" title="discord.Emoji"><code>Emoji</code></a>.

All lookups are done for the local guild first, if available. If that lookup fails, then it checks the client’s global cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by extracting ID from the emoji.
3. Lookup by name

Changed in version 1.5: Raise <a href="#discord.ext.commands.EmojiNotFound" title="discord.ext.commands.EmojiNotFound"><code>EmojiNotFound</code></a> instead of generic <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.EmojiConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.PartialEmojiConverter.convert)

<dl><dt>*class*discord.ext.commands.PartialEmojiConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.PartialEmojiConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.PartialEmoji" title="discord.PartialEmoji"><code>PartialEmoji</code></a>.

This is done by extracting the animated flag, name and ID from the emoji.

Changed in version 1.5: Raise <a href="#discord.ext.commands.PartialEmojiConversionFailure" title="discord.ext.commands.PartialEmojiConversionFailure"><code>PartialEmojiConversionFailure</code></a> instead of generic <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.PartialEmojiConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.ThreadConverter.convert)

<dl><dt>*class*discord.ext.commands.ThreadConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.ThreadConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a>.

All lookups are via the local guild.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by mention.
3. Lookup by channel URL.
4. Lookup by name.

Changed in version 2.4: Add lookup by channel URL, accessed via “Copy Link” in the Discord client within channels.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.ThreadConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.GuildStickerConverter.convert)

<dl><dt>*class*discord.ext.commands.GuildStickerConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.GuildStickerConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.GuildSticker" title="discord.GuildSticker"><code>GuildSticker</code></a>.

All lookups are done for the local guild first, if available. If that lookup fails, then it checks the client’s global cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by name.

New in version 2.0.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.GuildStickerConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.ScheduledEventConverter.convert)

<dl><dt>*class*discord.ext.commands.ScheduledEventConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.ScheduledEventConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ScheduledEvent" title="discord.ScheduledEvent"><code>ScheduledEvent</code></a>.

Lookups are done for the local guild if available. Otherwise, for a DM context, lookup is done by the global cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by url.
3. Lookup by name.

New in version 2.0.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.ScheduledEventConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.SoundboardSoundConverter.convert)

<dl><dt>*class*discord.ext.commands.SoundboardSoundConverter(**args*, ***kwargs*)<a href="#discord.ext.commands.SoundboardSoundConverter" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.SoundboardSound" title="discord.SoundboardSound"><code>SoundboardSound</code></a>.

Lookups are done for the local guild if available. Otherwise, for a DM context, lookup is done by the global cache.

The lookup strategy is as follows (in order):

1. Lookup by ID.
2. Lookup by name.

New in version 2.5.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.SoundboardSoundConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Methods

- async [convert](#discord.ext.commands.Timestamp.convert)

<dl><dt>*class*discord.ext.commands.Timestamp(**args*, ***kwargs*)<a href="#discord.ext.commands.Timestamp" title="Permalink to this definition">¶</a></dt>
<dd>

Converts to a <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime" title="(in Python v3.14)"><code>datetime.datetime</code></a>.

Conversion is attempted based on the <a href="https://discord.com/developers/docs/reference#message-formatting">Discord style timestamp</a> input format.

New in version 2.7.

Warning

Due to a Discord limitation, no timezone is provided with the input. The UTC timezone has been supplanted instead.

<dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.Timestamp.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

Attributes

- [escape\_markdown](#discord.ext.commands.clean_content.escape_markdown)
- [fix\_channel\_mentions](#discord.ext.commands.clean_content.fix_channel_mentions)
- [remove\_markdown](#discord.ext.commands.clean_content.remove_markdown)
- [use\_nicknames](#discord.ext.commands.clean_content.use_nicknames)

Methods

- async [convert](#discord.ext.commands.clean_content.convert)

<dl><dt>*class*discord.ext.commands.clean_content(***, *fix_channel_mentions=False*, *use_nicknames=True*, *escape_markdown=False*, *remove_markdown=False*)<a href="#discord.ext.commands.clean_content" title="Permalink to this definition">¶</a></dt>
<dd>

Converts the argument to mention scrubbed version of said content.

This behaves similarly to <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.clean_content" title="discord.Message.clean_content"><code>clean_content</code></a>.

<dl><dt>fix_channel_mentions<a href="#discord.ext.commands.clean_content.fix_channel_mentions" title="Permalink to this definition">¶</a></dt>
<dd>

Whether to clean channel mentions.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>use_nicknames<a href="#discord.ext.commands.clean_content.use_nicknames" title="Permalink to this definition">¶</a></dt>
<dd>

Whether to use nicknames when transforming mentions.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>escape_markdown<a href="#discord.ext.commands.clean_content.escape_markdown" title="Permalink to this definition">¶</a></dt>
<dd>

Whether to also escape special markdown characters.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>remove_markdown<a href="#discord.ext.commands.clean_content.remove_markdown" title="Permalink to this definition">¶</a></dt>
<dd>

Whether to also remove special markdown characters. This option is not supported with <code>escape_markdown</code>

New in version 1.7.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.clean_content.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method to override to do conversion logic.

If an error is found while converting, it is recommended to raise a <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> derived exception as it will properly propagate to the error handlers.

Note that if this method is called manually, <a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a> should be caught to handle the cases where a subclass does not explicitly inherit from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that the argument is being used in.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument that is being converted.

</dd><dt>Raises</dt>
<dd>

- <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – A generic exception occurred when converting the argument.
- <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument">**BadArgument**</a> – The converter failed to convert the argument.

</dd></dl></dd>
</dl></dd>
</dl>

<dl><dt>*class*discord.ext.commands.Greedy<a href="#discord.ext.commands.Greedy" title="Permalink to this definition">¶</a></dt>
<dd>

A special converter that greedily consumes arguments until it can’t. As a consequence of this behaviour, most input errors are silently discarded, since it is used as an indicator of when to stop parsing.

When a parser error is met the greedy converter stops converting, undoes the internal string parsing routine, and continues parsing regularly.

For example, in the following code:

```
@commands.command()
async def test(ctx, numbers: Greedy[int], reason: str):
    await ctx.send("numbers: {}, reason: {}".format(numbers, reason))

```

An invocation of <code>[p]test 1 2 3 4 5 6 hello</code> would pass <code>numbers</code> with <code>[1, 2, 3, 4, 5, 6]</code> and <code>reason</code> with <code>hello</code>.

For more information, check <a href="https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#ext-commands-special-converters">Special Converters</a>.

Note

For interaction based contexts the conversion error is propagated rather than swallowed due to the difference in user experience with application commands.

</dd></dl>

<dl><dt>*class*discord.ext.commands.Range<a href="#discord.ext.commands.Range" title="Permalink to this definition">¶</a></dt>
<dd>

A special converter that can be applied to a parameter to require a numeric or string type to fit within the range provided.

During type checking time this is equivalent to <a href="https://docs.python.org/3/library/typing.html#typing.Annotated" title="(in Python v3.14)"><code>typing.Annotated</code></a> so type checkers understand the intent of the code.

Some example ranges:

- <code>Range[int, 10]</code> means the minimum is 10 with no maximum.
- <code>Range[int, None, 10]</code> means the maximum is 10 with no minimum.
- <code>Range[int, 1, 10]</code> means the minimum is 1 and the maximum is 10.
- <code>Range[float, 1.0, 5.0]</code> means the minimum is 1.0 and the maximum is 5.0.
- <code>Range[str, 1, 10]</code> means the minimum length is 1 and the maximum length is 10.

Inside a <a href="#discord.ext.commands.HybridCommand" title="discord.ext.commands.HybridCommand"><code>HybridCommand</code></a> this functions equivalently to <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Range" title="discord.app_commands.Range"><code>discord.app_commands.Range</code></a>.

If the value cannot be converted to the provided type or is outside the given range, <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a> or <a href="#discord.ext.commands.RangeError" title="discord.ext.commands.RangeError"><code>RangeError</code></a> is raised to the appropriate error handlers respectively.

New in version 2.0.

Examples

```
@bot.command()
async def range(ctx: commands.Context, value: commands.Range[int, 10, 12]):
    await ctx.send(f'Your value is {value}')

```

</dd></dl><dl><dt>*await* discord.ext.commands.run_converters(*ctx*, *converter*, *argument*, *param*)<a href="#discord.ext.commands.run_converters" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Runs converters for a given converter, argument, and parameter.

This function does the same work that the library does under the hood.

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context to run the converters under.
- **converter** (*Any*) – The converter to run, this corresponds to the annotation in the function.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument to convert to.
- **param** (<a href="#discord.ext.commands.Parameter" title="discord.ext.commands.Parameter"><code>Parameter</code></a>) – The parameter being converted. This is mainly for error reporting.

</dd><dt>Raises</dt>
<dd>

<a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError">**CommandError**</a> – The converter failed to convert.

</dd><dt>Returns</dt>
<dd>

The resulting conversion.

</dd><dt>Return type</dt>
<dd>

Any

</dd></dl></dd>
</dl>

### Flag Converter ¶

Methods

- cls [FlagConverter.convert](#discord.ext.commands.FlagConverter.convert)
- cls [FlagConverter.get\_flags](#discord.ext.commands.FlagConverter.get_flags)

<dl><dt>*class*discord.ext.commands.FlagConverter<a href="#discord.ext.commands.FlagConverter" title="Permalink to this definition">¶</a></dt>
<dd>

A converter that allows for a user-friendly flag syntax.

The flags are defined using <a href="https://www.python.org/dev/peps/pep-0526">**PEP 526**</a> type annotations similar to the <a href="https://docs.python.org/3/library/dataclasses.html#module-dataclasses" title="(in Python v3.14)"><code>dataclasses</code></a> Python module. For more information on how this converter works, check the appropriate <a href="https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html#ext-commands-flag-converter">documentation</a>.

<dl><dt>iter(x)</dt>
<dd>

Returns an iterator of <code>(flag_name, flag_value)</code> pairs. This allows it to be, for example, constructed as a dict or a list of pairs. Note that aliases are not shown.

</dd></dl>

New in version 2.0.

<dl><dt>Parameters</dt>
<dd>

- **case\_insensitive** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – A class parameter to toggle case insensitivity of the flag parsing. If <code>True</code> then flags are parsed in a case insensitive manner. Defaults to <code>False</code>.
- **prefix** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The prefix that all flags must be prefixed with. By default there is no prefix.
- **delimiter** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The delimiter that separates a flag’s argument from the flag’s name. By default this is <code>:</code>.

</dd></dl><dl><dt>*classmethod* get_flags()<a href="#discord.ext.commands.FlagConverter.get_flags" title="Permalink to this definition">¶</a></dt>
<dd>

Dict\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="#discord.ext.commands.Flag" title="discord.ext.commands.Flag"><code>Flag</code></a>]: A mapping of flag name to flag object this converter has.

</dd></dl><dl><dt>*classmethod await* convert(*ctx*, *argument*)<a href="#discord.ext.commands.FlagConverter.convert" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

The method that actually converters an argument to the flag mapping.

<dl><dt>Parameters</dt>
<dd>

- **ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context.
- **argument** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The argument to convert from.

</dd><dt>Raises</dt>
<dd>

<a href="#discord.ext.commands.FlagError" title="discord.ext.commands.FlagError">**FlagError**</a> – A flag related parsing error.

</dd><dt>Returns</dt>
<dd>

The flag converter instance with all flags parsed.

</dd><dt>Return type</dt>
<dd>

<a href="#discord.ext.commands.FlagConverter" title="discord.ext.commands.FlagConverter"><code>FlagConverter</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

Attributes

- [aliases](#discord.ext.commands.Flag.aliases)
- [annotation](#discord.ext.commands.Flag.annotation)
- [attribute](#discord.ext.commands.Flag.attribute)
- [default](#discord.ext.commands.Flag.default)
- [description](#discord.ext.commands.Flag.description)
- [max\_args](#discord.ext.commands.Flag.max_args)
- [name](#discord.ext.commands.Flag.name)
- [override](#discord.ext.commands.Flag.override)
- [positional](#discord.ext.commands.Flag.positional)
- [required](#discord.ext.commands.Flag.required)

<dl><dt>*class*discord.ext.commands.Flag<a href="#discord.ext.commands.Flag" title="Permalink to this definition">¶</a></dt>
<dd>

Represents a flag parameter for <a href="#discord.ext.commands.FlagConverter" title="discord.ext.commands.FlagConverter"><code>FlagConverter</code></a>.

The <a href="#discord.ext.commands.flag" title="discord.ext.commands.flag"><code>flag()</code></a> function helps create these flag objects, but it is not necessary to do so. These cannot be constructed manually.

<dl><dt>name<a href="#discord.ext.commands.Flag.name" title="Permalink to this definition">¶</a></dt>
<dd>

The name of the flag.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>aliases<a href="#discord.ext.commands.Flag.aliases" title="Permalink to this definition">¶</a></dt>
<dd>

The aliases of the flag name.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>attribute<a href="#discord.ext.commands.Flag.attribute" title="Permalink to this definition">¶</a></dt>
<dd>

The attribute in the class that corresponds to this flag.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>default<a href="#discord.ext.commands.Flag.default" title="Permalink to this definition">¶</a></dt>
<dd>

The default value of the flag, if available.

<dl><dt>Type</dt>
<dd>

Any

</dd></dl></dd>
</dl><dl><dt>annotation<a href="#discord.ext.commands.Flag.annotation" title="Permalink to this definition">¶</a></dt>
<dd>

The underlying evaluated annotation of the flag.

<dl><dt>Type</dt>
<dd>

Any

</dd></dl></dd>
</dl><dl><dt>max_args<a href="#discord.ext.commands.Flag.max_args" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of arguments the flag can accept. A negative value indicates an unlimited amount of arguments.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>override<a href="#discord.ext.commands.Flag.override" title="Permalink to this definition">¶</a></dt>
<dd>

Whether multiple given values overrides the previous value.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>description<a href="#discord.ext.commands.Flag.description" title="Permalink to this definition">¶</a></dt>
<dd>

The description of the flag. Shown for hybrid commands when they’re used as application commands.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>positional<a href="#discord.ext.commands.Flag.positional" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the flag is positional or not. There can only be one positional flag.

New in version 2.4.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*required<a href="#discord.ext.commands.Flag.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the flag is required.

A required flag has no default value.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>discord.ext.commands.flag(***, *name=...*, *aliases=...*, *default=...*, *max_args=...*, *override=...*, *converter=...*, *description=...*, *positional=...*)<a href="#discord.ext.commands.flag" title="Permalink to this definition">¶</a></dt>
<dd>

Override default functionality and parameters of the underlying <a href="#discord.ext.commands.FlagConverter" title="discord.ext.commands.FlagConverter"><code>FlagConverter</code></a> class attributes.

<dl><dt>Parameters</dt>
<dd>

- **name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The flag name. If not given, defaults to the attribute name.
- **aliases** (List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]) – Aliases to the flag name. If not given no aliases are set.
- **default** (*Any*) – The default parameter. This could be either a value or a callable that takes <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a> as its sole parameter. If not given then it defaults to the default value given to the attribute.
- **max\_args** (<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>) – The maximum number of arguments the flag can accept. A negative value indicates an unlimited amount of arguments. The default value depends on the annotation given.
- **override** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) – Whether multiple given values overrides the previous value. The default value depends on the annotation given.
- **converter** (*Any*) – The converter to use for this flag. This replaces the annotation at runtime which is transparent to type checkers.
- **description** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The description of the flag. Shown for hybrid commands when they’re used as application commands.
- **positional** (<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>) –

  Whether the flag is positional or not. There can only be one positional flag.

  New in version 2.4.

</dd></dl></dd>
</dl>

## Defaults ¶

Attributes

- [annotation](#discord.ext.commands.Parameter.annotation)
- [converter](#discord.ext.commands.Parameter.converter)
- [default](#discord.ext.commands.Parameter.default)
- [description](#discord.ext.commands.Parameter.description)
- [displayed\_default](#discord.ext.commands.Parameter.displayed_default)
- [displayed\_name](#discord.ext.commands.Parameter.displayed_name)
- [kind](#discord.ext.commands.Parameter.kind)
- [name](#discord.ext.commands.Parameter.name)
- [required](#discord.ext.commands.Parameter.required)

Methods

- async [get\_default](#discord.ext.commands.Parameter.get_default)
- def [replace](#discord.ext.commands.Parameter.replace)

<dl><dt>*class*discord.ext.commands.Parameter<a href="#discord.ext.commands.Parameter" title="Permalink to this definition">¶</a></dt>
<dd>

A class that stores information on a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>'s parameter.

This is a subclass of <a href="https://docs.python.org/3/library/inspect.html#inspect.Parameter" title="(in Python v3.14)"><code>inspect.Parameter</code></a>.

New in version 2.0.

<dl><dt>replace(***, *name=...*, *kind=...*, *default=...*, *annotation=...*, *description=...*, *displayed_default=...*, *displayed_name=...*)<a href="#discord.ext.commands.Parameter.replace" title="Permalink to this definition">¶</a></dt>
<dd>

Creates a customized copy of the Parameter.

</dd></dl><dl><dt>*property*name<a href="#discord.ext.commands.Parameter.name" title="Permalink to this definition">¶</a></dt>
<dd>

The parameter’s name.

</dd></dl><dl><dt>*property*kind<a href="#discord.ext.commands.Parameter.kind" title="Permalink to this definition">¶</a></dt>
<dd>

The parameter’s kind.

</dd></dl><dl><dt>*property*default<a href="#discord.ext.commands.Parameter.default" title="Permalink to this definition">¶</a></dt>
<dd>

The parameter’s default.

</dd></dl><dl><dt>*property*annotation<a href="#discord.ext.commands.Parameter.annotation" title="Permalink to this definition">¶</a></dt>
<dd>

The parameter’s annotation.

</dd></dl><dl><dt>*property*required<a href="#discord.ext.commands.Parameter.required" title="Permalink to this definition">¶</a></dt>
<dd>

Whether this parameter is required.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl><dl><dt>*property*converter<a href="#discord.ext.commands.Parameter.converter" title="Permalink to this definition">¶</a></dt>
<dd>

The converter that should be used for this parameter.

</dd></dl><dl><dt>*property*description<a href="#discord.ext.commands.Parameter.description" title="Permalink to this definition">¶</a></dt>
<dd>

The description of this parameter.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*displayed_default<a href="#discord.ext.commands.Parameter.displayed_default" title="Permalink to this definition">¶</a></dt>
<dd>

The displayed default in <a href="#discord.ext.commands.Command.signature" title="discord.ext.commands.Command.signature"><code>Command.signature</code></a>.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*property*displayed_name<a href="#discord.ext.commands.Parameter.displayed_name" title="Permalink to this definition">¶</a></dt>
<dd>

The name that is displayed to the user.

New in version 2.3.

<dl><dt>Type</dt>
<dd>

Optional\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl><dl><dt>*await* get_default(*ctx*)<a href="#discord.ext.commands.Parameter.get_default" title="Permalink to this definition">¶</a></dt>
<dd>

This function is a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a>.

Gets this parameter’s default value.

<dl><dt>Parameters</dt>
<dd>

**ctx** (<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>) – The invocation context that is used to get the default argument.

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>discord.ext.commands.parameter(*\**, *converter=...*, *default=...*, *description=...*, *displayed_default=...*, *displayed_name=...*)<a href="#discord.ext.commands.parameter" title="Permalink to this definition">¶</a></dt>
<dd>

A way to assign custom metadata for a <a href="#discord.ext.commands.Command" title="discord.ext.commands.Command"><code>Command</code></a>'s parameter.

New in version 2.0.

Examples

A custom default can be used to have late binding behaviour.

```
@bot.command()
async def wave(ctx, to: discord.User = commands.parameter(default=lambda ctx: ctx.author)):
    await ctx.send(f'Hello {to.mention} :wave:')

```

<dl><dt>Parameters</dt>
<dd>

- **converter** (*Any*) – The converter to use for this parameter, this replaces the annotation at runtime which is transparent to type checkers.
- **default** (*Any*) – The default value for the parameter, if this is a <a href="https://docs.python.org/3/glossary.html#term-callable" title="(in Python v3.14)">callable</a> or a <a href="https://docs.python.org/3/library/asyncio-task.html#coroutine">*coroutine*</a> it is called with a positional <a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a> argument.
- **description** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The description of this parameter.
- **displayed\_default** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) – The displayed default in <a href="#discord.ext.commands.Command.signature" title="discord.ext.commands.Command.signature"><code>Command.signature</code></a>.
- **displayed\_name** (<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>) –

  The name that is displayed to the user.

  New in version 2.3.

</dd></dl></dd>
</dl><dl><dt>discord.ext.commands.param(***, *converter*, *default*, *description*, *displayed_default*, *displayed_name*)<a href="#discord.ext.commands.param" title="Permalink to this definition">¶</a></dt>
<dd>

param(\*, converter=…, default=…, description=…, displayed\_default=…, displayed\_name=…)

An alias for <a href="#discord.ext.commands.parameter" title="discord.ext.commands.parameter"><code>parameter()</code></a>.

New in version 2.0.

</dd></dl><dl><dt>discord.ext.commands.Author<a href="#discord.discord.ext.commands.Author" title="Permalink to this definition">¶</a></dt>
<dd>

A default <a href="#discord.ext.commands.Parameter" title="discord.ext.commands.Parameter"><code>Parameter</code></a> which returns the <a href="#discord.ext.commands.Context.author" title="discord.ext.commands.Context.author"><code>author</code></a> for this context.

New in version 2.0.

</dd></dl><dl><dt>discord.ext.commands.CurrentChannel<a href="#discord.discord.ext.commands.CurrentChannel" title="Permalink to this definition">¶</a></dt>
<dd>

A default <a href="#discord.ext.commands.Parameter" title="discord.ext.commands.Parameter"><code>Parameter</code></a> which returns the <a href="#discord.ext.commands.Context.channel" title="discord.ext.commands.Context.channel"><code>channel</code></a> for this context.

New in version 2.0.

</dd></dl><dl><dt>discord.ext.commands.CurrentGuild<a href="#discord.discord.ext.commands.CurrentGuild" title="Permalink to this definition">¶</a></dt>
<dd>

A default <a href="#discord.ext.commands.Parameter" title="discord.ext.commands.Parameter"><code>Parameter</code></a> which returns the <a href="#discord.ext.commands.Context.guild" title="discord.ext.commands.Context.guild"><code>guild</code></a> for this context. This will never be <code>None</code>. If the command is called in a DM context then <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a> is raised to the error handlers.

New in version 2.0.

</dd></dl>

## Exceptions ¶

<dl><dt>*exception*discord.ext.commands.CommandError(*message=None*, **args*)<a href="#discord.ext.commands.CommandError" title="Permalink to this definition">¶</a></dt>
<dd>

The base exception type for all command related errors.

This inherits from <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.DiscordException" title="discord.DiscordException"><code>discord.DiscordException</code></a>.

This exception and exceptions inherited from it are handled in a special way as they are caught and passed into a special event from <a href="#discord.ext.commands.Bot" title="discord.ext.commands.Bot"><code>Bot</code></a>, <a href="#discord.discord.ext.commands.on_command_error" title="discord.discord.ext.commands.on_command_error"><code>on_command_error()</code></a>.

</dd></dl><dl><dt>*exception*discord.ext.commands.ConversionError(*converter*, *original*)<a href="#discord.ext.commands.ConversionError" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when a Converter class raises non-CommandError.

This inherits from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>converter<a href="#discord.ext.commands.ConversionError.converter" title="Permalink to this definition">¶</a></dt>
<dd>

The converter that failed.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.Converter" title="discord.ext.commands.Converter"><code>discord.ext.commands.Converter</code></a>

</dd></dl></dd>
</dl><dl><dt>original<a href="#discord.ext.commands.ConversionError.original" title="Permalink to this definition">¶</a></dt>
<dd>

The original exception that was raised. You can also get this via the <code>__cause__</code> attribute.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.MissingRequiredArgument(*param*)<a href="#discord.ext.commands.MissingRequiredArgument" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when parsing a command and a parameter that is required is not encountered.

This inherits from <a href="#discord.ext.commands.UserInputError" title="discord.ext.commands.UserInputError"><code>UserInputError</code></a>

<dl><dt>param<a href="#discord.ext.commands.MissingRequiredArgument.param" title="Permalink to this definition">¶</a></dt>
<dd>

The argument that is missing.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.Parameter" title="discord.ext.commands.Parameter"><code>Parameter</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.MissingRequiredAttachment(*param*)<a href="#discord.ext.commands.MissingRequiredAttachment" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when parsing a command and a parameter that requires an attachment is not given.

This inherits from <a href="#discord.ext.commands.UserInputError" title="discord.ext.commands.UserInputError"><code>UserInputError</code></a>

New in version 2.0.

<dl><dt>param<a href="#discord.ext.commands.MissingRequiredAttachment.param" title="Permalink to this definition">¶</a></dt>
<dd>

The argument that is missing an attachment.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.Parameter" title="discord.ext.commands.Parameter"><code>Parameter</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.ArgumentParsingError(*message=None*, **args*)<a href="#discord.ext.commands.ArgumentParsingError" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when the parser fails to parse a user’s input.

This inherits from <a href="#discord.ext.commands.UserInputError" title="discord.ext.commands.UserInputError"><code>UserInputError</code></a>.

There are child classes that implement more granular parsing errors for i18n purposes.

</dd></dl><dl><dt>*exception*discord.ext.commands.UnexpectedQuoteError(*quote*)<a href="#discord.ext.commands.UnexpectedQuoteError" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when the parser encounters a quote mark inside a non-quoted string.

This inherits from <a href="#discord.ext.commands.ArgumentParsingError" title="discord.ext.commands.ArgumentParsingError"><code>ArgumentParsingError</code></a>.

<dl><dt>quote<a href="#discord.ext.commands.UnexpectedQuoteError.quote" title="Permalink to this definition">¶</a></dt>
<dd>

The quote mark that was found inside the non-quoted string.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.InvalidEndOfQuotedStringError(*char*)<a href="#discord.ext.commands.InvalidEndOfQuotedStringError" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when a space is expected after the closing quote in a string but a different character is found.

This inherits from <a href="#discord.ext.commands.ArgumentParsingError" title="discord.ext.commands.ArgumentParsingError"><code>ArgumentParsingError</code></a>.

<dl><dt>char<a href="#discord.ext.commands.InvalidEndOfQuotedStringError.char" title="Permalink to this definition">¶</a></dt>
<dd>

The character found instead of the expected string.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.ExpectedClosingQuoteError(*close_quote*)<a href="#discord.ext.commands.ExpectedClosingQuoteError" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when a quote character is expected but not found.

This inherits from <a href="#discord.ext.commands.ArgumentParsingError" title="discord.ext.commands.ArgumentParsingError"><code>ArgumentParsingError</code></a>.

<dl><dt>close_quote<a href="#discord.ext.commands.ExpectedClosingQuoteError.close_quote" title="Permalink to this definition">¶</a></dt>
<dd>

The quote character expected.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.BadArgument(*message=None*, **args*)<a href="#discord.ext.commands.BadArgument" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when a parsing or conversion failure is encountered on an argument to pass into a command.

This inherits from <a href="#discord.ext.commands.UserInputError" title="discord.ext.commands.UserInputError"><code>UserInputError</code></a>

</dd></dl><dl><dt>*exception*discord.ext.commands.BadUnionArgument(*param*, *converters*, *errors*)<a href="#discord.ext.commands.BadUnionArgument" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when a <a href="https://docs.python.org/3/library/typing.html#typing.Union" title="(in Python v3.14)"><code>typing.Union</code></a> converter fails for all its associated types.

This inherits from <a href="#discord.ext.commands.UserInputError" title="discord.ext.commands.UserInputError"><code>UserInputError</code></a>

<dl><dt>param<a href="#discord.ext.commands.BadUnionArgument.param" title="Permalink to this definition">¶</a></dt>
<dd>

The parameter that failed being converted.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/inspect.html#inspect.Parameter" title="(in Python v3.14)"><code>inspect.Parameter</code></a>

</dd></dl></dd>
</dl><dl><dt>converters<a href="#discord.ext.commands.BadUnionArgument.converters" title="Permalink to this definition">¶</a></dt>
<dd>

A tuple of converters attempted in conversion, in order of failure.

<dl><dt>Type</dt>
<dd>

Tuple\[Type, <code>...</code>]

</dd></dl></dd>
</dl><dl><dt>errors<a href="#discord.ext.commands.BadUnionArgument.errors" title="Permalink to this definition">¶</a></dt>
<dd>

A list of errors that were caught from failing the conversion.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.BadLiteralArgument(*param*, *literals*, *errors*, *argument=''*)<a href="#discord.ext.commands.BadLiteralArgument" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when a <a href="https://docs.python.org/3/library/typing.html#typing.Literal" title="(in Python v3.14)"><code>typing.Literal</code></a> converter fails for all its associated values.

This inherits from <a href="#discord.ext.commands.UserInputError" title="discord.ext.commands.UserInputError"><code>UserInputError</code></a>

New in version 2.0.

<dl><dt>param<a href="#discord.ext.commands.BadLiteralArgument.param" title="Permalink to this definition">¶</a></dt>
<dd>

The parameter that failed being converted.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/inspect.html#inspect.Parameter" title="(in Python v3.14)"><code>inspect.Parameter</code></a>

</dd></dl></dd>
</dl><dl><dt>literals<a href="#discord.ext.commands.BadLiteralArgument.literals" title="Permalink to this definition">¶</a></dt>
<dd>

A tuple of values compared against in conversion, in order of failure.

<dl><dt>Type</dt>
<dd>

Tuple\[Any, <code>...</code>]

</dd></dl></dd>
</dl><dl><dt>errors<a href="#discord.ext.commands.BadLiteralArgument.errors" title="Permalink to this definition">¶</a></dt>
<dd>

A list of errors that were caught from failing the conversion.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>]

</dd></dl></dd>
</dl><dl><dt>argument<a href="#discord.ext.commands.BadLiteralArgument.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The argument’s value that failed to be converted. Defaults to an empty string.

New in version 2.3.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.PrivateMessageOnly(*message=None*)<a href="#discord.ext.commands.PrivateMessageOnly" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when an operation does not work outside of private message contexts.

This inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

</dd></dl><dl><dt>*exception*discord.ext.commands.NoPrivateMessage(*message=None*)<a href="#discord.ext.commands.NoPrivateMessage" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when an operation does not work in private message contexts.

This inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

</dd></dl><dl><dt>*exception*discord.ext.commands.CheckFailure(*message=None*, **args*)<a href="#discord.ext.commands.CheckFailure" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the predicates in <a href="#discord.ext.commands.Command.checks" title="discord.ext.commands.Command.checks"><code>Command.checks</code></a> have failed.

This inherits from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>

</dd></dl><dl><dt>*exception*discord.ext.commands.CheckAnyFailure(*checks*, *errors*)<a href="#discord.ext.commands.CheckAnyFailure" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when all predicates in <a href="#discord.ext.commands.check_any" title="discord.ext.commands.check_any"><code>check_any()</code></a> fail.

This inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 1.3.

<dl><dt>errors<a href="#discord.ext.commands.CheckAnyFailure.errors" title="Permalink to this definition">¶</a></dt>
<dd>

A list of errors that were caught during execution.

<dl><dt>Type</dt>
<dd>

List\[<a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>]

</dd></dl></dd>
</dl><dl><dt>checks<a href="#discord.ext.commands.CheckAnyFailure.checks" title="Permalink to this definition">¶</a></dt>
<dd>

A list of check predicates that failed.

<dl><dt>Type</dt>
<dd>

List\[Callable\[\[<a href="#discord.ext.commands.Context" title="discord.ext.commands.Context"><code>Context</code></a>], <a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.CommandNotFound(*message=None*, **args*)<a href="#discord.ext.commands.CommandNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when a command is attempted to be invoked but no command under that name is found.

This is not raised for invalid subcommands, rather just the initial main command that is attempted to be invoked.

This inherits from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

</dd></dl><dl><dt>*exception*discord.ext.commands.DisabledCommand(*message=None*, **args*)<a href="#discord.ext.commands.DisabledCommand" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the command being invoked is disabled.

This inherits from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>

</dd></dl><dl><dt>*exception*discord.ext.commands.CommandInvokeError(*e*)<a href="#discord.ext.commands.CommandInvokeError" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the command being invoked raised an exception.

This inherits from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>

<dl><dt>original<a href="#discord.ext.commands.CommandInvokeError.original" title="Permalink to this definition">¶</a></dt>
<dd>

The original exception that was raised. You can also get this via the <code>__cause__</code> attribute.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.TooManyArguments(*message=None*, **args*)<a href="#discord.ext.commands.TooManyArguments" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the command was passed too many arguments and its <a href="#discord.ext.commands.Command.ignore_extra" title="discord.ext.commands.Command.ignore_extra"><code>Command.ignore_extra</code></a> attribute was not set to <code>True</code>.

This inherits from <a href="#discord.ext.commands.UserInputError" title="discord.ext.commands.UserInputError"><code>UserInputError</code></a>

</dd></dl><dl><dt>*exception*discord.ext.commands.UserInputError(*message=None*, **args*)<a href="#discord.ext.commands.UserInputError" title="Permalink to this definition">¶</a></dt>
<dd>

The base exception type for errors that involve errors regarding user input.

This inherits from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

</dd></dl><dl><dt>*exception*discord.ext.commands.CommandOnCooldown(*cooldown*, *retry_after*, *type*)<a href="#discord.ext.commands.CommandOnCooldown" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the command being invoked is on cooldown.

This inherits from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>

<dl><dt>cooldown<a href="#discord.ext.commands.CommandOnCooldown.cooldown" title="Permalink to this definition">¶</a></dt>
<dd>

A class with attributes <code>rate</code> and <code>per</code> similar to the <a href="#discord.ext.commands.cooldown" title="discord.ext.commands.cooldown"><code>cooldown()</code></a> decorator.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.Cooldown" title="discord.app_commands.Cooldown"><code>Cooldown</code></a>

</dd></dl></dd>
</dl><dl><dt>type<a href="#discord.ext.commands.CommandOnCooldown.type" title="Permalink to this definition">¶</a></dt>
<dd>

The type associated with the cooldown.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.BucketType" title="discord.ext.commands.BucketType"><code>BucketType</code></a>

</dd></dl></dd>
</dl><dl><dt>retry_after<a href="#discord.ext.commands.CommandOnCooldown.retry_after" title="Permalink to this definition">¶</a></dt>
<dd>

The amount of seconds to wait before you can retry again.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.MaxConcurrencyReached(*number*, *per*)<a href="#discord.ext.commands.MaxConcurrencyReached" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the command being invoked has reached its maximum concurrency.

This inherits from <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a>.

<dl><dt>number<a href="#discord.ext.commands.MaxConcurrencyReached.number" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum number of concurrent invokers allowed.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>

</dd></dl></dd>
</dl><dl><dt>per<a href="#discord.ext.commands.MaxConcurrencyReached.per" title="Permalink to this definition">¶</a></dt>
<dd>

The bucket type passed to the <a href="#discord.ext.commands.max_concurrency" title="discord.ext.commands.max_concurrency"><code>max_concurrency()</code></a> decorator.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.BucketType" title="discord.ext.commands.BucketType"><code>BucketType</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.NotOwner(*message=None*, **args*)<a href="#discord.ext.commands.NotOwner" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the message author is not the owner of the bot.

This inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

</dd></dl><dl><dt>*exception*discord.ext.commands.MessageNotFound(*argument*)<a href="#discord.ext.commands.MessageNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the message provided was not found in the channel.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.5.

<dl><dt>argument<a href="#discord.ext.commands.MessageNotFound.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The message supplied by the caller that was not found

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.MemberNotFound(*argument*)<a href="#discord.ext.commands.MemberNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the member provided was not found in the bot’s cache.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.5.

<dl><dt>argument<a href="#discord.ext.commands.MemberNotFound.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The member supplied by the caller that was not found

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.GuildNotFound(*argument*)<a href="#discord.ext.commands.GuildNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the guild provided was not found in the bot’s cache.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.7.

<dl><dt>argument<a href="#discord.ext.commands.GuildNotFound.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The guild supplied by the called that was not found

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.UserNotFound(*argument*)<a href="#discord.ext.commands.UserNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the user provided was not found in the bot’s cache.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.5.

<dl><dt>argument<a href="#discord.ext.commands.UserNotFound.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The user supplied by the caller that was not found

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.ChannelNotFound(*argument*)<a href="#discord.ext.commands.ChannelNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the bot can not find the channel.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.5.

<dl><dt>argument<a href="#discord.ext.commands.ChannelNotFound.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The channel supplied by the caller that was not found

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.ChannelNotReadable(*argument*)<a href="#discord.ext.commands.ChannelNotReadable" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the bot does not have permission to read messages in the channel.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.5.

<dl><dt>argument<a href="#discord.ext.commands.ChannelNotReadable.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The channel supplied by the caller that was not readable

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.ThreadNotFound(*argument*)<a href="#discord.ext.commands.ThreadNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the bot can not find the thread.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 2.0.

<dl><dt>argument<a href="#discord.ext.commands.ThreadNotFound.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The thread supplied by the caller that was not found

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.BadColourArgument(*argument*)<a href="#discord.ext.commands.BadColourArgument" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the colour is not valid.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.5.

<dl><dt>argument<a href="#discord.ext.commands.BadColourArgument.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The colour supplied by the caller that was not valid

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.RoleNotFound(*argument*)<a href="#discord.ext.commands.RoleNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the bot can not find the role.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.5.

<dl><dt>argument<a href="#discord.ext.commands.RoleNotFound.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The role supplied by the caller that was not found

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.BadInviteArgument(*argument*)<a href="#discord.ext.commands.BadInviteArgument" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the invite is invalid or expired.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.5.

<dl><dt>argument<a href="#discord.ext.commands.BadInviteArgument.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The invite supplied by the caller that was not valid

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.EmojiNotFound(*argument*)<a href="#discord.ext.commands.EmojiNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the bot can not find the emoji.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.5.

<dl><dt>argument<a href="#discord.ext.commands.EmojiNotFound.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The emoji supplied by the caller that was not found

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.PartialEmojiConversionFailure(*argument*)<a href="#discord.ext.commands.PartialEmojiConversionFailure" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the emoji provided does not match the correct format.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.5.

<dl><dt>argument<a href="#discord.ext.commands.PartialEmojiConversionFailure.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The emoji supplied by the caller that did not match the regex

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.GuildStickerNotFound(*argument*)<a href="#discord.ext.commands.GuildStickerNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the bot can not find the sticker.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 2.0.

<dl><dt>argument<a href="#discord.ext.commands.GuildStickerNotFound.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The sticker supplied by the caller that was not found

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.ScheduledEventNotFound(*argument*)<a href="#discord.ext.commands.ScheduledEventNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the bot can not find the scheduled event.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 2.0.

<dl><dt>argument<a href="#discord.ext.commands.ScheduledEventNotFound.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The event supplied by the caller that was not found

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.SoundboardSoundNotFound(*argument*)<a href="#discord.ext.commands.SoundboardSoundNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the bot can not find the soundboard sound.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 2.5.

<dl><dt>argument<a href="#discord.ext.commands.SoundboardSoundNotFound.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The sound supplied by the caller that was not found

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.BadBoolArgument(*argument*)<a href="#discord.ext.commands.BadBoolArgument" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when a boolean argument was not convertable.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 1.5.

<dl><dt>argument<a href="#discord.ext.commands.BadBoolArgument.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The boolean argument supplied by the caller that is not in the predefined list

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.RangeError(*value*, *minimum*, *maximum*)<a href="#discord.ext.commands.RangeError" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when an argument is out of range.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>

New in version 2.0.

<dl><dt>minimum<a href="#discord.ext.commands.RangeError.minimum" title="Permalink to this definition">¶</a></dt>
<dd>

The minimum value expected or <code>None</code> if there wasn’t one

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]]

</dd></dl></dd>
</dl><dl><dt>maximum<a href="#discord.ext.commands.RangeError.maximum" title="Permalink to this definition">¶</a></dt>
<dd>

The maximum value expected or <code>None</code> if there wasn’t one

<dl><dt>Type</dt>
<dd>

Optional\[Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>]]

</dd></dl></dd>
</dl><dl><dt>value<a href="#discord.ext.commands.RangeError.value" title="Permalink to this definition">¶</a></dt>
<dd>

The value that was out of range.

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>, <a href="https://docs.python.org/3/library/functions.html#float" title="(in Python v3.14)"><code>float</code></a>, <a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.MissingPermissions(*missing_permissions*, **args*)<a href="#discord.ext.commands.MissingPermissions" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the command invoker lacks permissions to run a command.

This inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

<dl><dt>missing_permissions<a href="#discord.ext.commands.MissingPermissions.missing_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The required permissions that are missing.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.BotMissingPermissions(*missing_permissions*, **args*)<a href="#discord.ext.commands.BotMissingPermissions" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the bot’s member lacks permissions to run a command.

This inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

<dl><dt>missing_permissions<a href="#discord.ext.commands.BotMissingPermissions.missing_permissions" title="Permalink to this definition">¶</a></dt>
<dd>

The required permissions that are missing.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.MissingRole(*missing_role*)<a href="#discord.ext.commands.MissingRole" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the command invoker lacks a role to run a command.

This inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

New in version 1.1.

<dl><dt>missing_role<a href="#discord.ext.commands.MissingRole.missing_role" title="Permalink to this definition">¶</a></dt>
<dd>

The required role that is missing. This is the parameter passed to <a href="#discord.ext.commands.has_role" title="discord.ext.commands.has_role"><code>has_role()</code></a>.

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.BotMissingRole(*missing_role*)<a href="#discord.ext.commands.BotMissingRole" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the bot’s member lacks a role to run a command.

This inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

New in version 1.1.

<dl><dt>missing_role<a href="#discord.ext.commands.BotMissingRole.missing_role" title="Permalink to this definition">¶</a></dt>
<dd>

The required role that is missing. This is the parameter passed to <a href="#discord.ext.commands.has_role" title="discord.ext.commands.has_role"><code>has_role()</code></a>.

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.MissingAnyRole(*missing_roles*)<a href="#discord.ext.commands.MissingAnyRole" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the command invoker lacks any of the roles specified to run a command.

This inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

New in version 1.1.

<dl><dt>missing_roles<a href="#discord.ext.commands.MissingAnyRole.missing_roles" title="Permalink to this definition">¶</a></dt>
<dd>

The roles that the invoker is missing. These are the parameters passed to <a href="#discord.ext.commands.has_any_role" title="discord.ext.commands.has_any_role"><code>has_any_role()</code></a>.

<dl><dt>Type</dt>
<dd>

List\[Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.BotMissingAnyRole(*missing_roles*)<a href="#discord.ext.commands.BotMissingAnyRole" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when the bot’s member lacks any of the roles specified to run a command.

This inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>

New in version 1.1.

<dl><dt>missing_roles<a href="#discord.ext.commands.BotMissingAnyRole.missing_roles" title="Permalink to this definition">¶</a></dt>
<dd>

The roles that the bot’s member is missing. These are the parameters passed to <a href="#discord.ext.commands.has_any_role" title="discord.ext.commands.has_any_role"><code>has_any_role()</code></a>.

<dl><dt>Type</dt>
<dd>

List\[Union\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>, <a href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.14)"><code>int</code></a>]]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.NSFWChannelRequired(*channel*)<a href="#discord.ext.commands.NSFWChannelRequired" title="Permalink to this definition">¶</a></dt>
<dd>

Exception raised when a channel does not have the required NSFW setting.

This inherits from <a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a>.

New in version 1.1.

<dl><dt>channel<a href="#discord.ext.commands.NSFWChannelRequired.channel" title="Permalink to this definition">¶</a></dt>
<dd>

The channel that does not have NSFW enabled.

<dl><dt>Type</dt>
<dd>

Union\[<a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.abc.GuildChannel" title="discord.abc.GuildChannel"><code>abc.GuildChannel</code></a>, <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.Thread" title="discord.Thread"><code>Thread</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.FlagError(*message=None*, **args*)<a href="#discord.ext.commands.FlagError" title="Permalink to this definition">¶</a></dt>
<dd>

The base exception type for all flag parsing related errors.

This inherits from <a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a>.

New in version 2.0.

</dd></dl><dl><dt>*exception*discord.ext.commands.BadFlagArgument(*flag*, *argument*, *original*)<a href="#discord.ext.commands.BadFlagArgument" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when a flag failed to convert a value.

This inherits from <a href="#discord.ext.commands.FlagError" title="discord.ext.commands.FlagError"><code>FlagError</code></a>

New in version 2.0.

<dl><dt>flag<a href="#discord.ext.commands.BadFlagArgument.flag" title="Permalink to this definition">¶</a></dt>
<dd>

The flag that failed to convert.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.Flag" title="discord.ext.commands.Flag"><code>Flag</code></a>

</dd></dl></dd>
</dl><dl><dt>argument<a href="#discord.ext.commands.BadFlagArgument.argument" title="Permalink to this definition">¶</a></dt>
<dd>

The argument supplied by the caller that was not able to be converted.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>original<a href="#discord.ext.commands.BadFlagArgument.original" title="Permalink to this definition">¶</a></dt>
<dd>

The original exception that was raised. You can also get this via the <code>__cause__</code> attribute.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.MissingFlagArgument(*flag*)<a href="#discord.ext.commands.MissingFlagArgument" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when a flag did not get a value.

This inherits from <a href="#discord.ext.commands.FlagError" title="discord.ext.commands.FlagError"><code>FlagError</code></a>

New in version 2.0.

<dl><dt>flag<a href="#discord.ext.commands.MissingFlagArgument.flag" title="Permalink to this definition">¶</a></dt>
<dd>

The flag that did not get a value.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.Flag" title="discord.ext.commands.Flag"><code>Flag</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.TooManyFlags(*flag*, *values*)<a href="#discord.ext.commands.TooManyFlags" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when a flag has received too many values.

This inherits from <a href="#discord.ext.commands.FlagError" title="discord.ext.commands.FlagError"><code>FlagError</code></a>.

New in version 2.0.

<dl><dt>flag<a href="#discord.ext.commands.TooManyFlags.flag" title="Permalink to this definition">¶</a></dt>
<dd>

The flag that received too many values.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.Flag" title="discord.ext.commands.Flag"><code>Flag</code></a>

</dd></dl></dd>
</dl><dl><dt>values<a href="#discord.ext.commands.TooManyFlags.values" title="Permalink to this definition">¶</a></dt>
<dd>

The values that were passed.

<dl><dt>Type</dt>
<dd>

List\[<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>]

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.MissingRequiredFlag(*flag*)<a href="#discord.ext.commands.MissingRequiredFlag" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when a required flag was not given.

This inherits from <a href="#discord.ext.commands.FlagError" title="discord.ext.commands.FlagError"><code>FlagError</code></a>

New in version 2.0.

<dl><dt>flag<a href="#discord.ext.commands.MissingRequiredFlag.flag" title="Permalink to this definition">¶</a></dt>
<dd>

The required flag that was not found.

<dl><dt>Type</dt>
<dd>

<a href="#discord.ext.commands.Flag" title="discord.ext.commands.Flag"><code>Flag</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.ExtensionError(*message=None*, **args*, *name*)<a href="#discord.ext.commands.ExtensionError" title="Permalink to this definition">¶</a></dt>
<dd>

Base exception for extension related errors.

This inherits from <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.DiscordException" title="discord.DiscordException"><code>DiscordException</code></a>.

<dl><dt>name<a href="#discord.ext.commands.ExtensionError.name" title="Permalink to this definition">¶</a></dt>
<dd>

The extension that had an error.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.ExtensionAlreadyLoaded(*name*)<a href="#discord.ext.commands.ExtensionAlreadyLoaded" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when an extension has already been loaded.

This inherits from <a href="#discord.ext.commands.ExtensionError" title="discord.ext.commands.ExtensionError"><code>ExtensionError</code></a>

</dd></dl><dl><dt>*exception*discord.ext.commands.ExtensionNotLoaded(*name*)<a href="#discord.ext.commands.ExtensionNotLoaded" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when an extension was not loaded.

This inherits from <a href="#discord.ext.commands.ExtensionError" title="discord.ext.commands.ExtensionError"><code>ExtensionError</code></a>

</dd></dl><dl><dt>*exception*discord.ext.commands.NoEntryPointError(*name*)<a href="#discord.ext.commands.NoEntryPointError" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when an extension does not have a <code>setup</code> entry point function.

This inherits from <a href="#discord.ext.commands.ExtensionError" title="discord.ext.commands.ExtensionError"><code>ExtensionError</code></a>

</dd></dl><dl><dt>*exception*discord.ext.commands.ExtensionFailed(*name*, *original*)<a href="#discord.ext.commands.ExtensionFailed" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when an extension failed to load during execution of the module or <code>setup</code> entry point.

This inherits from <a href="#discord.ext.commands.ExtensionError" title="discord.ext.commands.ExtensionError"><code>ExtensionError</code></a>

<dl><dt>name<a href="#discord.ext.commands.ExtensionFailed.name" title="Permalink to this definition">¶</a></dt>
<dd>

The extension that had the error.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>original<a href="#discord.ext.commands.ExtensionFailed.original" title="Permalink to this definition">¶</a></dt>
<dd>

The original exception that was raised. You can also get this via the <code>__cause__</code> attribute.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/exceptions.html#Exception" title="(in Python v3.14)"><code>Exception</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.ExtensionNotFound(*name*)<a href="#discord.ext.commands.ExtensionNotFound" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when an extension is not found.

This inherits from <a href="#discord.ext.commands.ExtensionError" title="discord.ext.commands.ExtensionError"><code>ExtensionError</code></a>

Changed in version 1.3: Made the <code>original</code> attribute always None.

<dl><dt>name<a href="#discord.ext.commands.ExtensionNotFound.name" title="Permalink to this definition">¶</a></dt>
<dd>

The extension that had the error.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.CommandRegistrationError(*name*, ***, *alias_conflict=False*)<a href="#discord.ext.commands.CommandRegistrationError" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when the command can’t be added because the name is already taken by a different command.

This inherits from <a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientException" title="discord.ClientException"><code>discord.ClientException</code></a>

New in version 1.4.

<dl><dt>name<a href="#discord.ext.commands.CommandRegistrationError.name" title="Permalink to this definition">¶</a></dt>
<dd>

The command name that had the error.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/stdtypes.html#str" title="(in Python v3.14)"><code>str</code></a>

</dd></dl></dd>
</dl><dl><dt>alias_conflict<a href="#discord.ext.commands.CommandRegistrationError.alias_conflict" title="Permalink to this definition">¶</a></dt>
<dd>

Whether the name that conflicts is an alias of the command we try to add.

<dl><dt>Type</dt>
<dd>

<a href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.14)"><code>bool</code></a>

</dd></dl></dd>
</dl></dd>
</dl><dl><dt>*exception*discord.ext.commands.HybridCommandError(*original*)<a href="#discord.ext.commands.HybridCommandError" title="Permalink to this definition">¶</a></dt>
<dd>

An exception raised when a <a href="#discord.ext.commands.HybridCommand" title="discord.ext.commands.HybridCommand"><code>HybridCommand</code></a> raises an <a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a> derived exception that could not be sufficiently converted to an equivalent <a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a> exception.

New in version 2.0.

<dl><dt>original<a href="#discord.ext.commands.HybridCommandError.original" title="Permalink to this definition">¶</a></dt>
<dd>

The original exception that was raised. You can also get this via the <code>__cause__</code> attribute.

<dl><dt>Type</dt>
<dd>

<a href="https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.app_commands.AppCommandError" title="discord.app_commands.AppCommandError"><code>AppCommandError</code></a>

</dd></dl></dd>
</dl></dd>
</dl>

### Exception Hierarchy ¶

- <dl><dt><a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.DiscordException" title="discord.DiscordException"><code>DiscordException</code></a></dt><dd>
  - <dl><dt><a href="#discord.ext.commands.CommandError" title="discord.ext.commands.CommandError"><code>CommandError</code></a></dt><dd>
    - <a href="#discord.ext.commands.ConversionError" title="discord.ext.commands.ConversionError"><code>ConversionError</code></a>
    - <dl><dt><a href="#discord.ext.commands.UserInputError" title="discord.ext.commands.UserInputError"><code>UserInputError</code></a></dt><dd>
      - <a href="#discord.ext.commands.MissingRequiredArgument" title="discord.ext.commands.MissingRequiredArgument"><code>MissingRequiredArgument</code></a>
      - <a href="#discord.ext.commands.MissingRequiredAttachment" title="discord.ext.commands.MissingRequiredAttachment"><code>MissingRequiredAttachment</code></a>
      - <a href="#discord.ext.commands.TooManyArguments" title="discord.ext.commands.TooManyArguments"><code>TooManyArguments</code></a>
      - <dl><dt><a href="#discord.ext.commands.BadArgument" title="discord.ext.commands.BadArgument"><code>BadArgument</code></a></dt><dd>
        - <a href="#discord.ext.commands.MessageNotFound" title="discord.ext.commands.MessageNotFound"><code>MessageNotFound</code></a>
        - <a href="#discord.ext.commands.MemberNotFound" title="discord.ext.commands.MemberNotFound"><code>MemberNotFound</code></a>
        - <a href="#discord.ext.commands.GuildNotFound" title="discord.ext.commands.GuildNotFound"><code>GuildNotFound</code></a>
        - <a href="#discord.ext.commands.UserNotFound" title="discord.ext.commands.UserNotFound"><code>UserNotFound</code></a>
        - <a href="#discord.ext.commands.ChannelNotFound" title="discord.ext.commands.ChannelNotFound"><code>ChannelNotFound</code></a>
        - <a href="#discord.ext.commands.ChannelNotReadable" title="discord.ext.commands.ChannelNotReadable"><code>ChannelNotReadable</code></a>
        - <a href="#discord.ext.commands.BadColourArgument" title="discord.ext.commands.BadColourArgument"><code>BadColourArgument</code></a>
        - <a href="#discord.ext.commands.RoleNotFound" title="discord.ext.commands.RoleNotFound"><code>RoleNotFound</code></a>
        - <a href="#discord.ext.commands.BadInviteArgument" title="discord.ext.commands.BadInviteArgument"><code>BadInviteArgument</code></a>
        - <a href="#discord.ext.commands.EmojiNotFound" title="discord.ext.commands.EmojiNotFound"><code>EmojiNotFound</code></a>
        - <a href="#discord.ext.commands.GuildStickerNotFound" title="discord.ext.commands.GuildStickerNotFound"><code>GuildStickerNotFound</code></a>
        - <a href="#discord.ext.commands.ScheduledEventNotFound" title="discord.ext.commands.ScheduledEventNotFound"><code>ScheduledEventNotFound</code></a>
        - <a href="#discord.ext.commands.SoundboardSoundNotFound" title="discord.ext.commands.SoundboardSoundNotFound"><code>SoundboardSoundNotFound</code></a>
        - <a href="#discord.ext.commands.PartialEmojiConversionFailure" title="discord.ext.commands.PartialEmojiConversionFailure"><code>PartialEmojiConversionFailure</code></a>
        - <a href="#discord.ext.commands.BadBoolArgument" title="discord.ext.commands.BadBoolArgument"><code>BadBoolArgument</code></a>
        - <a href="#discord.ext.commands.RangeError" title="discord.ext.commands.RangeError"><code>RangeError</code></a>
        - <a href="#discord.ext.commands.ThreadNotFound" title="discord.ext.commands.ThreadNotFound"><code>ThreadNotFound</code></a>
        - <dl><dt><a href="#discord.ext.commands.FlagError" title="discord.ext.commands.FlagError"><code>FlagError</code></a></dt><dd>
          - <a href="#discord.ext.commands.BadFlagArgument" title="discord.ext.commands.BadFlagArgument"><code>BadFlagArgument</code></a>
          - <a href="#discord.ext.commands.MissingFlagArgument" title="discord.ext.commands.MissingFlagArgument"><code>MissingFlagArgument</code></a>
          - <a href="#discord.ext.commands.TooManyFlags" title="discord.ext.commands.TooManyFlags"><code>TooManyFlags</code></a>
          - <a href="#discord.ext.commands.MissingRequiredFlag" title="discord.ext.commands.MissingRequiredFlag"><code>MissingRequiredFlag</code></a></dd></dl></dd></dl>
      - <a href="#discord.ext.commands.BadUnionArgument" title="discord.ext.commands.BadUnionArgument"><code>BadUnionArgument</code></a>
      - <a href="#discord.ext.commands.BadLiteralArgument" title="discord.ext.commands.BadLiteralArgument"><code>BadLiteralArgument</code></a>
      - <dl><dt><a href="#discord.ext.commands.ArgumentParsingError" title="discord.ext.commands.ArgumentParsingError"><code>ArgumentParsingError</code></a></dt><dd>
        - <a href="#discord.ext.commands.UnexpectedQuoteError" title="discord.ext.commands.UnexpectedQuoteError"><code>UnexpectedQuoteError</code></a>
        - <a href="#discord.ext.commands.InvalidEndOfQuotedStringError" title="discord.ext.commands.InvalidEndOfQuotedStringError"><code>InvalidEndOfQuotedStringError</code></a>
        - <a href="#discord.ext.commands.ExpectedClosingQuoteError" title="discord.ext.commands.ExpectedClosingQuoteError"><code>ExpectedClosingQuoteError</code></a></dd></dl></dd></dl>
    - <a href="#discord.ext.commands.CommandNotFound" title="discord.ext.commands.CommandNotFound"><code>CommandNotFound</code></a>
    - <dl><dt><a href="#discord.ext.commands.CheckFailure" title="discord.ext.commands.CheckFailure"><code>CheckFailure</code></a></dt><dd>
      - <a href="#discord.ext.commands.CheckAnyFailure" title="discord.ext.commands.CheckAnyFailure"><code>CheckAnyFailure</code></a>
      - <a href="#discord.ext.commands.PrivateMessageOnly" title="discord.ext.commands.PrivateMessageOnly"><code>PrivateMessageOnly</code></a>
      - <a href="#discord.ext.commands.NoPrivateMessage" title="discord.ext.commands.NoPrivateMessage"><code>NoPrivateMessage</code></a>
      - <a href="#discord.ext.commands.NotOwner" title="discord.ext.commands.NotOwner"><code>NotOwner</code></a>
      - <a href="#discord.ext.commands.MissingPermissions" title="discord.ext.commands.MissingPermissions"><code>MissingPermissions</code></a>
      - <a href="#discord.ext.commands.BotMissingPermissions" title="discord.ext.commands.BotMissingPermissions"><code>BotMissingPermissions</code></a>
      - <a href="#discord.ext.commands.MissingRole" title="discord.ext.commands.MissingRole"><code>MissingRole</code></a>
      - <a href="#discord.ext.commands.BotMissingRole" title="discord.ext.commands.BotMissingRole"><code>BotMissingRole</code></a>
      - <a href="#discord.ext.commands.MissingAnyRole" title="discord.ext.commands.MissingAnyRole"><code>MissingAnyRole</code></a>
      - <a href="#discord.ext.commands.BotMissingAnyRole" title="discord.ext.commands.BotMissingAnyRole"><code>BotMissingAnyRole</code></a>
      - <a href="#discord.ext.commands.NSFWChannelRequired" title="discord.ext.commands.NSFWChannelRequired"><code>NSFWChannelRequired</code></a></dd></dl>
    - <a href="#discord.ext.commands.DisabledCommand" title="discord.ext.commands.DisabledCommand"><code>DisabledCommand</code></a>
    - <a href="#discord.ext.commands.CommandInvokeError" title="discord.ext.commands.CommandInvokeError"><code>CommandInvokeError</code></a>
    - <a href="#discord.ext.commands.CommandOnCooldown" title="discord.ext.commands.CommandOnCooldown"><code>CommandOnCooldown</code></a>
    - <a href="#discord.ext.commands.MaxConcurrencyReached" title="discord.ext.commands.MaxConcurrencyReached"><code>MaxConcurrencyReached</code></a>
    - <a href="#discord.ext.commands.HybridCommandError" title="discord.ext.commands.HybridCommandError"><code>HybridCommandError</code></a></dd></dl>
  - <dl><dt><a href="#discord.ext.commands.ExtensionError" title="discord.ext.commands.ExtensionError"><code>ExtensionError</code></a></dt><dd>
    - <a href="#discord.ext.commands.ExtensionAlreadyLoaded" title="discord.ext.commands.ExtensionAlreadyLoaded"><code>ExtensionAlreadyLoaded</code></a>
    - <a href="#discord.ext.commands.ExtensionNotLoaded" title="discord.ext.commands.ExtensionNotLoaded"><code>ExtensionNotLoaded</code></a>
    - <a href="#discord.ext.commands.NoEntryPointError" title="discord.ext.commands.NoEntryPointError"><code>NoEntryPointError</code></a>
    - <a href="#discord.ext.commands.ExtensionFailed" title="discord.ext.commands.ExtensionFailed"><code>ExtensionFailed</code></a>
    - <a href="#discord.ext.commands.ExtensionNotFound" title="discord.ext.commands.ExtensionNotFound"><code>ExtensionNotFound</code></a></dd></dl></dd></dl>
- <dl><dt><a href="https://discordpy.readthedocs.io/en/stable/api.html#discord.ClientException" title="discord.ClientException"><code>ClientException</code></a></dt><dd>
  - <a href="#discord.ext.commands.CommandRegistrationError" title="discord.ext.commands.CommandRegistrationError"><code>CommandRegistrationError</code></a></dd></dl>

close

# Settings

## Font

### Use a serif font:

## Theme

### Automatic

### Light

### Dark

arrow\_upwardto top