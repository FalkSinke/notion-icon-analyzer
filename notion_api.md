# **Block**

A block object represents a piece of content within Notion. The API translates the headings, toggles, paragraphs, lists, media, and more that you can interact with in the Notion UI as different [__block type objects__](https://developers.notion.com/reference/block#block-type-objects).

For example, the following block object represents a `Heading 2` in the Notion UI:

Example Block Object

```
{
	"object": "block",
	"id": "c02fc1d3-db8b-45c5-a222-27595b15aea7",
	"parent": {
		"type": "page_id",
		"page_id": "59833787-2cf9-4fdf-8782-e53db20768a5"
	},
	"created_time": "2022-03-01T19:05:00.000Z",
	"last_edited_time": "2022-07-06T19:41:00.000Z",
	"created_by": {
		"object": "user",
		"id": "ee5f0f84-409a-440f-983a-a5315961c6e4"
	},
	"last_edited_by": {
		"object": "user",
		"id": "ee5f0f84-409a-440f-983a-a5315961c6e4"
	},
	"has_children": false,
	"archived": false,
  "in_trash": false,
	"type": "heading_2",
	"heading_2": {
		"rich_text": [
			{
				"type": "text",
				"text": {
					"content": "Lacinato kale",
					"link": null
				},
				"annotations": {
					"bold": false,
					"italic": false,
					"strikethrough": false,
					"underline": false,
					"code": false,
					"color": "green"
				},
				"plain_text": "Lacinato kale",
				"href": null
			}
		],
		"color": "default",
    "is_toggleable": false
	}
}
```

Use the [__Retrieve block children__](https://developers.notion.com/reference/get-block-children) endpoint to list all of the blocks on a page.

# **Keys**

> ## **📘**
>
> Fields marked with an * are available to integrations with any capabilities. Other properties require read content capabilities in order to be returned from the Notion API. Consult the [__integration capabilities reference__](https://developers.notion.com/reference/capabilities) for details.

**FieldTypeDescriptionExample value**`object`*`string`Always `"block"`.`"block"id`*`string` (UUIDv4)Identifier for the block.`"7af38973-3787-41b3-bd75-0ed3a1edfac9"parentobject`Information about the block's parent. See [__Parent object__](https://developers.notion.com/reference/parent-object).`{ "type": "block_id", "block_id": "7d50a184-5bbe-4d90-8f29-6bec57ed817b" }typestring` (enum)Type of block. Possible values are:

- `"bookmark"`
- `"breadcrumb"`
- `"bulleted_list_item"`
- `"callout"`
- `"child_database"`
- `"child_page"`
- `"column"`
- `"column_list"`
- `"divider"`
- `"embed"`
- `"equation"`
- `"file"`
- `"heading_1"`
- `"heading_2"`
- `"heading_3"`
- `"image"`
- `"link_preview"`
- `"numbered_list_item"`
- `"paragraph"`
- `"pdf"`
- `"quote"`
- `"synced_block"`
- `"table"`
- `"table_of_contents"`
- `"table_row"`
- `"template"`
- `"to_do"`
- `"toggle"`
- `"unsupported"`
- `"video""paragraph"created_timestring` ([__ISO 8601 date time__](https://en.wikipedia.org/wiki/ISO_8601))Date and time when this block was created. Formatted as an [__ISO 8601 date time__](https://en.wikipedia.org/wiki/ISO_8601) string.`"2020-03-17T19:10:04.968Z"created_by`[__Partial User__](https://developers.notion.com/reference/user)User who created the block.`{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}last_edited_timestring` ([__ISO 8601 date time__](https://en.wikipedia.org/wiki/ISO_8601))Date and time when this block was last updated. Formatted as an [__ISO 8601 date time__](https://en.wikipedia.org/wiki/ISO_8601) string.`"2020-03-17T19:10:04.968Z"last_edited_by`[__Partial User__](https://developers.notion.com/reference/user)User who last edited the block.`{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}archivedboolean`The archived status of the block.`falsein_trashboolean`Whether the block has been deleted.`falsehas_childrenboolean`Whether or not the block has children blocks nested within it.`true{type}block type object`An object containing type-specific block information.Refer to the [__block type object section__](https://developers.notion.com/reference/block#block-type-objects) for examples of each block type.

### **Block types that support child blocks**

Some block types contain nested blocks. The following block types support child blocks:
- [__Bulleted list item__](https://developers.notion.com/reference/block#bulleted-list-item)
- [__Callout__](https://developers.notion.com/reference/block#callout)
- [__Child database__](https://developers.notion.com/reference/block#child-database)
- [__Child page__](https://developers.notion.com/reference/block#child-page)
- [__Column__](https://developers.notion.com/reference/block#column-list-and-column)
- [__Heading 1__](https://developers.notion.com/reference/block#heading-1), when the `is_toggleable` property is `true`
- [__Heading 2__](https://developers.notion.com/reference/block#heading-2), when the `is_toggleable` property is `true`
- [__Heading 3__](https://developers.notion.com/reference/block#heading-3), when the `is_toggleable` property is `true`
- [__Numbered list item__](https://developers.notion.com/reference/block#numbered-list-item)
- [__Paragraph__](https://developers.notion.com/reference/block#paragraph)
- [__Quote__](https://developers.notion.com/reference/block#quote)
- [__Synced block__](https://developers.notion.com/reference/block#synced-block)
- [__Table__](https://developers.notion.com/reference/block#table)
- [__Template__](https://developers.notion.com/reference/block#template)
- [__To do__](https://developers.notion.com/reference/block#to-do)
- [__Toggle__](https://developers.notion.com/reference/block#toggle-blocks)

> ## **📘The API does not support all block types.**
>
> Only the block type objects listed in the reference below are supported. Any unsupported block types appear in the structure, but contain a `type` set to `"unsupported"`.

# **Block type objects**

Every block object has a key corresponding to the value of `type`. Under the key is an object with type-specific block information.

> ## **📘**
>
> Many block types support rich text. In cases where it is supported, a `rich_text`[__ object__](https://developers.notion.com/reference/rich-text) will be included in the block `type` object. All `rich_text` objects will include a `plain_text` property, which provides a convenient way for developers to access unformatted text from the Notion block.

## **Audio**

Audio block objects contain a [__file object__](https://developers.notion.com/reference/file-object) detailing information about the audio file.

Example Audio block object

```
{
  "type": "audio",
  //...other keys excluded
  "audio": {
    "type": "external",
    "external": {
      "url": "https://companywebsite.com/files/sample.mp3"
    }
  }
}
```

### **Supported audio types**

The following file types can be attached with external URLs in the API as well as in the Notion app UI:
- `.mp3`
- `.wav`
- `.ogg`
- `.oga`
- `.m4a`

A wider set of audio files is [__supported in the File Upload API__](https://developers.notion.com/reference/working-with-files-and-media#supported-file-types) and can be attached using a `file_upload` ID.

### **Supported file upload types**

See the [__file upload reference__](https://developers.notion.com/reference/file-upload#file-types-and-sizes) for a list of supported file extensions and content types when attaching a File Upload to a block.

Audio blocks only support file types in the "audio" section of the table.

## **Bookmark**

Bookmark block objects contain the following information within the `bookmark` property:

**FieldTypeDescription**`caption`array of [__rich text objects__](https://developers.notion.com/reference/rich-text) textThe caption for the bookmark.`url`stringThe link for the bookmark.

Example Bookmark block object

```
{
  //...other keys excluded
  "type": "bookmark",
  //...other keys excluded
  "bookmark": {
    "caption": [],
    "url": "https://companywebsite.com"
  }
}
```

## **Breadcrumb**

Breadcrumb block objects do not contain any information within the `breadcrumb` property.

Example Breadcrumb block object

```
{
  //...other keys excluded
  "type": "breadcrumb",
  //...other keys excluded
  "breadcrumb": {}
}
```

## **Bulleted list item**

Bulleted list item block objects contain the following information within the `bulleted_list_item` property:

**FieldTypeDescription**`rich_textarray` of [__rich text objects__](https://developers.notion.com/reference/rich-text)The rich text in the `bulleted_list_item` block.`colorstring` (enum)The color of the block. Possible values are:

- `"blue"`
- `"blue_background"`
- `"brown"`
- `"brown_background"`
- `"default"`
- `"gray"`
- `"gray_background"`
- `"green"`
- `"green_background"`
- `"orange"`
- `"orange_background"`
- `"yellow"`
- `"green"`
- `"pink"`
- `"pink_background"`
- `"purple"`
- `"purple_background"`
- `"red"`
- `"red_background"`
- `"yellow_background"childrenarray` of [__block objects__](https://developers.notion.com/reference/block)The nested child blocks (if any) of the `bulleted_list_item` block.

Example Bulleted list item block object

```
{
  //...other keys excluded
  "type": "bulleted_list_item",
  //...other keys excluded
  "bulleted_list_item": {
    "rich_text": [{
      "type": "text",
      "text": {
        "content": "Lacinato kale",
        "link": null
      }
      // ..other keys excluded
    }],
    "color": "default",
    "children":[{
      "type": "paragraph"
      // ..other keys excluded
    }]
  }
}
```

## **Callout**

Callout block objects contain the following information within the `callout` property:

**FieldTypeDescription**`rich_textarray` of [__rich text objects__](https://developers.notion.com/reference/rich-text)The rich text in the `callout` block.`iconobject`An [__emoji__](https://developers.notion.com/reference/emoji-object) or [__file__](https://developers.notion.com/reference/file-object) object that represents the callout's icon. If the callout does not have an icon.`colorstring` (enum)The color of the block. Possible values are:

- `"blue"`
- `"blue_background"`
- `"brown"`
- `"brown_background"`
- `"default"`
- `"gray"`
- `"gray_background"`
- `"green"`
- `"green_background"`
- `"orange"`
- `"orange_background"`
- `"yellow"`
- `"green"`
- `"pink"`
- `"pink_background"`
- `"purple"`
- `"purple_background"`
- `"red"`
- `"red_background"`
- `"yellow_background"`

Example Callout block object

```
{
  //...other keys excluded
	"type": "callout",
   // ..other keys excluded
   "callout": {
   	"rich_text": [{
      "type": "text",
      "text": {
        "content": "Lacinato kale",
        "link": null
      }
      // ..other keys excluded
    }],
     "icon": {
       "emoji": "⭐"
     },
     "color": "default"
   }
}
```

## **Child database**

Child database block objects contain the following information within the `child_database` property:

**FieldTypeDescription**`titlestring`The plain text title of the database.

Example Child database block

```
{
  //...other keys excluded
  "type": "child_database",
  //...other keys excluded
  "child_database": {
    "title": "My database"
  }
}
```

> ## **📘Creating and updating **`child_database`** blocks**
>
> To create or update `child_database` type blocks, use the [__Create a database__](https://developers.notion.com/reference/create-a-database) and the [__Update a database__](https://developers.notion.com/reference/update-a-database) endpoints, specifying the ID of the parent page in the `parent` body param.

## **Child page**

Child page block objects contain the following information within the `child_page` property:

**FieldTypeDescription**`titlestring`The plain text `title` of the page.

Example Child page block object

```
{
  //...other keys excluded
  "type": "child_page",
  //...other keys excluded
  "child_page": {
    "title": "Lacinato kale"
  }
}
```

> ## **📘Creating and updating **`child_page`** blocks**
>
> To create or update `child_page` type blocks, use the [__Create a page__](https://developers.notion.com/reference/post-page) and the [__Update page__](https://developers.notion.com/reference/patch-page) endpoints, specifying the ID of the parent page in the `parent` body param.

## **Code**

Code block objects contain the following information within the `code` property:

**FieldTypeDescription**`captionarray` of [__Rich text object__](https://developers.notion.com/reference/rich-text) text objectsThe rich text in the caption of the code block.`rich_textarray` of [__Rich text object__](https://developers.notion.com/reference/rich-text) text objectsThe rich text in the code block.`language`- `"abap"` - `"arduino"` - `"bash"` - `"basic"` - `"c"` - `"clojure"` - `"coffeescript"` - `"c++"` - `"c#"` - `"css"` - `"dart"` - `"diff"` - `"docker"` - `"elixir"` - `"elm"` - `"erlang"` - `"flow"` - `"fortran"` - `"f#"` - `"gherkin"` - `"glsl"` - `"go"` - `"graphql"` - `"groovy"` - `"haskell"` - `"html"` - `"java"` - `"javascript"` - `"json"` - `"julia"` - `"kotlin"` - `"latex"` - `"less"` - `"lisp"` - `"livescript"` - `"lua"` - `"makefile"` - `"markdown"` - `"markup"` - `"matlab"` - `"mermaid"` - `"nix"` - `"objective-c"` - `"ocaml"` - `"pascal"` - `"perl"` - `"php"` - `"plain text"` - `"powershell"` - `"prolog"` - `"protobuf"` - `"python"` - `"r"` - `"reason"` - `"ruby"` - `"rust"` - `"sass"` - `"scala"` - `"scheme"` - `"scss"` - `"shell"` - `"sql"` - `"swift"` - `"typescript"` - `"vb.net"` - `"verilog"` - `"vhdl"` - `"visual basic"` - `"webassembly"` - `"xml"` - `"yaml"` - `"java/c/c++/c#"`The language of the code contained in the code block.

Example Code block object

```
{
  // ... other keys excluded
  "type": "code",
  // ... other keys excluded
  "code": {
    "caption": [],
    "rich_text": [{
      "type": "text",
      "text": {
        "content": "const a = 3"
      }
    }],
    "language": "javascript"
  }
}
```

## **Column list and column**

Column lists are parent blocks for columns. They do not contain any information within the `column_list` property.

Example Column list block object

```
{
  // ... other keys excluded
  "type": "column_list",
  // ... other keys excluded
  "column_list": {}
}
```

Columns are parent blocks for any block types listed in this reference except for other `column`s. They do not require any information within the `column` property, but a `width_ratio` number between 0 and 1 can be provided to customize the width of a column relative to others in the same column list. When omitted, the default is to use equal widths for all columns. When provided, `width_ratio`s should add up to 1.

Columns can only be appended to `column_list`s.

Example Column object

```
{
  // ... other keys excluded
  "type": "column",
  // ... other keys excluded
  "column": {
    "width_ratio": 0.25
  }
}
```

When creating a `column_list` block via [__Append block children__](https://developers.notion.com/reference/patch-block-children), the `column_list` must have at least two `column`s, and each `column` must have at least one child.

### **Retrieve the content in a column list**

Follow these steps to fetch the content in a `column_list`:
1. Get the `column_list` ID from a query to [__Retrieve block children__](https://developers.notion.com/reference/get-block-children) for the parent page.
2. Get the `column` children from a query to Retrieve block children for the `column_list`.
3. Get the content in each individual `column` from a query to Retrieve block children for the unique `column` ID.

## **Divider**

Divider block objects do not contain any information within the `divider` property.

Example Divider block object

```
{
  //...other keys excluded
  "type": "divider",
  //...other keys excluded
  "divider": {}
}
```

## **Embed**

Embed block objects include information about another website displayed within the Notion UI. The `embed` property contains the following information:

**FieldTypeDescription**`urlstring`The link to the website that the embed block displays.

Example Embed block object

```
{
  //...other keys excluded
  "type": "embed",
  //...other keys excluded
  "embed": {
    "url": "https://companywebsite.com"
  }
}
```

> ## **🚧Differences in embed blocks between the Notion app and the API**
>
> The Notion app uses a 3rd-party service, iFramely, to validate and request metadata for embeds given a URL. This works well in a web app because Notion can kick off an asynchronous request for URL information, which might take seconds or longer to complete, and then update the block with the metadata in the UI after receiving a response from iFramely.
>
> We chose not to call iFramely when creating embed blocks in the API because the API needs to be able to return faster than the UI, and because the response from iFramely could actually cause us to change the block type. This would result in a slow and potentially confusing experience as the block in the response would not match the block sent in the request.
>
> The result is that embed blocks created via the API may not look exactly like their counterparts created in the Notion app.

> ## **👍**
>
> Vimeo video links can be embedded in a Notion page via the public API using the embed block type.
>
> For example, the following object can be passed to the [__Append block children endpoint__](https://developers.notion.com/reference/patch-block-children):
>
> JSON
>
> ```
> {
>   "children": [
>     {
>       "embed": {
>         "url": "https://player.vimeo.com/video/226053498?h=a1599a8ee9"
>       }
>     }
>   ]
> }
> 
> ```
>
> For other video sources, see [__Supported video types__](https://developers.notion.com/reference/block#supported-video-types).

## **Equation**

Equation block objects are represented as children of [__paragraph__](https://developers.notion.com/reference/block#paragraph) blocks. They are nested within a [__rich text object__](https://developers.notion.com/reference/rich-text) and contain the following information within the `equation` property:

**FieldTypeDescription**`expressionstring`A KaTeX compatible string.

Example Equation object

```
{
  //...other keys excluded
  "type": "equation",
  //...other keys excluded
  "equation": {
    "expression": "e=mc^2"
  }
}
```

## **File**

File block objects contain the following information within the `file` property:

**FieldTypeDescription**`captionarray` of [__rich text objects__](https://developers.notion.com/reference/rich-text)The caption of the file block.`type`One of:

- `"file"`
- `"external"`
- `"file_upload"`Type of file. This enum value indicates which of the following three objects are populated.`file`[__Notion-hosted file object__](https://developers.notion.com/reference/file-object#notion-hosted-files)A file object that details information about the file contained in the block: a temporary download `url` and `expiry_time`. After the `expiry_time`, fetch the block again from the API to get a new `url`.

Only valid as a parameter if copied verbatim from the `file` field of a recent block API response from Notion. To attach a file, provide a `type` of `file_upload` instead.`external`[__External file object__](https://developers.notion.com/reference/file-object#external-files)An object with a `url` property, identifying a publicly accessible URL.`file_upload`[__File upload object__](https://developers.notion.com/reference/file#file-uploads)An object with the `id` of a [__FileUpload__](https://developers.notion.com/reference/file-upload) to attach to the block. After attaching, the API response responds with a type of `file`, not `file_upload`, so your integration can access a download `url`.`namestring`The name of the file, as shown in the Notion UI. Note that the UI may auto-append `.pdf` or other extensions.

When attaching a `file_upload`, the `name` parameter is not required.

Example File block

```
{
  // ... other keys excluded
  "type": "file",
  // ... other keys excluded
  "file": {
    "caption": [],
    "type": "external",
    "external": {
      "url": "https://companywebsite.com/files/doc.txt"
    },
    "name": "doc.txt"
  }
}
```

## **Headings**

All heading block objects, `heading_1`, `heading_2`, and `heading_3`, contain the following information within their corresponding objects:

**FieldTypeDescription**`rich_textarray` of [__rich text objects__](https://developers.notion.com/reference/rich-text)The rich text of the heading.`colorstring` (enum)The color of the block. Possible values are:

- `"blue"`
- `"blue_background"`
- `"brown"`
- `"brown_background"`
- `"default"`
- `"gray"`
- `"gray_background"`
- `"green"`
- `"green_background"`
- `"orange"`
- `"orange_background"`
- `"yellow"`
- `"green"`
- `"pink"`
- `"pink_background"`
- `"purple"`
- `"purple_background"`
- `"red"`
- `"red_background"`
- `"yellow_background"is_toggleableboolean`Whether or not the heading block is a toggle heading or not. If `true`, then the heading block toggles and can support children. If `false`, then the heading block is a static heading block.

Example Heading 1 block object

```
{
  //...other keys excluded
  "type": "heading_1",
  //...other keys excluded
  "heading_1": {
    "rich_text": [{
      "type": "text",
      "text": {
        "content": "Lacinato kale",
        "link": null
      }
    }],
    "color": "default",
    "is_toggleable": false
  }
}
```

Example Heading 2 block object

```
{
  //...other keys excluded
  "type": "heading_2",
  //...other keys excluded
  "heading_2": {
    "rich_text": [{
      "type": "text",
      "text": {
        "content": "Lacinato kale",
        "link": null
      }
    }],
    "color": "default",
    "is_toggleable": false
  }
}
```

Example Heading 3 block object

```
{
  //...other keys excluded
  "type": "heading_3",
  //...other keys excluded
  "heading_3": {
    "rich_text": [{
      "type": "text",
      "text": {
        "content": "Lacinato kale",
        "link": null
      }
    }],
    "color": "default",
    "is_toggleable": false
  }
}
```

## **Image**

Image block objects contain a [__file object__](https://developers.notion.com/reference/file-object) detailing information about the image.

Example Image block object

```
{
  // ... other keys excluded
  "type": "image",
  // ... other keys excluded
  "image": {
    "type": "external",
    "external": {
      "url": "https://website.domain/images/image.png"
    }
  }
}
```

### **Supported external image types**

The image must be directly hosted. In other words, the `url` cannot point to a service that retrieves the image. The following image types are supported:
- `.bmp`
- `.gif`
- `.heic`
- `.jpeg`
- `.jpg`
- `.png`
- `.svg`
- `.tif`
- `.tiff`

### **Supported file upload types**

See the [__file upload reference__](https://developers.notion.com/reference/file-upload#file-types-and-sizes) for a list of supported file extensions and content types when attaching a File Upload to a block.

Image blocks only support file types in the "image" section of the table.

## **Link Preview**

[__Link Preview__](https://developers.notion.com/docs/link-previews) block objects contain the originally pasted `url`:

Example Link preview block object

```
{
  //...other keys excluded
  "type": "link_preview",
  //...other keys excluded
  "link_preview": {
    "url": "https://github.com/example/example-repo/pull/1234"
  }
}
```

> ## **🚧**
>
> The `link_preview` block can only be returned as part of a response. The API does not support creating or appending `link_preview` blocks.

## **Mention**

A mention block object is a child of a [__rich text object__](https://developers.notion.com/reference/rich-text) that is nested within a [__paragraph block object__](https://developers.notion.com/reference/block#paragraph). This block type represents any `@` tag in the Notion UI, for a user, date, Notion page, Notion database, or a miniaturized version of a [__Link Preview__](https://developers.notion.com/reference/unfurl-attribute-object).

A mention block object contains the following fields:

**FieldTypeDescription**`type"database"`

`"date"`

`"link_preview"`

`"page"`

`"user"`A constant string representing the type of the mention.`"database"`

`"date"`

`"link_preview"`

`"page"`

`"user"object`An object with type-specific information about the mention.

Example Mention object

```
{
  //...other keys excluded
  "type": "page",
  "page": {
    "id": "3c612f56-fdd0-4a30-a4d6-bda7d7426309"
  }
}
```

## **Numbered list item**

Numbered list item block objects contain the following information within the `numbered_list_item` property:

**FieldTypeDescription**`rich_textarray` of [__rich text objects__](https://developers.notion.com/reference/rich-text)The rich text displayed in the `numbered_list_item` block.`colorstring` (enum)The color of the block. Possible values are:

- `"blue"`
- `"blue_background"`
- `"brown"`
- `"brown_background"`
- `"default"`
- `"gray"`
- `"gray_background"`
- `"green"`
- `"green_background"`
- `"orange"`
- `"orange_background"`
- `"yellow"`
- `"green"`
- `"pink"`
- `"pink_background"`
- `"purple"`
- `"purple_background"`
- `"red"`
- `"red_background"`
- `"yellow_background"childrenarray` of [__block objects__](https://developers.notion.com/reference/block)The nested child blocks (if any) of the `numbered_list_item` block.

Example Numbered list item block

```
{
  //...other keys excluded
  "type": "numbered_list_item",
  "numbered_list_item": {
    "rich_text": [
      {
        "type": "text",
        "text": {
          "content": "Finish reading the docs",
          "link": null
        }
      }
    ],
    "color": "default"
  }
}
```

## **Paragraph**

Paragraph block objects contain the following information within the `paragraph` property:

**FieldTypeDescription**`rich_textarray` of [__rich text objects__](https://developers.notion.com/reference/rich-text)The rich text displayed in the paragraph block.`colorstring` (enum)The color of the block. Possible values are:

- `"blue"`
- `"blue_background"`
- `"brown"`
- `"brown_background"`
- `"default"`
- `"gray"`
- `"gray_background"`
- `"green"`
- `"green_background"`
- `"orange"`
- `"orange_background"`
- `"yellow"`
- `"green"`
- `"pink"`
- `"pink_background"`
- `"purple"`
- `"purple_background"`
- `"red"`
- `"red_background"`
- `"yellow_background"childrenarray` of [__block objects__](https://developers.notion.com/reference/block)The nested child blocks (if any) of the `paragraph` block.

Example Paragraph block object

```
{
  //...other keys excluded
  "type": "paragraph",
  //...other keys excluded
  "paragraph": {
    "rich_text": [{
      "type": "text",
      "text": {
        "content": "Lacinato kale",
        "link": null
      }
    }],
    "color": "default"
}
```

Example Paragraph block object with a child Mention block object

```
{
//...other keys excluded
	"type": "paragraph",
  	"paragraph":{
  		"rich_text": [
    		{
      		"type": "mention",
      		"mention": {
        		"type": "date",
        		"date": {
          		"start": "2023-03-01",
          		"end": null,
          		"time_zone": null
        		}
      		},
      		"annotations": {
        		"bold": false,
        		"italic": false,
        		"strikethrough": false,
        		"underline": false,
        		"code": false,
        		"color": "default"
      		},
      		"plain_text": "2023-03-01",
      		"href": null
    		},
    		{
          "type": "text",
      		"text": {
        		"content": " ",
        		"link": null
      		},
      		"annotations": {
        		"bold": false,
        		"italic": false,
        		"strikethrough": false,
        		"underline": false,
        		"code": false,
        		"color": "default"
      		},
      		"plain_text": " ",
      		"href": null
    		}
  		],
  		"color": "default"
  	}
}
```

## **PDF**

A PDF block object represents a PDF that has been embedded within a Notion page. It contains the following fields:

**PropertyTypeDescription**`captionarray` of [__rich text objects__](https://developers.notion.com/reference/rich-text)A caption, if provided, for the PDF block.`type`One of:

- `"file"`
- `"external"`
- `"file_upload"`A constant string representing the type of PDF. `file` indicates a Notion-hosted file, and `external` represents a third-party link. `file_upload` is only valid when providing parameters to attach a [__File Upload__](https://developers.notion.com/reference/file-upload) to a PDF block.`external` |
`file` |
`file_upload`[__file object__](https://developers.notion.com/reference/file-object)An object containing type-specific information about the PDF.

JSON

```
{
  //...other keys excluded
  "type": "pdf",
  //...other keys excluded
  "pdf": {
    "type": "external",
    "external": {
      "url": "https://website.domain/files/doc.pdf"
    }
  }
}
```

### **Supported file upload types**

See the [__file upload reference__](https://developers.notion.com/reference/file-upload#file-types-and-sizes) for a list of supported file extensions and content types when attaching a File Upload to a block.

PDF blocks only support a type of `.pdf`.

## **Quote**

Quote block objects contain the following information within the `quote` property:

**FieldTypeDescription**`rich_textarray` of [__rich text objects__](https://developers.notion.com/reference/rich-text)The rich text displayed in the quote block.`colorstring` (enum)The color of the block. Possible values are:

- `"blue"`
- `"blue_background"`
- `"brown"`
- `"brown_background"`
- `"default"`
- `"gray"`
- `"gray_background"`
- `"green"`
- `"green_background"`
- `"orange"`
- `"orange_background"`
- `"yellow"`
- `"green"`
- `"pink"`
- `"pink_background"`
- `"purple"`
- `"purple_background"`
- `"red"`
- `"red_background"`
- `"yellow_background"childrenarray` of [__block objects__](https://developers.notion.com/reference/block)The nested child blocks, if any, of the quote block.

Example Quote block

```
{
	//...other keys excluded
	"type": "quote",
   //...other keys excluded
   "quote": {
   	"rich_text": [{
      "type": "text",
      "text": {
        "content": "To be or not to be...",
        "link": null
      },
    	//...other keys excluded
    }],
    //...other keys excluded
    "color": "default"
   }
}
```

## **Synced block**

Similar to the Notion UI, there are two versions of a `synced_block` object: the original block that was created first and doesn't yet sync with anything else, and the duplicate block or blocks synced to the original.

> ## **📘**
>
> An original synced block must be created before corresponding duplicate block or blocks can be made.

### **Original synced block**

Original synced block objects contain the following information within the `synced_block` property:

**FieldTypeDescription**`synced_fromnull`The value is always `null` to signify that this is an original synced block that does not refer to another block.`childrenarray` of [__block objects__](https://developers.notion.com/reference/block)The nested child blocks, if any, of the `synced_block` block. These blocks will be mirrored in the duplicate `synced_block`.

Example Original synced block

```
{
    //...other keys excluded
  	"type": "synced_block",
    "synced_block": {
        "synced_from": null,
        "children": [
            {
                "callout": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Callout in synced block"
                            }
                        }
                    ]
                }
            }
        ]
    }
}
```

### **Duplicate synced block**

Duplicate synced block objects contain the following information within the `synced_from` object:

**FieldTypeDescription**`typestring` (enum)The type of the synced from object.

Possible values are:

- `"block_id"block_idstring` (UUIDv4)An identifier for the original `synced_block`.

Example Duplicate synced block object

```
{
    //...other keys excluded
  	"type": "synced_block",
    "synced_block": {
        "synced_from": {
            "block_id": "original_synced_block_id"
        }
    }
}
```

> ## **🚧**
>
> The API does not supported updating synced block content.

## **Table**

Table block objects are parent blocks for table row children. Table block objects contain the following fields within the `table` property:

**FieldTypeDescription**`table_widthinteger`The number of columns in the table.

**Note that this cannot be changed via the public API once a table is created.**`has_column_headerboolean`Whether the table has a column header. If `true`, then the first row in the table appears visually distinct from the other rows.`has_row_headerboolean`Whether the table has a header row. If `true`, then the first column in the table appears visually distinct from the other columns.

Example Table block object

```
{
  //...other keys excluded
  "type": "table",
  "table": {
    "table_width": 2,
    "has_column_header": false,
    "has_row_header": false
  }
}
```

> ## **🚧**`table_width`** can only be set when the table is first created.**
>
> Note that the number of columns in a table can only be set when the table is first created. Calls to the Update block endpoint to update `table_width` fail.

### **Table rows**

Follow these steps to fetch the `table_row`s of a `table`:
1. Get the `table` ID from a query to [__Retrieve block children__](https://developers.notion.com/reference/get-block-children) for the parent page.
2. Get the `table_rows` from a query to Retrieve block children for the `table`.

A `table_row` block object contains the following fields within the `table_row` property:

**PropertyTypeDescription**`cellsarray` of array of [__rich text objects__](https://developers.notion.com/reference/rich-text)An array of cell contents in horizontal display order. Each cell is an array of rich text objects.

Example Table row block object

```
{
  //...other keys excluded
  "type": "table_row",
  "table_row": {
    "cells": [
      [
        {
          "type": "text",
          "text": {
            "content": "column 1 content",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "column 1 content",
          "href": null
        }
      ],
      [
        {
          "type": "text",
          "text": {
            "content": "column 2 content",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "column 2 content",
          "href": null
        }
      ],
      [
        {
          "type": "text",
          "text": {
            "content": "column 3 content",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "column 3 content",
          "href": null
        }
      ]
    ]
  }
}
```

> ## **📘**
>
> When creating a table block via the [__Append block children__](https://developers.notion.com/reference/patch-block-children) endpoint, the `table` must have at least one `table_row` whose `cells` array has the same length as the `table_width`.

## **Table of contents**

Table of contents block objects contain the following information within the `table_of_contents` property:

**PropertyTypeDescription**`colorstring` (enum)The color of the block. Possible values are:

- `"blue"`
- `"blue_background"`
- `"brown"`
- `"brown_background"`
- `"default"`
- `"gray"`
- `"gray_background"`
- `"green"`
- `"green_background"`
- `"orange"`
- `"orange_background"`
- `"yellow"`
- `"green"`
- `"pink"`
- `"pink_background"`
- `"purple"`
- `"purple_background"`
- `"red"`
- `"red_background"`
- `"yellow_background"`

Example Table of contents block object

```
{
  //...other keys excluded
	"type": "table_of_contents",
  "table_of_contents": {
  	"color": "default"
  }
}
```

## **Template**

> ## **❗️Deprecation Notice**
>
> As of March 27, 2023 creation of template blocks will no longer be supported.

Template blocks represent [__template buttons__](https://www.notion.so/help/template-buttons) in the Notion UI.

Template block objects contain the following information within the `template` property:

**FieldTypeDescription**`rich_textarray` of [__rich text objects__](https://developers.notion.com/reference/rich-text)The rich text displayed in the title of the template.`childrenarray` of [__block objects__](https://developers.notion.com/reference/block)The nested child blocks, if any, of the template block. These blocks are duplicated when the template block is used in the UI.

Example Template block object

```
{
  //...other keys excluded
  "template": {
    "rich_text": [
      {
        "type": "text",
        "text": {
          "content": "Add a new to-do",
          "link": null
        },
        "annotations": {
          //...other keys excluded
        },
        "plain_text": "Add a new to-do",
        "href": null
      }
    ]
  }
}
```

## **To do**

To do block objects contain the following information within the `to_do` property:

**FieldTypeDescription**`rich_textarray` of [__rich text objects__](https://developers.notion.com/reference/rich-text)The rich text displayed in the To do block.`checkedboolean` (optional)Whether the To do is checked.`colorstring` (enum)The color of the block. Possible values are:

- `"blue"`
- `"blue_background"`
- `"brown"`
- `"brown_background"`
- `"default"`
- `"gray"`
- `"gray_background"`
- `"green"`
- `"green_background"`
- `"orange"`
- `"orange_background"`
- `"yellow"`
- `"green"`
- `"pink"`
- `"pink_background"`
- `"purple"`
- `"purple_background"`
- `"red"`
- `"red_background"`
- `"yellow_background"childrenarray` of [__block objects__](https://developers.notion.com/reference/block)The nested child blocks, if any, of the To do block.

Example To do block object

```
{
  //...other keys excluded
  "type": "to_do",
  "to_do": {
    "rich_text": [{
      "type": "text",
      "text": {
        "content": "Finish Q3 goals",
        "link": null
      }
    }],
    "checked": false,
    "color": "default",
    "children":[{
      "type": "paragraph"
      // ..other keys excluded
    }]
  }
}
```

## **Toggle blocks**

Toggle block objects contain the following information within the `toggle` property:

**FieldTypeDescription**`rich_textarray` of [__rich text objects__](https://developers.notion.com/reference/rich-text)The rich text displayed in the Toggle block.`colorstring` (enum)The color of the block. Possible values are:

- `"blue"`
- `"blue_background"`
- `"brown"`
- `"brown_background"`
- `"default"`
- `"gray"`
- `"gray_background"`
- `"green"`
- `"green_background"`
- `"orange"`
- `"orange_background"`
- `"yellow"`
- `"green"`
- `"pink"`
- `"pink_background"`
- `"purple"`
- `"purple_background"`
- `"red"`
- `"red_background"`
- `"yellow_background"childrenarray` of [__block objects__](https://developers.notion.com/reference/block)The nested child blocks, if any, of the Toggle block.

Toggle Block

```
{
  //...other keys excluded
  "type": "toggle",
  "toggle": {
    "rich_text": [{
      "type": "text",
      "text": {
        "content": "Additional project details",
        "link": null
      }
      //...other keys excluded
    }],
    "color": "default",
    "children":[{
      "type": "paragraph"
      // ..other keys excluded
    }]
  }
}
```

## **Video**

Video block objects contain a [__file object__](https://developers.notion.com/reference/file-object) detailing information about the video.

Example Video block object

```
{
  "type": "video",
  //...other keys excluded
  "video": {
    "type": "external",
    "external": {
      "url": "https://companywebsite.com/files/video.mp4"
    }
  }
}
```

### **Supported video types**

- `.amv`
- `.asf`
- `.avi`
- `.f4v`
- `.flv`
- `.gifv`
- `.mkv`
- `.mov`
- `.mpg`
- `.mpeg`
- `.mpv`
- `.mp4`
- `.m4v`
- `.qt`
- `.wmv`
- YouTube video links that include `embed` or `watch`.
  E.g. `https://www.youtube.com/watch?v=[id]`, `https://www.youtube.com/embed/[id]`

> ## **📘**
>
> Vimeo video links are not currently supported by the video block type. However, they can be embedded in Notion pages using the `embed` block type. See [__Embed__](https://developers.notion.com/reference/block#embed) for more information.

### **Supported file upload types**

See the [__file upload reference__](https://developers.notion.com/reference/file-upload#file-types-and-sizes) for a list of supported file extensions and content types when attaching a File Upload to a block.

Video blocks only support file types in the "video" section of the table.

**Rich text**

Notion uses rich text to allow users to customize their content. Rich text refers to a type of document where content can be styled and formatted in a variety of customizable ways. This includes styling decisions, such as the use of italics, font size, and font color, as well as formatting, such as the use of hyperlinks or code blocks.

Notion includes rich text objects in [__block objects__](https://developers.notion.com/reference/block) to indicate how blocks in a page are represented. [__Blocks__](https://developers.notion.com/reference/block) that support rich text will include a rich text object; however, not all block types offer rich text.

When blocks are retrieved from a page using the [__Retrieve a block__](https://developers.notion.com/reference/retrieve-a-block) or [__Retrieve block children__](https://developers.notion.com/reference/get-block-children) endpoints, an array of rich text objects will be included in the block object (when available). Developers can use this array to retrieve the plain text (`plain_text`) for the block or get all the rich text styling and formatting options applied to the block.

An example rich text object

```
{
  "type": "text",
  "text": {
    "content": "Some words ",
    "link": null
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "Some words ",
  "href": null
}
```

> ## **📘**
>
> Many [__block types__](https://developers.notion.com/reference/block#block-type-objects) support rich text. In cases where it is supported, a `rich_text` object will be included in the block `type` object. All `rich_text` objects will include a `plain_text` property, which provides a convenient way for developers to access unformatted text from the Notion block.

Each rich text object contains the following fields.

**FieldTypeDescriptionExample value**`typestring` (enum)The type of this rich text object. Possible type values are: `"text"`, `"mention"`, `"equation"`.`"text"text` | `mention` | `equationobject`An object containing type-specific configuration.

Refer to the rich text type objects section below for details on type-specific values.Refer to the rich text type objects section below for examples.`annotationsobject`The information used to style the rich text object. Refer to the annotation object section below for details.Refer to the annotation object section below for examples.`plain_textstring`The plain text without annotations.`"Some words "hrefstring` (optional)The URL of any link or Notion mention in this text, if any.`"https://www.notion.so/Avocado-d093f1d200464ce78b36e58a3f0d8043"`

## **The annotation object**

All rich text objects contain an `annotations` object that sets the styling for the rich text. `annotations` includes the following fields:

**PropertyTypeDescriptionExample value**`boldboolean`Whether the text is **bolded**.`trueitalicboolean`Whether the text is *italicized*.`truestrikethroughboolean`Whether the text is struck through.`falseunderlineboolean`Whether the text is underlined.`falsecodeboolean`Whether the text is `code style`.`truecolorstring` (enum)Color of the text. Possible values include:

- `"blue"`
- `"blue_background"`
- `"brown"`
- `"brown_background"`
- `"default"`
- `"gray"`
- `"gray_background"`
- `"green"`
- `"green_background"`
- `"orange"`
-`"orange_background"`
- `"pink"`
- `"pink_background"`
- `"purple"`
- `"purple_background"`
- `"red"`
- `"red_background”`
- `"yellow"`
- `"yellow_background""green"`

## **Rich text type objects**

### **Equation**

Notion supports inline LaTeX equations as rich text object’s with a type value of `"equation"`. The corresponding equation type object contains the following:

**FieldTypeDescriptionExample value**`expressionstring`The LaTeX string representing the inline equation.`"\frac{{ - b \pm \sqrt {b^2 - 4ac} }}{{2a}}"`

**Example rich text **`equation`** object**

JSON

```
{
  "type": "equation",
  "equation": {
    "expression": "E = mc^2"
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "E = mc^2",
  "href": null
}
```

### **Mention**

Mention objects represent an inline mention of a database, date, link preview mention, page, template mention, or user. A mention is created in the Notion UI when a user types `@` followed by the name of the reference.

If a rich text object’s `type` value is `"mention"`, then the corresponding `mention` object contains the following:

**FieldTypeDescriptionExample value**`typestring` (enum)The type of the inline mention. Possible values include:

- `"database"`
- `"date"`
- `"link_preview"`
- `"page"`
- `"template_mention"`
- `"user""user"database` | `date` | `link_preview` | `page` | `template_mention` | `userobject`An object containing type-specific configuration. Refer to the mention type object sections below for details.Refer to the mention type object sections below for example values.

**Database mention type object**

Database mentions contain a database reference within the corresponding `database` field. A database reference is an object with an `id` key and a string value (UUIDv4) corresponding to a database ID.

If an integration doesn’t have [__access__](https://developers.notion.com/reference/capabilities) to the mentioned database, then the mention is returned with just the ID. The `plain_text` value that would be a title appears as `"Untitled"` and the annotation object’s values are defaults.

*Example rich text* `mention` *object for a* `database` *mention*

JSON

```
{
  "type": "mention",
  "mention": {
    "type": "database",
    "database": {
      "id": "a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "Database with test things",
  "href": "https://www.notion.so/a1d8501e1ac143e9a6bdea9fe6c8822b"
}
```

**Date mention type object**

Date mentions contain a [__date property value object__](https://developers.notion.com/reference/property-value-object#date-property-values) within the corresponding `date` field.

*Example rich text* `mention` *object for a* `date` *mention*

JSON

```
{
  "type": "mention",
  "mention": {
    "type": "date",
    "date": {
      "start": "2022-12-16",
      "end": null
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "2022-12-16",
  "href": null
}
```

**Link Preview mention type object**

If a user opts to share a [__Link Preview__](https://developers.notion.com/docs/link-previews) as a mention, then the API handles the Link Preview mention as a rich text object with a `type` value of `link_preview`. Link preview rich text mentions contain a corresponding `link_preview` object that includes the `url` that is used to create the Link Preview mention.

*Example rich text* `mention` *object for a* `link_preview` *mention*

JSON

```
{
  "type": "mention",
  "mention": {
    "type": "link_preview",
    "link_preview": {
      "url": "https://workspace.slack.com/archives/C04PF0F9QSD/z1671139297838409?thread_ts=1671139274.065079&cid=C03PF0F9QSD"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "https://workspace.slack.com/archives/C04PF0F9QSD/z1671139297838409?thread_ts=1671139274.065079&cid=C03PF0F9QSD",
  "href": "https://workspace.slack.com/archives/C04PF0F9QSD/z1671139297838409?thread_ts=1671139274.065079&cid=C03PF0F9QSD"
}
```

**Page mention type object**

Page mentions contain a page reference within the corresponding `page` field. A page reference is an object with an `id` property and a string value (UUIDv4) corresponding to a page ID.

If an integration doesn’t have [__access__](https://developers.notion.com/reference/capabilities) to the mentioned page, then the mention is returned with just the ID. The `plain_text` value that would be a title appears as `"Untitled"` and the annotation object’s values are defaults.

*Example rich text* `mention` *object for a* `page` *mention*

JSON

```
{
  "type": "mention",
  "mention": {
    "type": "page",
    "page": {
      "id": "3c612f56-fdd0-4a30-a4d6-bda7d7426309"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "This is a test page",
  "href": "https://www.notion.so/3c612f56fdd04a30a4d6bda7d7426309"
}
```

**Template mention type object**

The content inside a [__template button__](https://www.notion.so/help/template-buttons) in the Notion UI can include placeholder date and user mentions that populate when a template is duplicated. Template mention type objects contain these populated values.

Template mention rich text objects contain a `template_mention` object with a nested `type` key that is either `"template_mention_date"` or `"template_mention_user"`.

If the `type` key is `"template_mention_date"`, then the rich text object contains the following `template_mention_date` field:

**FieldTypeDescriptionExample value**`template_mention_datestring` (enum)The type of the date mention. Possible values include: `"today"` and `"now"`.`"today"`

*Example rich text* `mention` *object for a* `template_mention_date` *mention*

JSON

```
{
  "type": "mention",
  "mention": {
    "type": "template_mention",
    "template_mention": {
      "type": "template_mention_date",
      "template_mention_date": "today"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "@Today",
  "href": null
}
```

If the type key is `"template_mention_user"`, then the rich text object contains the following `template_mention_user` field:

**FieldTypeDescriptionExample value**`template_mention_userstring` (enum)The type of the user mention. The only possible value is `"me"`.`"me"`

*Example rich text* `mention` *object for a* `template_mention_user` *mention*

JSON

```
{
  "type": "mention",
  "mention": {
    "type": "template_mention",
    "template_mention": {
      "type": "template_mention_user",
      "template_mention_user": "me"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "@Me",
  "href": null
}
```

**User mention type object**

If a rich text object’s `type` value is `"user"`, then the corresponding user field contains a [__user object__](https://developers.notion.com/reference/user).

> ## **📘**
>
> If your integration doesn’t yet have access to the mentioned user, then the `plain_text` that would include a user’s name reads as `"@Anonymous"`. To update the integration to get access to the user, update the integration capabilities on the integration settings page.

*Example rich text* `mention` *object for a* `user` *mention*

JSON

```
{
  "type": "mention",
  "mention": {
    "type": "user",
    "user": {
      "object": "user",
      "id": "b2e19928-b427-4aad-9a9d-fde65479b1d9"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "@Anonymous",
  "href": null
}
```

### **Text**

If a rich text object’s `type` value is `"text"`, then the corresponding `text` field contains an object including the following:

**FieldTypeDescriptionExample value**`contentstring`The actual text content of the text.`"Some words "linkobject` (optional)An object with information about any inline link in this text, if included.

If the text contains an inline link, then the object key is `url` and the value is the URL’s string web address.

If the text doesn’t have any inline links, then the value is `null`.`{ "url": "https://developers.notion.com/" }`

**Example rich text **`text`** object without link**

JSON

```
{
  "type": "text",
  "text": {
    "content": "This is an ",
    "link": null
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "This is an ",
  "href": null
}
```

**Example rich **`text`** text object with link**

JSON

```
{
  "type": "text",
  "text": {
    "content": "inline link",
    "link": {
      "url": "https://developers.notion.com/"
    }
  },
  "annotations": {
    "bold": false,
    "italic": false,
    "strikethrough": false,
    "underline": false,
    "code": false,
    "color": "default"
  },
  "plain_text": "inline link",
  "href": "https://developers.notion.com/"
}
```

> ## **📘Rich text object limits**
>
> Refer to the request limits documentation page for information about [__limits on the size of rich text objects__](https://developers.notion.com/reference/request-limits#limits-for-property-values).

# **Page**

The Page object contains the [__page property values__](https://developers.notion.com/reference/page-property-values) of a single Notion page.

Example page object

```
{
    "object": "page",
    "id": "be633bf1-dfa0-436d-b259-571129a590e5",
    "created_time": "2022-10-24T22:54:00.000Z",
    "last_edited_time": "2023-03-08T18:25:00.000Z",
    "created_by": {
        "object": "user",
        "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
    },
    "last_edited_by": {
        "object": "user",
        "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf"
    },
    "cover": null,
    "icon": {
        "type": "emoji",
        "emoji": "🐞"
    },
    "parent": {
        "type": "data_source_id",
        "data_source_id": "a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b"
    },
    "archived": true,
    "in_trash": true,
    "properties": {
        "Due date": {
            "id": "M%3BBw",
            "type": "date",
            "date": {
                "start": "2023-02-23",
                "end": null,
                "time_zone": null
            }
        },
        "Status": {
            "id": "Z%3ClH",
            "type": "status",
            "status": {
                "id": "86ddb6ec-0627-47f8-800d-b65afd28be13",
                "name": "Not started",
                "color": "default"
            }
        },
        "Title": {
            "id": "title",
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "Bug bash",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "Bug bash",
                    "href": null
                }
            ]
        }
    },
    "url": "https://www.notion.so/Bug-bash-be633bf1dfa0436db259571129a590e5",
		"public_url": "https://jm-testing.notion.site/p1-6df2c07bfc6b4c46815ad205d132e22d"
}
```

All pages have a [__Parent__](https://developers.notion.com/reference/parent-object). If the parent is a [__data source__](https://developers.notion.com/reference/data-source), the property values conform to the schema laid out in the data source's [__properties__](https://developers.notion.com/reference/property-object). Otherwise, the only property value is the `title`.

Page content is available as [__blocks__](https://developers.notion.com/reference/block). The content can be read using [__retrieve block children__](https://developers.notion.com/reference/get-block-children) and appended using [__append block children__](https://developers.notion.com/reference/patch-block-children).

## **Page object properties**

> ## **📘**
>
> Properties marked with an * are available to integrations with any capabilities. Other properties require read content capabilities in order to be returned from the Notion API. For more information on integration capabilities, see the [__capabilities guide__](https://developers.notion.com/reference/capabilities).

**PropertyTypeDescriptionExample value**`object`*`string`Always `"page"`.`"page"id`*`string` (UUIDv4)Unique identifier of the page.`"45ee8d13-687b-47ce-a5ca-6e2e45548c4b"created_timestring` ([__ISO 8601 date and time__](https://en.wikipedia.org/wiki/ISO_8601))Date and time when this page was created. Formatted as an [__ISO 8601 date time__](https://en.wikipedia.org/wiki/ISO_8601) string.`"2020-03-17T19:10:04.968Z"created_by`[__Partial User__](https://developers.notion.com/reference/user)User who created the page.`{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}last_edited_timestring` ([__ISO 8601 date and time__](https://en.wikipedia.org/wiki/ISO_8601))Date and time when this page was updated. Formatted as an [__ISO 8601 date time__](https://en.wikipedia.org/wiki/ISO_8601) string.`"2020-03-17T19:10:04.968Z"last_edited_by`[__Partial User__](https://developers.notion.com/reference/user)User who last edited the page.`{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}archivedboolean`The archived status of the page.`falsein_trashboolean`Whether the page is in Trash.`falseicon`[__File Object__](https://developers.notion.com/reference/file-object) (`type` of `"external"` or `"file_upload"` are supported) or [__Emoji object__](https://developers.notion.com/reference/emoji-object)Page icon.`cover`[__File object__](https://developers.notion.com/reference/file-object) (`type` of `"external"` or `"file_upload"` are supported)Page cover image.`propertiesobject`Property values of this page. As of version `2022-06-28`, `properties` only contains the ID of the property; in prior versions `properties` contained the values as well.

If `parent.type` is `"page_id"` or `"workspace"`, then the only valid key is `title`.

If `parent.type` is `"data_source_id"`, then the keys and values of this field are determined by the `properties` of the [__data source__](https://developers.notion.com/reference/data-source) this page belongs to.

`key` string
Name of a property as it appears in Notion.

`value` object
See [__Property value object__](https://developers.notion.com/reference/property-value-object).`{ "id": "A%40Hk" }parentobject`Information about the page's parent. See [__Parent object__](https://developers.notion.com/reference/parent-object).`{ "type": "data_source_id", "data_source_id": "d9824bdc-8445-4327-be8b-5b47500af6ce" }urlstring`The URL of the Notion page.`"https://www.notion.so/Avocado-d093f1d200464ce78b36e58a3f0d8043"public_urlstring`The public page URL if the page has been published to the web. Otherwise, `null`.`"https://jm-testing.notion.site/p1-6df2c07bfc6b4c46815ad205d132e22d"1`

## **Overview**

A [__page object__](https://developers.notion.com/reference/page) is made up of page properties that contain data about the page.

When you send a request to [__Create a page__](https://developers.notion.com/reference/post-page), set the page properties in the `properties` object body parameter.

[__Retrieve a page__](https://developers.notion.com/reference/retrieve-a-page) surfaces the identifier, type, and value of a page’s properties.

[__Retrieve a page property item__](https://developers.notion.com/reference/retrieve-a-page-property) returns information about a single property ID. Especially for formulas, rollups, and relations, Notion recommends using this API to ensure you get an accurate, up-to-date property value that isn't truncating any results. Refer to [__Page property items__](https://developers.notion.com/reference/property-item-object) for specific API shape details when using this endpoint.

An [__Update page__](https://developers.notion.com/reference/patch-page) query modifies the page property values specified in the `properties` object body param.

> ## **👍Pages that live in a data source are easier to query and manage**
>
> **Page properties** are most useful when interacting with a page that is an entry in a data source, represented as a row in the Notion app UI.
>
> If a page is not part of a data source, then its only available property is its `title`.

## **Attributes**

Each page property value object contains the following fields:

**FieldTypeDescriptionExample value**`idstring`An underlying identifier for the property. Historically, this may be a UUID, but newer IDs are a short ID that's always URL-encoded in the API and in [__integration webhooks__](https://developers.notion.com/reference/webhooks).

`id` may be used in place of name when creating or updating pages.

`id` remains constant when the property name changes.`"f%5C%5C%3Ap"typestring` (enum)The type of the property in the page object. Possible type values are:

- `checkbox`
- `created_by`
- `created_time`
- `date`
- `email`
- `files`
- `formula`
- `last_edited_by`
- `last_edited_time`
- `multi_select`
- `number`
- `people`
- `phone_number`
- `relation`
- `rollup`
- `rich_text`
- `select`
- `status`
- `title`
- `url`
- `unique_id`
- `verification`Refer to specific type sections below for details on type-specific values.`"rich_text"checkbox`
`created_by`
`created_time`
`date`
`email`
`files`
`formula`
`last_edited_by`
`last_edited_time`
`multi_select`
`number`
`people`
`phone_number`
`relation`
`rollup`
`rich_text`
`select`
`status`
`title`
`url`
`unique_id`
`verificationobject`A type object that contains data specific to the page property type, including the page property value.

Refer to the [__type objects section__](https://developers.notion.com/reference/page-property-values#type-objects) for descriptions and examples of each type.`"checkbox": true`

> ## **📘Size limits for page property values**
>
> For information about size limitations for specific page property objects, refer to the [__limits for property values documentation__](https://developers.notion.com/reference/request-limits#limits-for-property-values).

When returned from the [__Retrieve page property item__](https://developers.notion.com/changelog/retrieve-page-property-values) API, there's an additional field, `object`, which is always the string `"property_item"`, as described in [__Page property items__](https://developers.notion.com/reference/property-item-object).

## **Type objects**

### **Checkbox**

**FieldTypeDescriptionExample value**`checkboxboolean`Whether the checkbox is checked (`true`) or unchecked (`false`).`true`

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a **`checkbox`** page property value**

JSON

```
{
  "properties": {
    "Task completed": {
      "checkbox": true
    }
  }
}
```

**Example **`checkbox`** page property value as returned in a GET page request**

JSON

```
{
  "Task completed": {
    "id": "ZI%40W",
    "type": "checkbox",
    "checkbox": true
  }
}
```

### **Created by**

**FieldTypeDescriptionExample value**`created_byobject`A [__user object__](https://developers.notion.com/reference/user) containing information about the user who created the page.

`created_by` can’t be updated.Refer to the example response objects below.

**Example **`created_by`** page property value as returned in a GET page request**

JSON

```
{
  "created_by": {
    "object": "user",
    "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
  }
}
```

### **Created time**

**FieldTypeDescriptionExample value**`created_timestring` ([__ISO 8601__](https://en.wikipedia.org/wiki/ISO_8601) date and time)The date and time that the page was created.

The `created_time` value can’t be updated.`"2022-10-12T16:34:00.000Z"`

**Example **`created_time`** page property value as returned in a GET page request**

JSON

```
{
  "Created time": {
    "id": "eB_%7D",
    "type": "created_time",
    "created_time": "2022-10-24T22:54:00.000Z"
  }
}
```

### **Date**

If the `type` of a page property value is `"date"`, then the property value contains a `"date"` object with the following fields:

**FieldTypeDescriptionExample value**`endstring` ([__ISO 8601__](https://en.wikipedia.org/wiki/ISO_8601) date and time)(Optional) A string representing the end of a date range.

If the value is `null`, then the date value is not a range.`"2020-12-08T12:00:00Z"startstring` ([__ISO 8601__](https://en.wikipedia.org/wiki/ISO_8601) date and time)A date, with an optional time.

If the `date` value is a range, then `start` represents the start of the range.`"2020-12-08T12:00:00Z”`

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a date page property value**

JSON

```
{
  "properties": {
    "Due date": {
      "date": {
        "start": "2023-02-23"
      }
    }
  }
}
```

**Example **`date`** page property value as returned in a GET page request**

JSON

```
{
  "Due date": {
    "id": "M%3BBw",
    "type": "date",
    "date": {
      "start": "2023-02-07",
      "end": null,
      "time_zone": null
    }
  }
}
```

### **Email**

**FieldTypeDescriptionExample value**`emailstring`A string describing an email address.`"ada@makenotion.com"`

**Example **`properties`** body param for a POST or PATCH page request that creates or updates an **`email`** page property value**

JSON

```
{
  "properties": {
    "Email": {
      "email": "ada@makenotion.com"
    }
  }
}
```

**Example **`email`** page property value as returned in a GET page request**

JSON

```
{
  "Email": {
    "id": "y%5C%5E_",
    "type": "email",
    "email": "ada@makenotion.com"
  }
}
```

### **Files**

**FieldTypeDescriptionExample value**`files`array of [__file objects__](https://developers.notion.com/reference/file-object)An array of objects containing information about the files.Refer to the example response objects below.

**Example creation or update of **`files`** property**

The following is an example `properties` body parameter for a `POST` or `PATCH` page request that creates or updates a `files` page property value.

When providing an `external` URL, the `name` parameter is required.

When providing a `file_upload`, the `name` is optional and defaults to the `filename` of the original [__File Upload__](https://developers.notion.com/reference/file-upload).

JSON

```
{
  "properties": {
    "Blueprint": {
      "files": [
        {
          "name": "Project Alpha blueprint",
          "external": {
            "url": "https://www.figma.com/file/g7eazMtXnqON4i280CcMhk/project-alpha-blueprint?node-id=0%3A1&t=nXseWIETQIgv31YH-1"
          }
        }
      ]
    }
  }
}
```

**Example **`files`** page property value as returned in a GET page request**

JSON

```
{
  "Blueprint": {
    "id": "tJPS",
    "type": "files",
    "files": [
      {
        "name": "Project blueprint",
        "type": "external",
        "external": {
          "url": "https://www.figma.com/file/g7eazMtXnqON4i280CcMhk/project-alpha-blueprint?node-id=0%3A1&t=nXseWIETQIgv31YH-1"
        }
      }
    ]
  }
}
```

> ## **📘Array parameter overwrites the entire existing value**
>
> When updating a `files` page property value, the value is overwritten by the new array of `files` passed.
>
> If you pass a `file` object containing a file hosted by Notion, it remains one of the files. To remove any file, don't pass it in the update request.

### **Formula**

Formula property value objects represent the result of evaluating a formula described in the
[__data source's properties__](https://developers.notion.com/reference/data%20source).

If the `type` of a page property value is `"formula"`, then the property value contains a `"formula"` object with the following fields:

**FieldTypeDescriptionExample value**`boolean` || `date` || `number` || `stringboolean` || `date` || `number` || `string`The value of the result of the formula.

The value can’t be updated directly via the API.42`typestring` (enum)A string indicating the data type of the result of the formula. Possible `type` values are:

- `boolean`
- `date`
- `number`
- `string"number"`

**Example **`formula`** page property value as returned in a GET page request**

JSON

```
{
  "Days until launch": {
    "id": "CSoE",
    "type": "formula",
    "formula": {
      "type": "number",
      "number": 56
    }
  }
}
```

> ## **📘**
>
> The [__Retrieve a page endpoint__](https://developers.notion.com/reference/retrieve-a-page) returns a maximum of 25 inline page or person references for a `formula` property. If a `formula` property includes more than 25 references, then you can use the [__Retrieve a page property item endpoint__](https://developers.notion.com/reference/retrieve-a-page-property) for the specific `formula` property to get its complete list of references.

### **Icon**

> ## **📘Page icon and cover are not nested under **`properties`
>
> The `icon` and `cover` parameters and fields in the [__Create a page__](https://developers.notion.com/reference/post-page) and [__Update page properties__](https://developers.notion.com/reference/patch-page) APIs are top-level are not nested under `properties`.

**FieldTypeDescriptionExample value**`icon`an objectIcon objectRefer to the example response objects below.

**Example emoji **`icon`** property value as returned in GET page request**

JSON

```
{
  "icon": {
    "type": "emoji",
    "emoji":"😀"
  }
}
```

**Example uploaded **`icon`** page property value as returned in a GET page request**

JSON

```
{
  "icon": {
    "type":"file",
    "file": {
      "url": "https://local-files-secure.s3.us-west-2.amazonaws.com/13950b26-c203-4f3b-b97d-93ec06319565/a7084c4c-3e9a-4324-af99-34e0cb7f8fe7/notion.jpg?...",
      "expiry_time": "2024-12-03T19:44:56.932Z"
    }
  }
}
```

**Example updating a page icon to an uploaded file**

After uploading an image using the [__File Upload API__](https://developers.notion.com/reference/file-upload#file-types-and-sizes), use the File Upload's ID in the [__Create a page__](https://developers.notion.com/reference/post-page) or [__Update page properties__](https://developers.notion.com/reference/patch-page) API to attach it as a page icon. For example:

JSON

```
{
  "icon": {
    "type": "file_upload",
    "file_upload": {
      "id": "43833259-72ae-404e-8441-b6577f3159b4"
    }
  }
}
```

To attach a file upload as a page cover rather than an icon, use the create or update page APIs with the `cover` parameter, nesting a `file_upload` parameter the same way as the `icon` example.

### **Last edited by**

**FieldTypeDescriptionExample value**`last_edited_byobject`A [__user object__](https://developers.notion.com/reference/user) containing information about the user who last updated the page.

`last_edited_by` can’t be updated.Refer to the example response objects below.

**Example **`last_edited_by`** page property value as returned in a GET page request**

JSON

```
{
  "Last edited by column name": {
    "id": "uGNN",
    "type": "last_edited_by",
    "last_edited_by": {
      "object": "user",
      "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf",
      "name": "Test Integration",
      "avatar_url": "https://s3-us-west-2.amazonaws.com/public.notion-static.com/3db373fe-18f6-4a3c-a536-0f061cb9627f/leplane.jpeg",
      "type": "bot",
      "bot": {}
    }
  }
}
```

### **Last edited time**

**FieldTypeDescriptionExample value**`last_edited_timestring` ([__ISO 8601__](https://en.wikipedia.org/wiki/ISO_8601) date and time)The date and time that the page was last edited.

The `last_edited_time` value can’t be updated.`"2022-10-12T16:34:00.000Z"`

**Example **`last_edited_time`** page property value as returned in a GET page request**

JSON

```
{
  "Last edited time": {
    "id": "%3Defk",
    "type": "last_edited_time",
    "last_edited_time": "2023-02-24T21:06:00.000Z"
  } 
}
```

### **Multi-select**

If the `type` of a page property value is `"multi_select"`, then the property value contains a `"multi_select"` array with the following fields:

**FieldTypeDescriptionExample value**`colorstring` (enum)Color of the option. Possible `"color"` values are: 

- `blue`
- `brown`
- `default`
- `gray`
- `green`
- `orange`
- `pink"`
- `"purple`
- `red`
- `yellow`Defaults to `default`. The `color` value can’t be updated via the API.`"red"idstring`The ID of the option.

You can use `id` or `name` to update a multi-select property.`"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"namestring`The name of the option as it appears in Notion.

If the multi-select [__data source property__](https://developers.notion.com/reference/property-object) does not yet have an option by that name, then the name will be added to the data source schema if the integration also has write access to the parent data source.

Note: Commas (`","`) are not valid for select values.`"JavaScript"`

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a **`multi_select`** page property value**

JSON

```
{
  "properties": {
    "Programming language": {
      "multi_select": [
        {
          "name": "TypeScript"
        },
        {
          "name": "Python"
        }
      ]
    }
  }
}
```

**Example **`multi_select`** page property value as returned in a GET page request**

JSON

```
{
  "Programming language": {
    "id": "QyRn",
    "name": "Programming language",
    "type": "multi_select",
    "multi_select": [
      {
        "id": "tC;=",
        "name": "TypeScript",
        "color": "purple"
      },
      {
        "id": "e4413a91-9f84-4c4a-a13d-5b4b3ef870bb",
        "name": "JavaScript",
        "color": "red"
      },
      {
        "id": "fc44b090-2166-40c8-8c58-88f2d8085ec0",
        "name": "Python",
        "color": "gray"
      }
    ]
  }
}
```

> ## **📘**
>
> If you want to add a new option to a multi-select property via the [__Update page__](https://developers.notion.com/reference/patch-page) or [__Update data source__](https://developers.notion.com/reference/update-a-data-source) endpoint, then your integration needs write access to the parent database.

### **Number**

**FieldTypeDescriptionExample value**`numbernumber`A number representing some value.`1234`

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a **`number`** page property value**

JSON

```
{
  "properties": {
    "Number of subscribers": {
      "number": 42
    }
  }
}
```

**Example **`number`** page property value as returned in a GET page request**

JSON

```
{
  "Number of subscribers": {
    "id": "WPj%5E",
    "name": "Number of subscribers",
    "type": "number",
    "number": {
      "format": "number"
    }
  }
}
```

### **People**

**FieldTypeDescriptionExample value**`people`array of [__user objects__](https://developers.notion.com/reference/user)An array of user objects.Refer to the example response objects below.

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a **`people`** page property value**

JSON

```
{
  "properties": {
    "Stakeholders": {
      "people": [{
        "object": "user",
        "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
      }]
    }
  }
}
```

**Example **`people`** page property value as returned in a GET page request**

JSON

```
{
  "Stakeholders": {
    "id": "%7BLUX",
    "type": "people",
    "people": [
      {
        "object": "user",
        "id": "c2f20311-9e54-4d11-8c79-7398424ae41e",
        "name": "Kimberlee Johnson",
        "avatar_url": null,
        "type": "person",
        "person": {
          "email": "hello@kimberlee.dev"
        }
      }
    ]
  }
}
```

> ## **📘Retrieve individual property items to avoid truncation**
>
> The [__Retrieve a page endpoint__](https://developers.notion.com/reference/retrieve-a-page) can’t be guaranteed to return more than 25 people per `people` page property. If a `people` page property includes more than 25 people, then you can use the [__Retrieve a page property item endpoint__](https://developers.notion.com/reference/retrieve-a-page-property) for the specific `people` property to get a complete list of people.

### **Phone number**

**FieldTypeDescriptionExample value**`phone_numberstring`A string representing a phone number. No phone number format is enforced.`"415-867-5309"`

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a **`phone_number`** page property value**

JSON

```
{
  "properties": {
    "Contact phone number": {
      "phone_number": "415-202-4776"
    }
  }
}
```

**Example **`phone_number`** page property value as returned in a GET page request**

JSON

```
{
  "Example phone number property": {
    "id": "%5DKhQ",
    "name": "Example phone number property",
    "type": "phone_number",
    "phone_number": {}
  }
}
```

### **Relation**

**FieldTypeDescriptionExample value**`has_moreboolean`If a `relation` has more than 25 references, then the `has_more` value for the relation in the response object is `true`. If a relation doesn’t exceed the limit, then `has_more` is `false`.Refer to the example response objects below.`relation`an array of page referencesAn array of related page references. A page reference is an object with an `id` key and a string value corresponding to a page ID in another data source.Refer to the example response objects below.

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a **`relation`** page property value**

JSON

```
{
  "properties": {
    "Related tasks": {
      "relation": [
        {
          "id": "dd456007-6c66-4bba-957e-ea501dcda3a6"
        },
        {
          "id": "0c1f7cb2-8090-4f18-924e-d92965055e32"
        }
      ]
    }
  }
}
```

**Example **`relation`** page property value as returned in a GET page request**

JSON

```
{
  "Related tasks": {
    "id": "hgMz",
    "type": "relation",
    "relation": [
      {
        "id": "dd456007-6c66-4bba-957e-ea501dcda3a6"
      },
      {
        "id": "0c1f7cb2-8090-4f18-924e-d92965055e32"
      }
    ],
    "has_more": false
  } 
}
```

> ## **📘To update a **`relation`** property value via the API, share the related parent database with the integration.**
>
> If a `relation` property value is unexpectedly empty, then make sure that you have shared the original source database for the data source that the `relation` points to with the integration.
>
> Ensuring correct permissions is also important for complete results for `rollup` and `formula` properties.

### **Rollup**

If the `type` of a page property value is `"rollup"`, then the property value contains a `"rollup"` object with the following fields:

**FieldTypeDescriptionExample value**`array` || `date` || `incomplete` || `number` || `unsupported`Corresponds to the field.

For example, if the field is `number`, then the type of the value is `number`.The value of the calculated rollup.

The value can't be directly updated via the API.`1234functionstring` (enum)The function that is evaluated for every page in the relation of the rollup. Possible `"function"` values are:

- `average`
- `checked`
- `count`
- `count_per_group`
- `count_values`
- `date_range`
- `earliest_date`
- `empty`
- `latest_date`
- `max`
- `median`
- `min`
- `not_empty`
- `percent_checked`
- `percent_empty`
- `percent_not_empty`
- `percent_per_group`
- `percent_unchecked`
- `range`
- `show_original`
- `show_unique`
- `sum`
- `unchecked`
- `unique"sum"typearray` || `date` || `incomplete` || `number` || `unsupported`The value type of the calculated rollup.`number`

**Example **`rollup`** page property value as returned in a GET page request**

JSON

```
{
  "Number of units": {
    "id": "hgMz",
    "type": "rollup",
    "rollup": {
      "type": "number",
      "number": 2,
      "function": "count"
    }
  }
}
```

> ## **🚧For rollup properties with more than 25 references, use the Retrieve a page property endpoint**
>
> Both the [__Retrieve a page__](https://developers.notion.com/reference/retrieve-a-page) and [__Retrieve a page property__](https://developers.notion.com/reference/retrieve-a-page-property) endpoints will return information related to the page properties. In cases where a rollup property has more than 25 references, the [__Retrieve a page property__](https://developers.notion.com/reference/retrieve-a-page-property) endpoint must but used.
>
> Learn more about rollup properties in Notion’s [__Help Center__](https://developers.notion.com/reference/page-property-values#rollup).

> ## **🚧The API does not support updating **`rollup`** page property values.**
>
> To change a page's `rollup` property, use the Notion UI.

### **Rich text**

**FieldTypeDescriptionExample value**`rich_text`an array of [__rich text objects__](https://developers.notion.com/reference/rich-text)An array of [__rich text objects__](https://developers.notion.com/reference/rich-text)Refer to the example response objects below.

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a **`rich_text`** page property value**

JSON

```
{
  "properties": {
    "Description": {
      "rich_text": [
        {
          "type": "text",
          "text": {
            "content": "There is some ",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "There is some ",
          "href": null
        },
        {
          "type": "text",
          "text": {
            "content": "text",
            "link": null
          },
          "annotations": {
            "bold": true,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "text",
          "href": null
        },
        {
          "type": "text",
          "text": {
            "content": " in this property!",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": " in this property!",
          "href": null
        }
      ]
    }
  }
}
```

**Example **`rich_text`** page property value as returned in a GET page request**

JSON

```
{
  "Description": {
    "id": "HbZT",
    "type": "rich_text",
    "rich_text": [
      {
        "type": "text",
        "text": {
          "content": "There is some ",
          "link": null
        },
        "annotations": {
          "bold": false,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": "There is some ",
        "href": null
      },
      {
        "type": "text",
        "text": {
          "content": "text",
          "link": null
        },
        "annotations": {
          "bold": true,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": "text",
        "href": null
      },
      {
        "type": "text",
        "text": {
          "content": " in this property!",
          "link": null
        },
        "annotations": {
          "bold": false,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": " in this property!",
        "href": null
      }
    ]
  } 
}
```

> ## **📘**
>
> The [__Retrieve a page endpoint__](https://developers.notion.com/reference/retrieve-a-page) returns a maximum of 25 populated inline page or person references for a `rich_text` property. If a `rich_text` property includes more than 25 references, then you can use the [__Retrieve a page property item endpoint__](https://developers.notion.com/reference/retrieve-a-page-property) for the specific `rich_text` property to get its complete list of references.

### **Select**

If the type of a page property value is `select`, then the property value contains a `select` object with the following fields:

**PropertyTypeDescriptionExample value**`colorstring` (enum)The color of the option. Possible `"color"` values are: 

- `blue`
- `brown`
- `default`
- `gray`
- `green`
- `orange`
- `pink`
- `purple`
- `red`
- yellow`Defaults to `default`. The `color` value can’t be updated via the API.`redidstring`The ID of the option.

You can use `id` or `name` to [__update__](https://developers.notion.com/reference/patch-page) a select property.`"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"namestring`The name of the option as it appears in Notion.

If the select [__data source property__](https://developers.notion.com/reference/property-object) doesn't have an option by that name yet, then the name is added to the data source schema if the integration also has write access to the parent data source.

Note: Commas (`","`) are not valid for select values.`"jQuery"`

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a **`select`** page property value**

JSON

```
{
  "properties": {
    "Department": {
      "select": {
        "name": "Marketing"
      }
    }
  }
}
```

**Example select page property value as returned in a GET page request**

JSON

```
{
  "Department": {
    "id": "Yc%3FJ",
    "type": "select",
    "select": {
      "id": "ou@_",
      "name": "jQuery",
      "color": "purple"
    }
  }
}
```

### **Status**

If the type of a page property value is `status`, then the property value contains a `status` object with the following fields:

**PropertyTypeDescriptionExample value**`colorstring` (enum)The color of the option. Possible `"color"` values are: 

- `blue`
- `brown`
- `default`
- `gray`
- `green`
- `orange`
- `pink`
- `purple`
- `red`
- `yellow`Defaults to `default`. The `color` value can’t be updated via the API.`"red"idstringstring"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"namestring`The name of the option as it appears in Notion.`"In progress"`

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a **`status`** page property value**

JSON

```
{
  "properties": {
    "Status": {
      "status": {
        "name": "Not started"
      }
    }
  }
}
```

**Example **`status`** page property value as returned in a GET page request**

JSON

```
{
  "Status": {
    "id": "Z%3ClH",
    "type": "status",
    "status": {
      "id": "539f2705-6529-42d8-a215-61a7183a92c0",
      "name": "In progress",
      "color": "blue"
    }
  }
}
```

### **Title**

**FieldTypeDescriptionExample value**`title`an array of [__rich text objects__](https://developers.notion.com/reference/rich-text)An array of [__rich text objects__](https://developers.notion.com/reference/rich-text).Refer to the example response objects below.

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a **`title`** page property value**

JSON

```
{
  "properties": {
    "Title": {
      "id": "title",
      "type": "title",
      "title": [
        {
          "type": "text",
          "text": {
            "content": "A better title for the page",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "This is also not done",
          "href": null
        }
      ]
    }
  }
}
```

**Example **`title`** page property value as returned in a GET page request**

JSON

```
{
  "Title": {
    "id": "title",
    "type": "title",
    "title": [
      {
        "type": "text",
        "text": {
          "content": "A better title for the page",
          "link": null
        },
        "annotations": {
          "bold": false,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": "This is also not done",
        "href": null
      }
    ]
  }
}
```

> ## **📘**
>
> The [__Retrieve a page endpoint__](https://developers.notion.com/reference/retrieve-a-page) returns a maximum of 25 inline page or person references for a `title` property. If a `title` property includes more than 25 references, then you can use the [__Retrieve a page property item endpoint__](https://developers.notion.com/reference/retrieve-a-page-property) for the specific `title` property to get its complete list of references.

### **URL**

**FieldTypeDescriptionExample value**`urlstring`A string that describes a web address.`"https://developers.notion.com/"`

**Example **`properties`** body param for a POST or PATCH page request that creates or updates a **`url`** page property value**

JSON

```
{
  "properties": {
    "Website": {
      "url": "https://developers.notion.com/"
    }
  }
}
```

**Example **`url`** page property value as returned in a GET page request**

JSON

```
{
  "Website": {
    "id": "bB%3D%5B",
    "type": "url",
    "url": "https://developers.notion.com/"
  }
}
```

### **Unique ID**

**FieldTypeDescriptionExample value**`numbernumber`The ID count (auto-incrementing).3`prefixstring` or `null`An optional prefix to be applied to the unique ID."RL"

> ## **👍**
>
> Unique IDs can be read using the API with a [__GET page__](https://developers.notion.com/reference/retrieve-a-page) request, but they cannot be updated with the API, since they are auto-incrementing.

**Example **`url`** page property value as returned in a GET page request**

JSON

```
{
  "test-ID": {
    "id": "tqqd",
    "type": "unique_id",
    "unique_id": {
      "number": 3,
      "prefix": "RL",
    },
  },
}
```

### **Verification**

The verification status of a page in a wiki database. Pages can be verified or unverified, and verifications can have an optional expiration date set.

The verification status cannot currently be set or updated via the public API.

> ## **📘**
>
> The `verification` property is only available for pages that are part of a [__wiki database__](https://developers.notion.com/docs/working-with-databases#wiki-databases). To learn more about wiki databases and verifying pages, see our [__Help Center article__](https://www.notion.so/help/wikis-and-verified-pages#verifying-pages).

**FieldTypeDescriptionExample value**`statestring`The verification state of the page. `"verified"` or `"unverified"`.`"unverified"verified_by`[__User__](https://developers.notion.com/reference/user) object or `null`If the page if verified, a [__User__](https://developers.notion.com/reference/user) object will be included to indicate the user who verified the page.Refer to the example response objects below.`date`Object or `null`If the page is verified, the date object will include the date the verification started (`start`). If an expiration date is set for the verification, an end date (`end`) will be included. ([__ISO 8601__](https://en.wikipedia.org/wiki/ISO_8601) date and time.)Refer to the example response objects below.

**Example **`verification`** page property values as returned in a GET page request**

**Unverified**

JSON

```
{
  Verification: {
    id: "fpVq",
    type: "verification",
    verification: { state: "unverified", verified_by: null, date: null },
  },
}
```

**Verified with no expiration date set**

JSON

```
{
  Verification: {
    id: "fpVq",
    type: "verification",
    verification: {
      state: "verified",
      verified_by: {
        object: "user",
        id: "01e46064-d5fb-4444-8ecc-ad47d076f804",
        name: "User Name",
        avatar_url: null,
        type: "person",
        person: {},
      },
      date: { start: "2023-08-01T04:00:00.000Z", end: null, time_zone: null },
    },
  },
}
```

**Verified with 90-day expiration date**

JSON

```
{
  Verification: {
    id: "fpVq",
    type: "verification",
    verification: {...},
      date: {
        start: "2023-08-01T04:00:00.000Z",
        end: "2023-10-30T04:00:00.000Z",
        time_zone: null,
      },
    },
  },
}
```

## **Paginated page properties**

The `title`, `rich_text`, `relation` and `people` page properties are returned as a paginated `list` object of individual `property_item` objects.

An abridged set of the the properties found in the `list` object is below. Refer to the [__pagination documentation__](https://developers.notion.com/reference/intro#pagination) for additional information.

**FieldTypeDescriptionExample value**`object"list"`Always `"list"`.`"list"type"property_item"`Always `"property_item"`.`"property_item"resultslist`List of `property_item` objects.`[{"object": "property_item", "id": "vYdV", "type": "relation", "relation": { "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"}}... ]property_itemobject`A `property_item` object that describes the property.`{"id": "title", "next_url": null, "type": "title", "title": {}}next_urlstring` or `null`The URL the user can request to get the next page of results.`"http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/vYdV?start_cursor=LYxaUO&page_size=25"`

# **Page property items**

## **Overview**

A `property_item` object describes the identifier, type, and value of a page property. It's returned from the [__Retrieve a page property item__](https://developers.notion.com/reference/retrieve-a-page-property) API.

Generally, the details on this page are the same as those in [__Page properties__](https://developers.notion.com/reference/page-property-values), but with tweaks and additional information specific to the retrieve page property item endpoint, such as [__value pagination__](https://developers.notion.com/reference/property-item-object#paginated-property-values) .

## **Common fields**

Each page property item object contains the following keys. In addition, it will contain a key corresponding with the value of `type`. The value is an object containing type-specific data. The type-specific data are described in the sections below.

**PropertyTypeDescriptionExample value**`object"property_item"`Always `"property_item"`.`"property_item"idstring`Underlying identifier for the property. This identifier is guaranteed to remain constant when the property name changes. It may be a UUID, but is often a short random string.

The `id` may be used in place of `name` when creating or updating pages.`"f%5C%5C%3Ap"typestring` (enum)Type of the property. Possible values are `"rich_text"`, `"number"`, `"select"`, `"multi_select"`, `"date"`, `"formula"`, `"relation"`, `"rollup"`, `"title"`, `"people"`, `"files"`, `"checkbox"`, `"url"`, `"email"`, `"phone_number"`, `"created_time"`, `"created_by"`, `"last_edited_time"`, and `"last_edited_by"`.`"rich_text"`

## **Paginated values**

The `title`[__, __](https://developers.notion.com/reference/retrieve-a-page-property#paginated-properties)`rich_text`[__, __](https://developers.notion.com/reference/retrieve-a-page-property#paginated-properties)`relation`[__ and __](https://developers.notion.com/reference/retrieve-a-page-property#paginated-properties)`people` property items of are returned as a paginated `list` object of individual `property_item` objects in the results. An abridged set of the the properties found in the `list` object are found below; see the [__Pagination__](https://developers.notion.com/reference/pagination) documentation for additional information.

**PropertyTypeDescriptionExample value**`object"list"`Always `"list"`.`"list"type"property_item"`Always `"property_item"`.`"property_item"resultslist`List of `property_item` objects.`[{"object": "property_item", "id": "vYdV", "type": "relation", "relation": { "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"}}... ]property_itemobject`A `property_item` object that describes the property.`{"id": "title", "next_url": null, "type": "title", "title": {}}next_urlstring` or `null`The URL the user can request to get the next page of results.`"http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/vYdV?start_cursor=LYxaUO&page_size=25"`

## **Title**

Title property value objects contain an array of [__rich text objects__](https://developers.notion.com/reference/rich-text) within the `title` property.

Title property value

```
{
  "Name": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "title",
        "type": "title",
        "title": {
          "type": "text",
          "text": {
            "content": "The title",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "The title",
          "href": null
        }
      }
    ],
    "next_cursor": null,
    "has_more": false,
    "type": "property_item",
    "property_item": {
      "id": "title",
      "next_url": null,
      "type": "title",
      "title": {}
    }
  }
}
```

## **Rich text**

Rich text property value objects contain an array of [__rich text objects__](https://developers.notion.com/reference/rich-text) within the `rich_text` property.

Rich text property value

```
{
  "Details": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "NVv%5E",
        "type": "rich_text",
        "rich_text": {
          "type": "text",
          "text": {
            "content": "Some more text with ",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "Some more text with ",
          "href": null
        }
      },
      {
        "object": "property_item",
        "id": "NVv%5E",
        "type": "rich_text",
        "rich_text": {
          "type": "text",
          "text": {
            "content": "fun formatting",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": true,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "fun formatting",
          "href": null
        }
      }
    ],
    "next_cursor": null,
    "has_more": false,
    "type": "property_item",
    "property_item": {
      "id": "NVv^",
      "next_url": null,
      "type": "rich_text",
      "rich_text": {}
    }
  }
}
```

## **Number**

Number property value objects contain a number within the `number` property.

Number property value

```
{
  "Quantity": {
    "object": "property_item",
    "id": "XpXf",
    "type": "number",
    "number": 1234
  }
}
```

## **Select**

Select property value objects contain the following data within the `select` property:

**PropertyTypeDescriptionExample value**`idstring` (UUIDv4)ID of the option.

When updating a select property, you can use either `name` or `id`.`"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"namestring`Name of the option as it appears in Notion.

If the select [__database property__](https://developers.notion.com/reference/property-object) does not yet have an option by that name, it will be added to the database schema if the integration also has write access to the parent database.

Note: Commas (",") are not valid for select values.`"Fruit"colorstring` (enum)Color of the option. Possible values are: `"default"`, `"gray"`, `"brown"`, `"red"`, `"orange"`, `"yellow"`, `"green"`, `"blue"`, `"purple"`, `"pink"`. Defaults to `"default"`.

Not currently editable.`"red"`

Select property value

```
{
  "Option": {
    "object": "property_item",
    "id": "%7CtzR",
    "type": "select",
    "select": {
      "id": "64190ec9-e963-47cb-bc37-6a71d6b71206",
      "name": "Option 1",
      "color": "orange"
    }
  }
}
```

## **Multi-select**

Multi-select property value objects contain an array of multi-select option values within the `multi_select` property.

### **Option values**

**PropertyTypeDescriptionExample value**`idstring` (UUIDv4)ID of the option.

When updating a multi-select property, you can use either `name` or `id`.`"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"namestring`Name of the option as it appears in Notion.

If the multi-select [__database property__](https://developers.notion.com/reference/property-object) does not yet have an option by that name, it will be added to the database schema if the integration also has write access to the parent database.

Note: Commas (",") are not valid for select values.`"Fruit"colorstring` (enum)Color of the option. Possible values are: `"default"`, `"gray"`, `"brown"`, `"red"`, `"orange"`, `"yellow"`, `"green"`, `"blue"`, `"purple"`, `"pink"`. Defaults to `"default"`.

Not currently editable.`"red"`

Multi-select property value

```
{
  "Tags": {
    "object": "property_item",
    "id": "z%7D%5C%3C",
    "type": "multi_select",
    "multi_select": [
      {
        "id": "91e6959e-7690-4f55-b8dd-d3da9debac45",
        "name": "A",
        "color": "orange"
      },
      {
        "id": "2f998e2d-7b1c-485b-ba6b-5e6a815ec8f5",
        "name": "B",
        "color": "purple"
      }
    ]
  }
}
```

## **Date**

Date property value objects contain the following data within the `date` property:

**PropertyTypeDescriptionExample value**`start`string ([__ISO 8601 date and time__](https://en.wikipedia.org/wiki/ISO_8601))An ISO 8601 format date, with optional time.`"2020-12-08T12:00:00Z"end`string (optional, [__ISO 8601 date and time__](https://en.wikipedia.org/wiki/ISO_8601))An ISO 8601 formatted date, with optional time. Represents the end of a date range.

If `null`, this property's date value is not a range.`"2020-12-08T12:00:00Z"time_zone`string (optional, enum)Time zone information for `start` and `end`. Possible values are extracted from the [__IANA database__](https://www.iana.org/time-zones) and they are based on the time zones from [__Moment.js__](https://momentjs.com/timezone/).

When time zone is provided, `start` and `end` should not have any [__UTC offset__](https://en.wikipedia.org/wiki/UTC_offset). In addition, when time zone is provided, `start` and `end` cannot be dates without time information.

If `null`, time zone information will be contained in [__UTC offset__](https://en.wikipedia.org/wiki/UTC_offset)s in `start` and `end`.`"America/Los_Angeles"`

Date property value

```
{
  "Shipment Time": {
    "object": "property_item",
    "id": "i%3Ahj",
    "type": "date",
    "date": {
      "start": "2021-05-11T11:00:00.000-04:00",
      "end": null,
      "time_zone": null
    }
  }
}
```

## **Formula**

Formula property value objects represent the result of evaluating a formula described in the
[__database's properties__](https://developers.notion.com/reference/property-object). These objects contain a `type` key and a key corresponding with the value of `type`. The value is an object containing type-specific data. The type-specific data are described in the sections below.

**PropertyTypeDescription**`typestring` (enum)The type of the formula result. Possible values are `"string"`, `"number"`, `"boolean"`, and `"date"`.

### **String formula**

String formula property values contain an optional string within the `string` property.

### **Number formula**

Number formula property values contain an optional number within the `number` property.

### **Boolean formula**

Boolean formula property values contain a boolean within the `boolean` property.

### **Date formula**

Date formula property values contain an optional [__date property value__](https://developers.notion.com/reference/property-item-object#date-property-values) within the `date` property.

Formula Property Value

```
{
  "Formula": {
    "object": "property_item",
    "id": "KpQq",
    "type": "formula",
    "formula": {
      "type": "number",
      "number": 1234
    }
  }
}
```

## **Relation**

Relation property value objects contain an array of `relation` property items with page references within the `relation` property. A page reference is an object with an `id` property which is a string value (UUIDv4) corresponding to a page ID in another database.

Relation property value

```
{
  "Project": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "vYdV",
        "type": "relation",
        "relation": {
          "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"
        }
      }
    ],
    "next_cursor": null,
    "has_more": true,
    "type": "property_item",
    "property_item": {
      "id": "vYdV",
      "next_url": null,
      "type": "relation",
      "relation": {}
    }
  }
}
```

## **Rollup**

Rollup property value objects represent the result of evaluating a rollup described in the
[__data source's properties__](https://developers.notion.com/reference/property-object). The property is returned as a `list` object of type `property_item` with a list of `relation` items used to computed the rollup under `results`.

A `rollup` property item is also returned under the `property_type` key that describes the rollup aggregation and computed result.

In order to avoid timeouts, if the rollup has a with a large number of aggregations or properties the endpoint returns a `next_cursor` value that is used to determinate the aggregation value *so far* for the subset of relations that have been paginated through.

Once `has_more` is `false`, then the final rollup value is returned. See the [__Pagination documentation__](https://developers.notion.com/reference/pagination) for more information on pagination in the Notion API.

Computing the values of following aggregations are *not* supported. Instead the endpoint returns a list of `property_item` objects for the rollup:
- `show_unique` (Show unique values)
- `unique` (Count unique values)
- `median`(Median)

**PropertyTypeDescription**`typestring` (enum)The type of rollup. Possible values are `"number"`, `"date"`, `"array"`, `"unsupported"` and `"incomplete"`.`functionstring` (enum)Describes the aggregation used.
Possible values include: `count`, `count_values`, `empty`, `not_empty`, `unique`, `show_unique`, `percent_empty`, `percent_not_empty`, `sum`, `average`, `median`, `min`, `max`, `range`, `earliest_date`, `latest_date`, `date_range`, `checked`, `unchecked`, `percent_checked`, `percent_unchecked`, `count_per_group`, `percent_per_group`, `show_original`

### **Number rollup**

Number rollup property values contain a number within the `number` property.

### **Date rollup**

Date rollup property values contain a [__date property value__](https://developers.notion.com/reference/property-item-object#date-property-values) within the `date` property.

### **Array rollup**

Array rollup property values contain an array of `property_item` objects within the `results` property.

### **Incomplete rollup**

Rollups with an aggregation with more than one page of aggregated results will return a `rollup` object of type `"incomplete"`. To obtain the final value paginate through the next values in the rollup using the `next_cursor` or `next_url` property.

Rollup Property Value

```
{
  "Rollup": {
    "object": "list",
    "results": [
      {
        "object": "property_item",
        "id": "vYdV",
        "type": "relation",
        "relation": {
          "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"
        }
      }...
    ],	
    "next_cursor": "1QaTunT5",
    "has_more": true,
    "type": "property_item",
    "property_item": {
      "id": "y}~p",
      "next_url": "http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/y%7D~p?start_cursor=1QaTunT5&page_size=25",
      "type": "rollup",
      "rollup": {
        "function": "sum",
        "type": "incomplete",
        "incomplete": {}
      }
    }
  }
}
```

## **People**

People property value objects contain an array of [__user objects__](https://developers.notion.com/reference/user) within the `people` property.

People property value

```
{
  "Owners": {
    "object": "property_item",
    "id": "KpQq",
    "type": "people",
    "people": [
      {
        "object": "user",
        "id": "285e5768-3fdc-4742-ab9e-125f9050f3b8",
        "name": "Example Avo",
        "avatar_url": null,
        "type": "person",
        "person": {
          "email": "avo@example.com"
        }
      }
    ]
  }
}
```

## **Files**

File property value objects contain an array of file references within the `files` property. A file reference is an object with a [__File Object__](https://developers.notion.com/reference/file-object) and `name` property, with a string value corresponding to a filename of the original file upload (e.g. `"Whole_Earth_Catalog.jpg"`).

JSON

```
{
  "Files": {
    "object": "property_item",
    "id": "KpQq",
    "type": "files",
    "files": [
      {
        "type": "external",
        "name": "Space Wallpaper",
        "external": "https://website.domain/images/space.png"
      }
    ]
  }
}
```

## **Checkbox**

Checkbox property value objects contain a boolean within the `checkbox` property.

Checkbox property value

```
{
  "Done?": {
    "object": "property_item",
    "id": "KpQq",
    "type": "checkbox",
    "checkbox": true
  }
}
```

## **URL**

URL property value objects contain a non-empty string within the `url` property. The string describes a web address (i.e. `"http://worrydream.com/EarlyHistoryOfSmalltalk/"`).

URL property value

```
{
  "Website": {
    "object": "property_item",
    "id": "KpQq",
    "type": "url",
    "url": "https://notion.so/notiondevs"
  }
}
```

## **Email**

Email property value objects contain a string within the `email` property. The string describes an email address (i.e. `"hello@example.org"`).

Email property value

```
{
  "Shipper's Contact": {
    "object": "property_item",
    "id": "KpQq",
    "type": "email",
    "email": "hello@test.com"
  }
}
```

## **Phone number**

Phone number property value objects contain a string within the `phone_number` property. No structure is enforced.

Phone number property value

```
{
  "Shipper's No.": {
    "object": "property_item",
    "id": "KpQq",
    "type": "phone_number",
    "phone_number": "415-000-1111"
  }
}
```

## **Created time**

Created time property value objects contain a string within the `created_time` property. The string contains the date and time when this page was created. It is formatted as an [__ISO 8601__](https://en.wikipedia.org/wiki/ISO_8601) date time string (i.e. `"2020-03-17T19:10:04.968Z"`).

Created time property value

```
{
  "Created Time": {
    "object": "property_item",
    "id": "KpQq",
    "type": "create_time",
  	"created_time": "2020-03-17T19:10:04.968Z"
  }
}
```

## **Created by**

Created by property value objects contain a [__user object__](https://developers.notion.com/reference/user) within the `created_by` property. The user object describes the user who created this page.

Created by property valueCreated by property value (using ID)

```
{
  "Created By": {
    "created_by": {
      "object": "user",
      "id": "23345d4f-cf71-4a70-89a5-226c95a6eaae",
      "name": "Test User",
      "type": "person",
      "person": {
        "email": "avo@example.org"
      }
    }
  }
}
```

## **Last edited time**

Last edited time property value objects contain a string within the `last_edited_time` property. The string contains the date and time when this page was last updated. It is formatted as an [__ISO 8601__](https://en.wikipedia.org/wiki/ISO_8601) date time string (i.e. `"2020-03-17T19:10:04.968Z"`).

Last edited time property valueLast edited time property value (using ID)

```
{
  "Last Edited Time": {
  	"last_edited_time": "2020-03-17T19:10:04.968Z"
  }
}
```

## **Last edited by**

Last edited by property value objects contain a [__user object__](https://developers.notion.com/reference/user) within the `last_edited_by` property. The user object describes the user who last updated this page.

Last edited by property valueLast edited by property value (using ID)

{   "Last Edited By": {     "last_edited_by": {       "object": "user",       "id": "23345d4f-cf71-4a70-89a5-226c95a6eaae",       "name": "Test User",       "type": "person",       "person": {         "email": "avo@example.org"       }     }   } }  

# **Database**

Learn more about Notion's database object.

A **database** is an object that contains one or more [__data sources__](https://developers.notion.com/reference/data-sources). Databases can either be displayed inline in the parent page (`is_inline: true`) or as a full page (`is_inline: false`). The properties (schema) of each data source under a database can be maintained independently, and each data source has its own set of rows (pages).

Individual data sources don't have permissions settings, so the set of Notion users and bots that have access to data source children is managed through **databases**.

Databases that exist at the workspace level must be full-page databases, not inline. For easier permission management, we typically recommend having at least one level of parent page in between a database and the top-level workspace root.

## **Object fields**

> ## **📘Changed as of 2025-09-03**
>
> In September 2025, the [__Data source__](https://developers.notion.com/reference/data-source) object was introduced, and includes the `properties` that used to exist here at the database level.
>
> Diagram of the new Notion API data model.
> A database is a parent of one or more data sources, each of which parents zero or more pages.
> Previously, databases could only have one data source, so the concepts were combined in the API until 2025.
>
> After [__upgrading your API__](https://developers.notion.com/docs/upgrade-guide-2025-09-03) integration to `2025-09-03`, the new database object shape is displayed, including an array of child `data_sources` but **not** the data source `properties`.

**FieldTypeDescriptionExample value**`objectstring`Always `"database"`.`"database"idstring` (UUID)Unique identifier for the database.`"2f26ee68-df30-4251-aad4-8ddc420cba3d"data_sources`array of data source objectsList of child data sources, each of which is a JSON object with an `id` and `name`.

Use [__Retrieve a data source__](https://developers.notion.com/reference/retrieve-a-data-source) to get more details on the data source, including its `properties`.`[{"id": "c174b72c-d782-432f-8dc0-b647e1c96df6", "name": "Tasks data source"}]created_timestring` ([__ISO 8601 date and time__](https://en.wikipedia.org/wiki/ISO_8601))Date and time when this database was created. Formatted as an [__ISO 8601 date time__](https://en.wikipedia.org/wiki/ISO_8601) string.`"2020-03-17T19:10:04.968Z"created_by`[__Partial User__](https://developers.notion.com/reference/user)User who created the database.`{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}last_edited_timestring` ([__ISO 8601 date and time__](https://en.wikipedia.org/wiki/ISO_8601))Date and time when this database was updated. Formatted as an [__ISO 8601 date time__](https://en.wikipedia.org/wiki/ISO_8601) string.`"2020-03-17T21:49:37.913Z"last_edited_by`[__Partial User__](https://developers.notion.com/reference/user)User who last edited the database.`{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}title`array of [__rich text objects__](https://developers.notion.com/reference/rich-text)Name of the database as it appears in Notion.
See [__rich text object__](https://developers.notion.com/reference/rich-text)) for a breakdown of the properties.`"title": [ { "type": "text", "text": { "content": "Can I create a URL property", "link": null }, "annotations": { "bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default" }, "plain_text": "Can I create a URL property", "href": null } ]description`array of [__rich text objects__](https://developers.notion.com/reference/rich-text)Description of the database as it appears in Notion.
See [__rich text object__](https://developers.notion.com/reference/rich-text)) for a breakdown of the properties.`icon`[__File Object__](https://developers.notion.com/reference/file-object) or [__Emoji object__](https://developers.notion.com/reference/emoji-object)Page icon.`cover`[__File object__](https://developers.notion.com/reference/file-object)Page cover image.`parentobject`Information about the database's parent. See [__Parent object__](https://developers.notion.com/reference/parent-object).`{ "type": "page_id", "page_id": "af5f89b5-a8ff-4c56-a5e8-69797d11b9f8" }urlstring`The URL of the Notion database.`"https://www.notion.so/668d797c76fa49349b05ad288df2d136"archivedboolean`The archived status of the database.`falsein_trashboolean`Whether the database has been deleted.`falseis_inlineboolean`Has the value `true` if the database appears in the page as an inline block. Otherwise has the value `false` if the database appears as a child page.`falsepublic_urlstring`The public page URL if the page has been published to the web. Otherwise, `null`.`"https://jm-testing.notion.site/p1-6df2c07bfc6b4c46815ad205d132e22d"1`

# **Data source**

Learn more about Notion's data source object.

**Data sources** are the individual tables of data that live under a Notion database. [__Pages__](https://developers.notion.com/reference/page) are the items (or children) in a data source. [__Page property values__](https://developers.notion.com/reference/page#property-value-object) must conform to the [__property objects__](https://developers.notion.com/reference/property-object) laid out in the parent data source object.

Diagram of the new Notion API data model.
A database is a parent of one or more data sources, each of which parents zero or more pages.
Previously, databases could only have one data source, so the concepts were combined in the API until 2025.

As of API version `2025-09-03`, there's a suite of APIs for managing data sources:
- [__Create a data source__](https://developers.notion.com/reference/create-a-data-source): add an additional data source for an existing [__Database__](https://developers.notion.com/reference/database)
- [__Update a data source__](https://developers.notion.com/reference/update-a-data-source): update attributes, such as the `properties`, of a data source
- [__Retrieve a data source__](https://developers.notion.com/reference/retrieve-a-data-source)
- [__Query a data source__](https://developers.notion.com/reference/query-a-data-source)

## **Object fields**

> ## **📘**
>
> Properties marked with an asterisk (*) are available to integrations with any capabilities. Other properties require read content capabilities in order to be returned from the Notion API. For more information on integration capabilities, see the [__capabilities guide__](https://developers.notion.com/reference/capabilities).

**FieldTypeDescriptionExample value**`object`*`string`Always `"data_source"`.`"data_source"id`*`string` (UUID)Unique identifier for the data source.`"2f26ee68-df30-4251-aad4-8ddc420cba3d"properties`*`object`Schema of properties for the data source as they appear in Notion.

`key` string
The name of the property as it appears in Notion.

`value` object
A [__Property object__](https://developers.notion.com/reference/property-object).`parentobject`Information about the data source's parent database. See [__Parent object__](https://developers.notion.com/reference/parent-object).`{"type": "database_id", "database_id": "842a0286-cef0-46a8-abba-eac4c8ca644e"}database_parentobject`Information about the database's parent (in other words, the the data source's grandparent). See [__Parent object__](https://developers.notion.com/reference/parent-object) .`{ "type": "page_id", "page_id": "af5f89b5-a8ff-4c56-a5e8-69797d11b9f8" }created_timestring` ([__ISO 8601 date and time__](https://en.wikipedia.org/wiki/ISO_8601))Date and time when this data source was created. Formatted as an [__ISO 8601 date time__](https://en.wikipedia.org/wiki/ISO_8601) string.`"2020-03-17T19:10:04.968Z"created_by`[__Partial User__](https://developers.notion.com/reference/user)User who created the data source.`{"object": "user", "id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}last_edited_timestring` ([__ISO 8601 date and time__](https://en.wikipedia.org/wiki/ISO_8601))Date and time when this data source was updated. Formatted as an [__ISO 8601 date time__](https://en.wikipedia.org/wiki/ISO_8601) string.`"2020-03-17T21:49:37.913Z"last_edited_by`[__Partial User__](https://developers.notion.com/reference/user)User who last edited the data source.`{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}title`array of [__rich text objects__](https://developers.notion.com/reference/rich-text)Name of the data source as it appears in Notion.
See [__rich text object__](https://developers.notion.com/reference/rich-text)) for a breakdown of the properties.`[ { "type": "text", "text": { "content": "Can I create a URL property", "link": null }, "annotations": { "bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default" }, "plain_text": "Can I create a URL property", "href": null } ]description`array of [__rich text objects__](https://developers.notion.com/reference/rich-text)Description of the data source as it appears in Notion.
See [__rich text object__](https://developers.notion.com/reference/rich-text)) for a breakdown of the properties.`icon`[__File Object__](https://developers.notion.com/reference/file-object) or [__Emoji object__](https://developers.notion.com/reference/emoji-object)Data source icon.`archivedboolean`The archived status of the data source.`falsein_trashboolean`Whether the data source has been deleted.`false`

> ## **🚧Maximum schema size recommendation**
>
> Notion recommends a maximum schema size of **50KB**. Updates to database schemas that are too large will be blocked to help maintain database performance.

# **Data source properties**

Data source property objects are rendered in the Notion UI as data columns.

All [__data source objects__](https://developers.notion.com/reference/data-source) include a child `properties` object. This `properties` object is composed of individual data source property objects. These property objects define the data source schema and are rendered in the Notion UI as data columns.

> ## **📘Data source rows**
>
> If you’re looking for information about how to use the API to work with data source rows, then refer to the [__page property values__](https://developers.notion.com/reference/property-value-object) documentation. The API treats data source rows as pages.

Every data source property object contains the following keys:

**FieldTypeDescriptionExample value**`idstring`An identifier for the property, usually a short string of random letters and symbols.

Some automatically generated property types have special human-readable IDs. For example, all Title properties have an `id` of `"title"`.`"fy:{"namestring`The name of the property as it appears in Notion.`descriptionstring`The description of a property as it appear in Notion.`typestring` (enum)The type that controls the behavior of the property. Possible values are:

- `"checkbox"`

- `"created_by"`
- `"created_time"`
- `"date"`
- `"email"`
- `"files"`
- `"formula"`
- `"last_edited_by"`
- `"last_edited_time"`
- `"multi_select"`
- `"number"`
- `"people"`
- `"phone_number"`
- `"relation"`
- `"rich_text"`
- `"rollup"`
- `"select"`
- `"status"`
- `"title"`
- `"url""rich_text"`

Each data source property object also contains a type object. The key of the object is the `type` of the object, and the value is an object containing type-specific configuration. The following sections detail these type-specific objects along with example property objects for each type.

## **Checkbox**

A checkbox data source property is rendered in the Notion UI as a column that contains checkboxes. The `checkbox` type object is empty; there is no additional property configuration.

Example checkbox data source property object

```
"Task complete": {
  "id": "BBla",
  "name": "Task complete",
  "type": "checkbox",
  "checkbox": {}
}
```

## **Created by**

A created by data source property is rendered in the Notion UI as a column that contains people mentions of each row's author as values.

The `created_by` type object is empty. There is no additional property configuration.

Example created by data source property object

```
"Created by": {
  "id": "%5BJCR",
  "name": "Created by",
  "type": "created_by",
  "created_by": {}
}
```

## **Created time**

A created time data source property is rendered in the Notion UI as a column that contains timestamps of when each row was created as values.

The `created_time` type object is empty. There is no additional property configuration.

Example created time data source property object

```
"Created time": {
  "id": "XcAf",
  "name": "Created time",
  "type": "created_time",
  "created_time": {}
}
```

## **Date**

A date data source property is rendered in the Notion UI as a column that contains date values.

The `date` type object is empty; there is no additional configuration.

Example date data source property object

```
"Task due date" {
  "id": "AJP%7D",
  "name": "Task due date",
  "type": "date",
  "date": {}
}
```

## **Email**

An email data source property is represented in the Notion UI as a column that contains email values.

The `email` type object is empty. There is no additional property configuration.

Example email data source property object

```
"Contact email": {
  "id": "oZbC",
  "name": "Contact email",
  "type": "email",
  "email": {}
}
```

## **Files**

A files data source property is rendered in the Notion UI as a column that has values that are either files uploaded directly to Notion or external links to files. The `files` type object is empty; there is no additional configuration.

Example files data source property object

```
"Product image": {
  "id": "pb%3E%5B",
  "name": "Product image",
  "type": "files",
  "files": {}
}
```

## **Formula**

A formula data source property is rendered in the Notion UI as a column that contains values derived from a provided expression.

The `formula` type object defines the expression in the following fields:

**FieldTypeDescriptionExample value**`expressionstring`The formula that is used to compute the values for this property.

Refer to the Notion help center for [__information about formula syntax__](https://www.notion.so/help/formulas).`{{notion:block_property:BtVS:00000000-0000-0000-0000-000000000000:8994905a-074a-415f-9bcf-d1f8b4fa38e4}}/2`

Example formula data source property object

```
"Updated price": {
  "id": "YU%7C%40",
  "name": "Updated price",
  "type": "formula",
  "formula": {
    "expression": "{{notion:block_property:BtVS:00000000-0000-0000-0000-000000000000:8994905a-074a-415f-9bcf-d1f8b4fa38e4}}/2"
  }
}
```

## **Last edited by**

A last edited by data source property is rendered in the Notion UI as a column that contains people mentions of the person who last edited each row as values.

The `last_edited_by` type object is empty. There is no additional property configuration.

## **Last edited time**

A last edited time data source property is rendered in the Notion UI as a column that contains timestamps of when each row was last edited as values.

The `last_edited_time` type object is empty. There is no additional property configuration.

Example last edited time data source property object

```
"Last edited time": {
  "id": "jGdo",
  "name": "Last edited time",
  "type": "last_edited_time",
  "last_edited_time": {}
}
```

## **Multi-select**

A multi-select data source property is rendered in the Notion UI as a column that contains values from a range of options. Each row can contain one or multiple options.

The `multi_select` type object includes an array of `options` objects. Each option object details settings for the option, indicating the following fields:

**FieldTypeDescriptionExample value**`colorstring` (enum)The color of the option as rendered in the Notion UI. Possible values include:

- `blue`

- `brown`
- `default`
- `gray`
- `green`
- `orange`
- `pink`
- `purple`
- `red`
- `yellow"blue"idstring`An identifier for the option, which does not change if the name is changed. An `id` is sometimes, but not *always*, a UUID.`"ff8e9269-9579-47f7-8f6e-83a84716863c"namestring`The name of the option as it appears in Notion.

**Notes**: Commas (",") are not valid for multi-select properties. Names **MUST** be unique across options, ignoring case. For example, you can't have two options that are named `"apple"` and `"APPLE"`.`"Fruit"`

Example multi-select data source property

```
"Store availability": {
  "id": "flsb",
  "name": "Store availability",
  "type": "multi_select",
  "multi_select": {
    "options": [
      {
        "id": "5de29601-9c24-4b04-8629-0bca891c5120",
        "name": "Duc Loi Market",
        "color": "blue"
      },
      {
        "id": "385890b8-fe15-421b-b214-b02959b0f8d9",
        "name": "Rainbow Grocery",
        "color": "gray"
      },
      {
        "id": "72ac0a6c-9e00-4e8c-80c5-720e4373e0b9",
        "name": "Nijiya Market",
        "color": "purple"
      },
      {
        "id": "9556a8f7-f4b0-4e11-b277-f0af1f8c9490",
        "name": "Gus's Community Market",
        "color": "yellow"
      }
    ]
  }
}
```

## **Number**

A number data source property is rendered in the Notion UI as a column that contains numeric values. The `number` type object contains the following fields:

**FieldTypeDescriptionExample value**`formatstring` (enum)The way that the number is displayed in Notion. Potential values include:

- `argentine_peso`

- `baht`
- `australian_dollar`
- `canadian_dollar`
- `chilean_peso`
- `colombian_peso`
- `danish_krone`
- `dirham`
- `dollar`
- `euro`
- `forint`
- `franc`
- `hong_kong_dollar`
- `koruna`
- `krona`
- `leu`
- `lira`
- `mexican_peso`
- `new_taiwan_dollar`
- `new_zealand_dollar`
- `norwegian_krone`
- `number`
- `number_with_commas`
- `percent`
- `philippine_peso`
- `pound`
- `peruvian_sol`
- `rand`
- `real`
- `ringgit`
- `riyal`
- `ruble`
- `rupee`
- `rupiah`
- `shekel`
- `singapore_dollar`
- `uruguayan_peso`
- `yen`,
- `yuan`
- `won`
- `zloty"percent"`

Example number data source property object

```
"Price"{
  "id": "%7B%5D_P",
  "name": "Price",
  "type": "number",
  "number": {
    "format": "dollar"
  }
}
```

## **People**

A people data source property is rendered in the Notion UI as a column that contains people mentions. The `people` type object is empty; there is no additional configuration.

Example people data source property object

```
"Project owner": {
  "id": "FlgQ",
  "name": "Project owner",
  "type": "people",
  "people": {}
}
```

## **Phone number**

A phone number data source property is rendered in the Notion UI as a column that contains phone number values.

The `phone_number` type object is empty. There is no additional property configuration.

Example phone number data source property object

```
"Contact phone number": {
  "id": "ULHa",
  "name": "Contact phone number",
  "type": "phone_number",
  "phone_number": {}
}
```

## **Relation**

A relation data source property is rendered in the Notion UI as column that contains [__relations__](https://www.notion.so/help/relations-and-rollups), references to pages in another data source, as values.

The `relation` type object contains the following fields:

**FieldTypeDescriptionExample value**`data_source_idstring` (UUID)The data source that the relation property refers to.

The corresponding linked page values must belong to the data source in order to be valid.`"668d797c-76fa-4934-9b05-ad288df2d136"synced_property_idstring`The `id` of the corresponding property that is updated in the related data source when this property is changed.`"fy:{"synced_property_namestring`The `name` of the corresponding property that is updated in the related data source when this property is changed.`"Ingredients"`

Example relation data source property object

```
"Projects": {
  "id": "~pex",
  "name": "Projects",
  "type": "relation",
  "relation": {
    "data_source_id": "6c4240a9-a3ce-413e-9fd0-8a51a4d0a49b",
    "dual_property": {
      "synced_property_name": "Tasks",
      "synced_property_id": "JU]K" 
    }
  }
}
```

> ## **📘Database relations must be shared with your integration**
>
> To retrieve properties from data source [__relations__](https://www.notion.so/help/relations-and-rollups#what-is-a-database-relation), the related database must be shared with your integration in addition to the database being retrieved. If the related database is not shared, properties based on relations will not be included in the API response.
>
> Similarly, to update a data source relation property via the API, share the related database with the integration.

## **Rich text**

A rich text data source property is rendered in the Notion UI as a column that contains text values. The `rich_text` type object is empty; there is no additional configuration.

Example rich text data source property object

```
"Project description": {
  "id": "NZZ%3B",
  "name": "Project description",
  "type": "rich_text",
  "rich_text": {}
}
```

## **Rollup**

A rollup data source property is rendered in the Notion UI as a column with values that are rollups, specific properties that are pulled from a related data source.

The `rollup` type object contains the following fields:

**FieldTypeDescriptionExample value**`functionstring` (enum)The function that computes the rollup value from the related pages.

Possible values include:

- `average`

- `checked`
- `count_per_group`
- `count`
- `count_values`
- `date_range`
- `earliest_date`
- `empty`
- `latest_date`
- `max`
- `median`
- `min`
- `not_empty`
- `percent_checked`
- `percent_empty`
- `percent_not_empty`
- `percent_per_group`
- `percent_unchecked`
- `range`
- `unchecked`
- `unique`
- `show_original`
- `show_unique`
- `sum"sum"relation_property_idstring`The `id` of the related data source property that is rolled up.`"fy:{"relation_property_namestring`The `name` of the related data source property that is rolled up.`Tasks"rollup_property_idstring`The `id` of the rollup property.`"fy:{"rollup_property_namestring`The `name` of the rollup property.`"Days to complete"`

Example rollup data source property object

```
"Estimated total project time": {
  "id": "%5E%7Cy%3C",
  "name": "Estimated total project time",
  "type": "rollup",
  "rollup": {
    "rollup_property_name": "Days to complete",
    "relation_property_name": "Tasks",
    "rollup_property_id": "\\nyY",
    "relation_property_id": "Y]<y",
    "function": "sum"
  }
}
```

## **Select**

A select data source property is rendered in the Notion UI as a column that contains values from a selection of options. Only one option is allowed per row.

The `select` type object contains an array of objects representing the available options. Each option object includes the following fields:

**FieldTypeDescriptionExample value**`colorstring` (enum)The color of the option as rendered in the Notion UI. Possible values include:

- `blue`

- `brown`
- `default`
- `gray`
- `green`
- `orange`
- `pink`
- `purple`
- `red`
- `yellow`- `"red"idstring`An identifier for the option. It doesn't change if the name is changed. These are sometimes, but not *always*, UUIDs.`"ff8e9269-9579-47f7-8f6e-83a84716863c"namestring`The name of the option as it appears in the Notion UI.

**Notes**: Commas (",") are not valid for select properties. Names **MUST** be unique across options, ignoring case. For example, you can't have two options that are named `"apple"` and `"APPLE"`.`"Fruit"`

Example select data source property object

```
"Food group": {
  "id": "%40Q%5BM",
  "name": "Food group",
  "type": "select",
  "select": {
    "options": [
      {
        "id": "e28f74fc-83a7-4469-8435-27eb18f9f9de",
        "name": "🥦Vegetable",
        "color": "purple"
      },
      {
        "id": "6132d771-b283-4cd9-ba44-b1ed30477c7f",
        "name": "🍎Fruit",
        "color": "red"
      },
      {
        "id": "fc9ea861-820b-4f2b-bc32-44ed9eca873c",
        "name": "💪Protein",
        "color": "yellow"
      }
    ]
  }
}
```

## **Status**

A status data source property is rendered in the Notion UI as a column that contains values from a list of status options. The `status` type object includes an array of `options` objects and an array of `groups` objects.

The `options` array is a sorted list of list of the available status options for the property. Each option object in the array has the following fields:

**FieldTypeDescriptionExample value**`colorstring` (enum)The color of the option as rendered in the Notion UI. Possible values include:

- `blue`

- `brown`
- `default`
- `gray`
- `green`
- `orange`
- `pink`
- `purple`
- `red`
- `yellow"green"idstring`An identifier for the option. The `id` does not change if the `name` is changed. It is sometimes, but not *always*, a UUID.`"ff8e9269-9579-47f7-8f6e-83a84716863c"namestring`The name of the option as it appears in the Notion UI.

**Notes**: Commas (",") are not valid for select properties. Names **MUST** be unique across options, ignoring case. For example, you can't have two options that are named `"In progress"` and `"IN PROGRESS"`.`"In progress"`

A group is a collection of options. The `groups` array is a sorted list of the available groups for the property. Each group object in the array has the following fields:

**FieldTypeDescriptionExample value**`colorstring` (enum)The color of the option as rendered in the Notion UI. Possible values include:

- `blue`

- `brown`
- `default`
- `gray`
- `green`
- `orange`
- `pink`
- `purple`
- `red`
- `yellow"purple"idstring`An identifier for the option. The `id` does not change if the `name` is changed. It is sometimes, but not *always*, a UUID.`"ff8e9269-9579-47f7-8f6e-83a84716863c"namestring`The name of the option as it appears in the Notion UI.

**Note**: Commas (",") are not valid for status values.`"To do"option_ids`an array of `string`s (UUID)A sorted list of `id`s of all of the options that belong to a group.Refer to the example `status` object below.

Example status data source property object

```
"Status": {
  "id": "biOx",
  "name": "Status",
  "type": "status",
  "status": {
    "options": [
      {
        "id": "034ece9a-384d-4d1f-97f7-7f685b29ae9b",
        "name": "Not started",
        "color": "default"
      },
      {
        "id": "330aeafb-598c-4e1c-bc13-1148aa5963d3",
        "name": "In progress",
        "color": "blue"
      },
      {
        "id": "497e64fb-01e2-41ef-ae2d-8a87a3bb51da",
        "name": "Done",
        "color": "green"
      }
    ],
    "groups": [
      {
        "id": "b9d42483-e576-4858-a26f-ed940a5f678f",
        "name": "To-do",
        "color": "gray",
        "option_ids": [
          "034ece9a-384d-4d1f-97f7-7f685b29ae9b"
        ]
      },
      {
        "id": "cf4952eb-1265-46ec-86ab-4bded4fa2e3b",
        "name": "In progress",
        "color": "blue",
        "option_ids": [
          "330aeafb-598c-4e1c-bc13-1148aa5963d3"
        ]
      },
      {
        "id": "4fa7348e-ae74-46d9-9585-e773caca6f40",
        "name": "Complete",
        "color": "green",
        "option_ids": [
          "497e64fb-01e2-41ef-ae2d-8a87a3bb51da"
        ]
      }
    ]
  }
}
```

> ## **🚧It is not possible to update a status data source property's **`name`** or **`options`** values via the API.**
>
> Update these values from the Notion UI, instead.

## **Title**

A title data source property controls the title that appears at the top of a page when a data source row is opened. The `title` type object itself is empty; there is no additional configuration.

Example title data source property object

```
"Project name": {
  "id": "title",
  "name": "Project name",
  "type": "title",
  "title": {}
}
```

> ## **🚧All data sources require one, and only one, **`title`** property.**
>
> The API throws errors if you send a request to [__Create a data source__](https://developers.notion.com/reference/create-a-data-source) or [__Create a database__](https://developers.notion.com/reference/database-create) without a `title` property, or if you attempt to [__Update a data source__](https://developers.notion.com/reference/update-a-data-source) to add or remove a `title` property.

> ## **📘Title data source property vs. data source title**
>
> A `title` data source property is a type of column in a data source.
>
> A data source `title` defines the title of the data source and is found on the [__data source object__](https://developers.notion.com/reference/data-source).
>
> Every data source requires both a data source `title` and a `title` data source property. This ensures that we have both:>
> - An overall title to display when viewing the database or data source in the Notion app>
> - A title property for each page under the data source, so page titles can be displayed in the Notion app

## **URL**

A URL data source property is represented in the Notion UI as a column that contains URL values.

The `url` type object is empty. There is no additional property configuration.

Example URL data source property object

```
"Project URL": {
  "id": "BZKU",
  "name": "Project URL",
  "type": "url",
  "url": {}
}
```

## **Unique ID**

A unique ID data source property records values that are automatically incremented, and enforced to be unique across all pages in a data source. This can be useful for task or bug report IDs (e.g. TASK-1234), or other similar types of identifiers that must be unique.

The `unique_id` type object can contain an optional `prefix` attribute, which is a common prefix assigned to pages in the data source. When a `prefix` is set, a special URL (for example, `notion.so/TASK-1234`) is generated to be able to look up a page easily by the ID. Learn more in our [__help center documentation__](https://www.notion.com/help/unique-id) or [__Notion Academy lesson__](https://www.notion.com/help/notion-academy/lesson/unique-id-property).

```
Example unique ID data source property object
"Task ID": {   "prefix": "TASK" }  
```

# **File**

Files, images, and other media bring Notion pages to life — from rich visuals in image blocks to downloadable attachments in databases, or branded page icons and covers.

This guide introduces how file objects work in the Notion API, the different types of file sources you can work with, and how to choose the right type for your integration.

You’ll learn about:
- Files uploaded manually in the Notion UI — returned as Notion-hosted file objects (type: `file`)
- Files uploaded via API — created using the File Upload API (type: `file_upload`)
- External files — linked via a public URL (type: `external`)

## **What is a file object?**

In the Notion API, any media asset is represented as a file object. A file object stores metadata about the file and indicates where and how the file is hosted.

Each file object has a required type field that determines the structure of its contents:

**FieldTypeDescription**`typestring` (enum)The type of the file object. Possible type values are: `"file"`, `"file_upload"`, `"external"`.`file`|`file_upload` | `externalobject`An object containing type-specific configuration.

Refer to the type sections below for details on type-specific values.

Here’s what each type looks like:

javascript

```
// Notion-hosted file (uploaded via UI)  
{  
  "type": "file",  
  "file": {  
    "url": "<https://s3.us-west-2.amazonaws.com/...">,  
    "expiry_time": "2025-04-24T22:49:22.765Z"  
  }  
}

// File uploaded via the Notion API  
{  
  "type": "file_upload",  
  "file_upload": {  
    "id": "43833259-72ae-404e-8441-b6577f3159b4"  
  }  
}

// External file  
{  
  "type": "external",  
  "external": {  
    "url": "<https://example.com/image.png">  
  }  
}
```

### **Notion-hosted files (type: **`file`**)**

These are files that users upload manually through the Notion app — such as dragging an image into a page, adding a PDF block, or setting a page cover.

**When to use:**
- You're working with existing content in a Notion workspace
- You’re accessing files that users manually added via drag-and-drop or upload

**Tips**
- Each time you fetch a Notion-hosted file, it includes a temporary public url valid for 1 hour.
- Don’t cache or statically reference these URLs. To refresh access, re-fetch the file object.

**These corresponding file objects contain the following fields:**

**FieldTypeDescriptionExample value**`urlstring`An authenticated HTTP GET URL to the file.

The URL is valid for one hour. If the link expires, send an API request to get an updated URL.`"https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9bc6c6e0-32b8-4d55-8c12-3ae931f43a01/brocolli.jpeg?..."expiry_timestring` ([__ISO 8601__](https://en.wikipedia.org/wiki/ISO_8601) date time)The date and time when the link expires.`"2020-03-17T19:10:04.968Z"`

**Example snippet**:

json

```
{  
  "type": "file",  
  "file": {  
    "url": "<https://s3.us-west-2.amazonaws.com/...">,  
    "expiry_time": "2025-04-24T22:49:22.765Z"  
  }  
}
```

### **Files uploaded in the API (type: **`file_upload`**)**

These are files uploaded using the File Upload API. You first create a [__File Upload__](https://developers.notion.com/reference/file-upload), send file content, and then reference it by ID to attach it.

**When to use:**
1. You want to programmatically upload files to Notion
2. You’re building automations or file-rich integrations

**Tips**
- Once uploaded, you can reuse the File Upload ID to attach the same file to multiple pages or blocks
- To learn more about file uploads, view the [__Working with files and media__](https://developers.notion.com/docs/working-with-files-and-media) guide

**These corresponding file objects contain the following fields:**

**FieldTypeDescriptionExample Value**`id`UUIDID of a [__File Upload__](https://developers.notion.com/reference/file-upload) object that has a `status` of `"uploaded""43833259-72ae-404e-8441-b6577f3159b4"`

**Example snippet**:

json

```
{  
  "type": "file_upload",  
  "file_upload": {  
    "id": "43833259-72ae-404e-8441-b6577f3159b4"  
  }  
}
```

## **External files (type: **`external`**)**

Use this approach if you have already hosted your files elsewhere (e.g., S3, Dropbox, CDN) and want Notion to link to them.

**When to use:**
- You have an existing CDN or media server
- You have stable, permanent URLs
- Your files are publicly accessible and don’t require authentication
- You don’t want to upload files into Notion

**How to use:**
- Pass an HTTPS URL when creating or updating file-supporting blocks or properties.
- These links never expire and will always be returned as-is in API responses.

**These corresponding file objects contain the following fields:**

**FieldTypeDescriptionExample value**`urlstring`A link to the externally hosted content.`"https://website.domain/files/doc.txt"`

**Example snippet**:

json

```
{  
  "type": "external",  
  "external": {  
    "url": "<https://example.com/photo.png">  
  }  
}
```

# **Working with files and media**

Learn how to add or retrieve files and media from Notion pages.

[Suggest Edits](https://developers.notion.com/edit/working-with-files-and-media)

Files, images, and other media bring your Notion workspace to life — from company logos and product photos to contract PDFs and design assets. With the Notion API, you can programmatically upload, attach, and reuse these files wherever they’re needed.

In this guide, you’ll learn how to:
- Upload a new file using the **Direct Upload** method (single-part)
- Retrieve existing files already uploaded to your workspace

We’ll also walk through the different upload methods and supported file types, so you can choose the best path for your integration.

## **Upload methods at a glance**

The Notion API supports three ways to add files to your workspace:

**Upload methodDescriptionBest for**[**__Direct Upload__**](https://developers.notion.com/docs/uploading-small-files)Upload a file (≤ 20MB) via a `multipart/form-data` requestThe simplest method for most files[**__Direct Upload (multi-part)__**](https://developers.notion.com/docs/sending-larger-files)Upload large files (&gt; 20MB) in chunks across multiple requestsLarger media assets and uploads over time[**__Indirect Import__**](https://developers.notion.com/docs/importing-external-files)Import a file from a publicly accessible URLMigration workflows and hosted content

## **Supported block types**

Uploaded files can be attached to:
- Media blocks: `file`, `image`, `pdf`, `audio`, `video`
- Page properties: `files` properties in databases
- Page-level visuals: page `icon` and `cover`

💡** Need support for another block or content type**? Let us know [__here__](https://notiondevs.notion.site/1f8a4445d271805da593dd86bd86872b?pvs=105).

## **Supported file types**

Before uploading, make sure your file type is supported. Here’s what the API accepts:

**CategoryExtensionsMIME typesAudio**.aac, .adts, .mid, .midi, .mp3, .mpga, .m4a, .m4b, .mp4, .oga, .ogg, .wav, .wmaaudio/aac, audio/midi, audio/mpeg, audio/mp4, audio/ogg, audio/wav, audio/x-ms-wma**Document**.pdf, .txt, .json, .doc, .dot, .docx, .dotx, .xls, .xlt, .xla, .xlsx, .xltx, .ppt, .pot, .pps, .ppa, .pptx, .potxapplication/pdf, text/plain, application/json, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/vnd.openxmlformats-officedocument.wordprocessingml.template, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.openxmlformats-officedocument.spreadsheetml.template, application/vnd.ms-powerpoint, application/vnd.openxmlformats-officedocument.presentationml.presentation, application/vnd.openxmlformats-officedocument.presentationml.template**Image**.gif, .heic, .jpeg, .jpg, .png, .svg, .tif, .tiff, .webp, .icoimage/gif, image/heic, image/jpeg, image/png, image/svg+xml, image/tiff, image/webp, image/vnd.microsoft.icon**Video**.amv, .asf, .wmv, .avi, .f4v, .flv, .gifv, .m4v, .mp4, .mkv, .webm, .mov, .qt, .mpegvideo/x-amv, video/x-ms-asf, video/x-msvideo, video/x-f4v, video/x-flv, video/mp4, application/mp4, video/webm, video/quicktime, video/mpeg

> ## **⚠️Ensure your file type matches the context**
>
> For example:>
> - You can’t use a video in an image block>
> - Page icons can’t be PDFs>
> - Text files can’t be embedded in video blocks

### **File size limits**

- **Free** workspaces are limited to **5 MiB (binary megabytes) per file**
- **Paid** workspaces are limited to **5 GiB per file**.
  - Files larger than 20 MiB must be split into parts and [__uploaded using multi-part mode__](https://developers.notion.com/docs/sending-larger-files) in the API.

These are the same [__size limits that apply__](https://www.notion.com/pricing) to uploads in the Notion app UI.

Use the [__Retrieve a user__](https://developers.notion.com/reference/get-user) or [__List all users__](https://developers.notion.com/reference/get-users) API to get the file size limit for a [__bot user__](https://developers.notion.com/reference/user#bots). Public integrations that can be added to both free or paid workspaces can retrieve or cache each bot's file size limit. This can help avoid HTTP 400 validation errors for attempting to [__send__](https://developers.notion.com/reference/send-a-file-upload) files above the size limit.

Bot user API response shape

```
type APIUserObject = {
  object: "user",
  type: "bot",
  // ... other fields omitted

  bot: {
    // ... other fields omitted

    // Limits and restrictions that apply to the bot's workspace.
    workspace_limits: {
      // The maximum allowable size of a file upload, in bytes.
      max_file_upload_size_in_bytes: number,
    },
  }
}
```

For example, in a free workspace where bots are limited to FileUploads of 5 MiB, the response looks like:

Example user API object response

```
{
  "object": "user",
  "id": "be51669b-1932-4a11-8d35-38fbc2e1e4fd",
  "type": "bot",
  "bot": {
    "owner": {
      "type": "workspace"
    },
    "workspace_name": "Cat's Notion",
    "workspace_limits": {
      "max_file_upload_size_in_bytes": 5242880
    }
  }
}
```

### **Other limitations**

The rest of the pages in this guide, as well as the API reference for the File Upload API, include additional validations and restrictions to keep in mind as you build your integration and send files.

One final limit to note here is both the [__Create a file upload__](https://developers.notion.com/reference/create-a-file-upload) and [__Send a file upload__](https://developers.notion.com/reference/send-a-file-upload) APIs allow a maximum length of a `filename` (including the extension) of 900 bytes. However, we recommend using shorter names for performance and easier file management and lookup using the [__List file uploads__](https://developers.notion.com/reference/list-file-uploads) API.

**Updated 3 months ago**

---

**What’s Next**

Now that you know what’s supported, let’s walk through a real upload using the simplest method: uploading a single file in one request.

# **Uploading small files**

Learn how to send and attach files up to 20 MB using the Notion API.

[Suggest Edits](https://developers.notion.com/edit/uploading-small-files)

The **Direct Upload** method lets you securely upload private files to Notion-managed storage via the API. Once uploaded, these files can be reused and attached to pages, blocks, or database properties.

This guide walks you through the upload lifecycle:
1. Create a file upload object
2. Send the file content to Notion
3. Attach the file to content in your workspace

💡 **Tip**: Upload once, attach many times. You can reuse the same `file_upload` ID across multiple blocks or pages.

---

## **Step 1: Create a File Upload object**

Before uploading any content, start by creating a [__File Upload object__](https://developers.notion.com/reference/file-upload). This returns a unique `id` and `upload_url` used to send the file.

**🧠 Tip: **Save the `id` — You’ll need it to upload the file in Step 2 and attach it in Step 3.

### **Example requests**

This snippet sends a `POST` request to create the upload object.

cURLpython

```
curl --request POST \
  --url 'https://api.notion.com/v1/file_uploads' \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{}'
```

### **Example Response**

JSON

```
{
  "object": "file_upload",
  "id": "a3f9d3e2-1abc-42de-b904-badc0ffee000",
  "created_time": "2025-04-09T22:26:00.000Z",
  "last_edited_time": "2025-04-09T22:26:00.000Z",
  "expiry_time": "2025-04-09T23:26:00.000Z",
  "upload_url": "https://api.notion.com/v1/file_uploads/a3f9d3e2-1abc-42de-b904-badc0ffee000/send",
  "archived": false,
  "status": "pending",
  "filename": null,
  "content_type": null,
  "content_length": null,
  "request_id": "b7c1fd7e-2c84-4f55-877e-d3ad7db2ac4b"
}
```

## **Step 2: Upload file contents**

Next, use the `upload_url` or File Upload object `id` from Step 1 to send the binary file contents to Notion.

**Tips**:
- The only required field is the file contents under the `file` key.
- Unlike other Notion APIs, the Send File Upload endpoint expects a Content-Type of multipart/form-data, not application/json.
- Include a boundary in the `Content-Type` header [for the Send File Upload API] as described in [__RFC 2388__](https://datatracker.ietf.org/doc/html/rfc2388) and [__RFC 1341__](https://www.w3.org/Protocols/rfc1341/7_2_Multipart.html).
  Most HTTP clients (e.g. `fetch`, `ky`) handle this automatically if you include `FormData` with your file and don't pass an explicit `Content-Type` header.

### **Example requests**

This uploads the file directly from your local system.

curljavascriptPython

```
curl --request POST \
  --url 'https://api.notion.com/v1/file_uploads/a3f9d3e2-1abc-42de-b904-badc0ffee000/send' \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Notion-Version: 2022-06-28' \
  -H 'Content-Type: multipart/form-data' \
  -F "file=@path/to-file.gif"
```

### **Example response**

JSON

```
{
  "object": "file_upload",
  "id": "a3f9d3e2-1abc-42de-b904-badc0ffee000",
  "created_time": "2025-04-09T22:26:00.000Z",
  "last_edited_time": "2025-04-09T22:27:00.000Z",
  "expiry_time": "2025-04-09T23:26:00.000Z",
  "archived": false,
  "status": "uploaded",
  "filename": "Really funny.gif",
  "content_type": "image/gif",
  "content_length": "4435",
  "request_id": "91a4ee8c-61f6-4c27-bd41-09aa35299929"
}
```

> ## **⏳Reminder**
>
> Files must be attached within **1 hour** of upload or they’ll be automatically moved to an `archived` status.

## **Step 3: Attach the file to a page or block**

Once the file’s `status` is `uploaded`, it can be attached to any location that supports file objects using the File Upload object `id`.

This step uses standard Notion API endpoints; there’s no special upload-specific API for attaching. Just pass a file object with a type of `file_upload` and include the `id` that you received earlier in Step 1.

You can use the file upload `id` with the following APIs:
1. [__Create a page__](https://developers.notion.com/reference/post-page)
   - Attach files to a database property with the `files` type
   - Include uploaded files in `children` blocks (e.g., file/image blocks inside a new page)
2. [__Update page properties__](https://developers.notion.com/reference/patch-page)
   - Update existing `files` properties on a database page
   - Set page `icon` or `cover`
3. [__Append block children__](https://developers.notion.com/reference/patch-block-children)
   - Add a new block to a page — like a file, image, audio, video, or PDF block that uses an uploaded file
4. [__Update a block__](https://developers.notion.com/reference/update-a-block)
   - Change the file attached to an existing file block (e.g., convert an image with an external URL to one that uses a file uploaded via the API)

### **Example: add an image block to a page**

This example uses the [__Append block children__](https://developers.notion.com/reference/patch-block-children) API to create a new image block in a page and attach the uploaded file.

cURLPython

```
curl --request PATCH \
	--url "https://api.notion.com/v1/blocks/$PAGE_OR_BLOCK_ID/children" \
	-H "Authorization: Bearer ntn_*****" \
	-H 'Content-Type: application/json' \
	-H 'Notion-Version: 2022-06-28' \
	--data '{
		"children": [
			{
				"type": "image",
				"image": {
					"caption": [],
					"type": "file_upload",
					"file_upload": {
						"id": "'"$FILE_UPLOAD_ID'""
					}
				}
			}
		]
	}'
```

### **Example: add a file block to a page**

example uses the [__Append block children__](https://developers.notion.com/reference/patch-block-children) API to create a new file block in a page and attach the uploaded file.

cURL

```
curl --request PATCH \
  --url "https://api.notion.com/v1/blocks/$PAGE_OR_BLOCK_ID/children" \
  -H "Authorization: Bearer ntn_*****" \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{
	  "children": [
		  {
			  "type": "file",
			  "file": {
				  "type": "file_upload",
				  "file_upload": {
					  "id": "'"$FILE_UPLOAD_ID"'"
				  }
			  }
		  }
	  ]
  }'
```

### **Example: attach a file property to a page in a database**

This example uses the [__Update page properties__](https://developers.notion.com/reference/patch-page) API to add the uploaded file to a `files` property on a page that lives in a Notion data source.

cURL

```
curl --request PATCH \
  --url "https://api.notion.com/v1/pages/$PAGE_ID" \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{
    "properties": {
      "Attachments": {
        "type": "files",
        "files": [
          {
            "type": "file_upload",
            "file_upload": { "id": "9a8b7c6d-1e2f-4a3b-9e0f-a1b2c3d4e5f6" },
            "name": "logo.png"
          }
        ]
      }
    }
  }'
```

### **Example: Set a page cover**

This example uses the [__Update page properties__](https://developers.notion.com/reference/patch-page) API to add the uploaded file as a page cover.

cURL

```
curl --request PATCH \
  --url "https://api.notion.com/v1/pages/$PAGE_ID" \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{
	  "cover": {
		  "type": "file_upload",
		  "file_upload": {
			  "id": "'"$FILE_UPLOAD_ID"'"
		  }
	  }
  }'
```

**✅ You’ve successfully uploaded and attached a file using Notion’s Direct Upload method.**

---

## **File lifecycle and reuse**

When a file is first uploaded, it has an `expiry_time`, one hour from the time of creation, during which it must be attached.

Once attached to any page, block, or database in your workspace:
- The `expiry_time` is removed.
- The file becomes a permanent part of your workspace.
- The `status` remains `uploaded`.

Even if the original content is deleted, the `file_upload` ID remains valid and can be reused to attach the file again.

Currently, there is no way to delete or revoke a file upload after it has been created.

## **Downloading an uploaded file**

Attaching a file upload gives you access to a temporary download URL via the Notion API.

These URLs expire after 1 hour.

To refresh access, re-fetch the page, block, or database where the file is attached.

📌** Tip: **A file becomes persistent and reusable after the first successful attachment — no need to re-upload.

## **Tips and troubleshooting**

- **URL expiration**: Notion-hosted files expire after 1 hour. Always re-fetch file objects to refresh links.
- **Attachment deadline**: Files must be attached within 1 hour of upload, or they’ll expire.
- **Size limit**: This guide only supports files up to 20 MB. Larger files require a [__multi-part upload__](https://developers.notion.com/docs/sending-larger-files).
- **Block type compatibility**: Files can be attached to image, file, video, audio, or pdf blocks — and to `files` properties on pages.

# **Working with databases**

Learn about data source schemas, querying data sources, and more.

[Suggest Edits](https://developers.notion.com/edit/working-with-databases)

## **Overview**

[__Databases__](https://www.notion.so/help/intro-to-databases) are containers for one or more [__data sources__](https://developers.notion.com/reference/data-source), each of which is a collection of [__pages__](https://developers.notion.com/reference/page) in a Notion workspace. Data sources can be filtered, sorted, and organized as needed. They allow users to create and manipulate structured data in Notion.

Integrations can be used to help users sync databases with external systems or build workflows around Notion databases.

In this guide, you'll learn:
- [__How databases and data sources are represented in the API__](https://developers.notion.com/docs/working-with-databases#structure).
- [__How to add items to a data source__](https://developers.notion.com/docs/working-with-databases#adding-pages-to-a-data-source).
- [__How to find items within data sources__](https://developers.notion.com/docs/working-with-databases#finding-pages-in-a-data%20source).

### **Additional types of databases**

In addition to regular Notion databases, there are two other types of databases & data sources to be aware of. *However, neither of these database types are currently supported by Notion's API.*

**Linked data sources**

Notion offers [__linked data sources__](https://www.notion.so/help/guides/using-linked-databases) as a way of showing a data source in multiple places. You can identify them by a ↗ next to the data source title which, when clicked, takes you to the original data source.

Linked databases are indicated with an arrow next to the name.

> ## **🚧**
>
> Notion's API does not currently support linked data sources. When sharing a database with your integration, make sure it contains the original data source!

**Wiki databases**

Wiki databases are a special category of databases that allow [__Workspace Owners__](https://www.notion.so/help/add-members-admins-guests-and-groups) to organize child pages and databases with a homepage view. Wiki database pages can be verified by the Workspace Owner with an optional expiration date for the verification.

Pages in a wiki database will have a `verification` property that can be set through your Notion workspace. See directions for [__creating wikis__](https://www.notion.so/help/wikis-and-verified-pages#create-a-wiki) and [__verifying pages__](https://www.notion.so/help/wikis-and-verified-pages#verifying-pages) in our Help Center.

Wiki databases can currently only be created through your Notion workspace directly (i.e., not Notion's API). Ability to retrieve wiki databases in the API may be limited, and you can't add multiple data sources to a wiki database.

To learn more about creating and working with wiki databases, see the following Help Center articles:
- [__Wikis and verified pages__](https://www.notion.so/help/wikis-and-verified-pages)
- [__Wiki guides__](https://www.notion.so/help/guides/category/wiki)

## **Structure**

Database objects, and their data source children, describe a part of what a user sees in Notion when they open a database. See our [__documentation on database objects__](https://developers.notion.com/reference/database), [__data source objects__](https://developers.notion.com/reference/data-source), and [__data source properties__](https://developers.notion.com/reference/property-object) for a complete description.

Databases contain a list of data sources (IDs and names). In turn, each data source can be retrieved and managed separately and acts as the parent for pages (rows of data) that live under them.

Database object exampleData source object example

```
{
  "object": "database",
  "id": "248104cd-477e-80fd-b757-e945d38000bd",
  "title": [
    {
      "type": "text",
      "text": {
        "content": "Grocery DB",
        // ...
      },
      // ...
    }
  ],
  "parent": {
    "type": "page_id",
    "page_id": "255104cd-477e-808c-b279-d39ab803a7d2"
  },
  "is_inline": false,
  "in_trash": false,
  "created_time": "2025-08-07T10:11:07.504-07:00",
  "last_edited_time": "2025-08-10T15:53:11.386-07:00",
  "data_sources": [
    {
      "id": "248104cd-477e-80af-bc30-000bd28de8f9",
      "name": "Grocery list"
    }
  ],
  "url": "https://www.notion.so/example/248104cd477e80fdb757e945d38000bd",
  "icon": null,
  "cover": {
    "type": "external",
    "external": {
      "url": "https://website.domain/images/image.png"
    }
  },
}
```

The most important part is the data source's schema, defined in the `properties` object.

> ## **📘Terminology**
>
> The **columns** of a Notion data source are referred to as its “**properties**” or “**schema**”.
>
> The **rows** of a data source are individual [__Page__](https://developers.notion.com/reference/page)s that live under it and each contain page properties (keys and values that conform to the data source's schema) and content (what you see in the body of the page in the Notion app).

> ## **🚧Maximum schema size recommendation**
>
> Notion recommends a maximum schema size of **50KB**. Updates to database schemas that are too large will be blocked to help maintain database performance.

### **Data source properties**

Example of a data source with three properties (Grocery item, Price, Last ordered).

Let's assume you're viewing a data source as a table. The columns of the data source are represented in the API by database [__property objects__](https://developers.notion.com/reference/property-object). Property objects store a description of a column, including a type for the allowable values that can go into a column.

You might recognize a few of the common types:
- [__Text__](https://developers.notion.com/reference/property-object#rich-text)
- [__Numbers__](https://developers.notion.com/reference/property-object#number)
- [__Dates__](https://developers.notion.com/reference/property-object#date)
- [__People__](https://developers.notion.com/reference/property-object#people)

For each type, additional configuration may also be available. Let's take a look at the `properties` section of an example data source object.

Data Source object snippet

```
{
  "object": "data_source",

  "properties": {
    "Grocery item": {
      "id": "fy%3A%7B", // URL-decoded: fy:{
      "type": "title",
      "title": {}
    },
    "Price": {
      "id": "dia%5B", // URL-decoded: dia[
      "type": "number",
      "number": {
        "format": "dollar"
      }
    },
    "Last ordered": {
      "id": "%5D%5C%5CR%5B", // URL-decoded: ]\\R[
      "type": "date",
      "date": {}
    },
  }
  
  // ... remaining fields omitted
}
```

In this data source object, there are three `properties` defined. Each key is the property name and each value is a property object. Here are some key takeaways:
- **The **`"title"`** type is special.** Every data source has exactly one property with the `"title"` type. Properties of this type refer to the page title for each item in the database. In this example, the *Grocery item* property has this type.
- **The value of **`type`** corresponds to another key in the property object.** Each property object has a nested property named the same as its `type` value. For example, *Last ordered* has the type `"date"`, and it also has a `date` property. **This pattern is used throughout the Notion API on many objects and we call it type-specific data.**
- **Certain property object types have additional configuration.** In this example, *Price* has the type `"number"`. [__Number property objects__](https://developers.notion.com/reference/property-object#number) have additional configuration inside the `number` property. In this example, the `format` configuration is set to `"dollar"` to control the appearance of page property values in this column.

### **Iterate over a data source object**

A request to [__Retrieve a data source__](https://developers.notion.com/reference/retrieve-a-data-source) returns a [__Data source__](https://developers.notion.com/reference/data-source) object. You can iterate over the `properties` object in the response to list information about each property. For example:

JavaScript

```
Object.entries(dataSource.properties).forEach(([propertyName, propertyValue]) => {
    console.log(`${propertyName}: ${propertyValue.type}`);
});
```

## **Adding pages to a data source**

Pages are used as items inside a data source, and each page's properties must conform to its parent database's schema. In other words, if you're viewing a data source as a table, a page's properties define all the values in a single row.

> ## **📘The page properties that are valid depend on the page's parent**
>
> If you are [__creating a page__](https://developers.notion.com/reference/post-page) in a data source, the page properties must match the properties of the database. If you are creating a page that is not a child of a database, `title` is the only property that can be set.

Pages are added to a data source using the [__Create a page API endpoint__](https://developers.notion.com/reference/post-page). Let's try to add a page to the example data source above.

The [__Create a page__](https://developers.notion.com/reference/post-page) endpoint has two required parameters: `parent` and `properties`.

When adding a page to a database, the `parent` parameter must be a [__data source parent__](https://developers.notion.com/reference/parent-object). We can build this object for the example data source above:

JSON

```
{
  "type": "data_source_id",
  "data_source_id": "248104cd-477e-80af-bc30-000bd28de8f9"
}
```

> ## **📘Permissions**
>
> Before an integration can create a page within another page, it needs access to the page parent. To share a page with an integration, click the ••• menu at the top right of a page, scroll to `Add connections`, and use the search bar to find and select the integration from the dropdown list.

> ## **📘Where can I find my database and data source's IDs?**
>
> - Open the database as a full page in Notion.>
> - Use the `Share` menu to `Copy link`.>
> - Now paste the link in your text editor so you can take a closer look. The URL uses the following format:
>
> ```
> https://www.notion.so/{workspace_name}/{database_id}?v={view_id}
> 
> ```
>
> - Find the part that corresponds to `{database_id}` in the URL you pasted. It is a 36 character long string. This value is your **database ID**.>
> - Note that when you receive the database ID from the API, e.g. the [__search__](https://developers.notion.com/reference/post-search) endpoint, it will contain hyphens in the UUIDv4 format. You may use either the hyphenated or un-hyphenated ID when calling the API.>
> - To get the **data source ID**, either use the [__Retrieve a database__](https://developers.notion.com/reference/database-retrieve) endpoint first and check the `data_sources` array, or use the overflow menu under "Manage data sources" to copy it from the Notion app:

Continuing the create page example above, the `properties` parameter is an object that uses property names or IDs as keys, and [__property value objects__](https://developers.notion.com/reference/page-property-values) as values. In order to create this parameter correctly, you refer to the [__property objects__](https://developers.notion.com/reference/property-object) in the database's schema as a blueprint. We can build this object for the example database above too:

JSON

```
{
  "Grocery item": {
    "type": "title",
    "title": [{ "type": "text", "text": { "content": "Tomatoes" } }]
  },
  "Price": {
    "type": "number",
    "number": 1.49
  },
  "Last ordered": {
    "type": "date",
    "date": { "start": "2021-05-11" }
  }
}
```

> ## **📘Building a property value object in code**
>
> Building the property value object manually, as described in this guide, is only helpful when you're working with one specific database that you know about ahead of time.
>
> In order to build an integration that works with any database a user picks, and to remain flexible as the user's chosen database inevitably changes in the future, use the [__Retrieve a database__](https://developers.notion.com/reference/database-retrieve) endpoint, followed by [__Retrieve a data source__](https://developers.notion.com/reference/retrieve-a-data-source). Your integration can call this endpoint to get a current data source schema, and then create the `properties` parameter in code based on that schema.

Using both the `parent` and `properties` parameters, we create a page by sending a request to [__the endpoint__](https://developers.notion.com/reference/post-page).

cURLJavaScript

```
curl -X POST https://api.notion.com/v1/pages \
  -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2025-09-03" \
  --data '{
	  "parent": { "type": "data_source_id", "data_source_id": "248104cd-477e-80af-bc30-000bd28de8f9" },
	  "properties": {
      "Grocery item": {
        "type": "title",
        "title": [{ "type": "text", "text": { "content": "Tomatoes" } }]
      },
      "Price": {
        "type": "number",
        "number": 1.49
      },
      "Last ordered": {
        "type": "date",
        "date": { "start": "2021-05-11" }
      }
    }
  }'
```

Once the page is added, you'll receive a response containing the new [__page object__](https://developers.notion.com/reference/page). An important property in the response is the page ID (`id`). If you're connecting Notion to an external system, it's a good idea to store the page ID. If you want to update the page properties later, you can use the ID with the [__Update page properties__](https://developers.notion.com/reference/patch-page) endpoint.

## **Finding pages in a data source**

Pages can be read from a data source using the [__Query a data source__](https://developers.notion.com/reference/query-a-data-source) endpoint. This endpoint allows you to find pages based on criteria such as "which page has the most recent *Last ordered date*". Some data sources are very large and this endpoint also allows you to get the results in a specific order, and get the results in smaller batches.

> ## **📘Getting a specific page**
>
> If you're looking for one specific page and already have its page ID, you don't need to query a database to find it. Instead, use the [__Retrieve a page__](https://developers.notion.com/reference/retrieve-a-page) endpoint.

### **Filtering data source pages**

The criteria used to find pages are called [__filters__](https://developers.notion.com/reference/post-database-query-filter). Filters can describe simple conditions (i.e. "*Tag* includes *Urgent*") or more complex conditions (i.e. "*Tag* includes *Urgent* AND *Due date* is within the next week AND *Assignee* equals *Cassandra Vasquez*"). These complex conditions are called [__compound filters__](https://developers.notion.com/reference/post-database-query#compound-filters) because they use "and" or "or" to join multiple single property conditions together.

> ## **📘Finding all pages in a data source**
>
> In order to find all the pages in a data source, send a request to the [__query a database__](https://developers.notion.com/reference/post-database-query) without a `filter` parameter.

In this guide, let's focus on a single property condition using the example data source above. Looking at the data source schema, we know the *Last ordered* property uses the type `"date"`. This means we can build a filter for the *Last ordered* property using any [__condition for the __](https://developers.notion.com/reference/filter-data-source-entries#date)`"date"`[__ type__](https://developers.notion.com/reference/filter-data-source-entries#date). The following filter object matches pages where the *Last ordered* date is in the past week:

JavaScript

```
{
  "property": "Last ordered",
  "date": {
    "past_week": {}
  }
}
```

Using this filter, we can find all the pages in the example database that match the condition.

cURLJavaScript

```
curl -X POST https://api.notion.com/v1/data_sources/248104cd477e80afbc30000bd28de8f9/query \
  -H 'Authorization: Bearer '"$NOTION_API_KEY"''
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2025-09-03" \
	--data '{
	  "filter": {
      "property": "Last ordered",
      "date": {
        "past_week": {}
      }
		}
	}'
```

You'll receive a response that contains a list of matching [__page objects__](https://developers.notion.com/reference/page).

JavaScript

```
{
  "object": "list",
  "results": [
    {
      "object": "page",
      /* details omitted */
    }
  ],
  "has_more": false,
  "next_cursor": null
}
```

This is a paginated response. Paginated responses are used throughout the Notion API when returning a potentially large list of objects. The maximum number of results in one paginated response is 100. The [__pagination reference__](https://developers.notion.com/reference/pagination) explains how to use the `"start_cursor"` and `"page_size"` parameters to get more than 100 results.

### **Sorting data source pages**

In this case, the individual pages we requested are in the `"results"` array. What if our integration (or its users) cared most about pages that were created recently? It would be helpful if the results were ordered so that the most recently created page was first, especially if the results didn't fit into one paginated response.

The `sort` parameter is used to order results by individual properties or by timestamps. This parameter can be assigned an array of sort object.

The time which a page was created is not a page property (properties that conform to the data source schema). Instead, it's a property that every page has, and it's one of two kinds of timestamps. It is called the `"created_time"` timestamp. Let's build a [__sort object__](https://developers.notion.com/reference/post-database-query-sort) that orders results so the most recently created page is first:

JSON

```
{
  "timestamp": "created_time",
  "direction": "descending"
}
```

Finally, let's update the request we made earlier to order the page results using this sort object:

cURLJavaScript

```
curl -X POST https://api.notion.com/v1/data_sources/248104cd477e80afbc30000bd28de8f9/query \
  -H 'Authorization: Bearer '"$NOTION_API_KEY"''
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2025-09-03" \
	--data '{
	  "filter": {
      "property": "Last ordered",
      "date": {
        "past_week": {}
      }
		},
    "sorts": [{ "timestamp": "created_time", "direction": "descending" }]
	}'
```

## **Conclusion**

Understanding data source schemas, made from a collection of properties, is key to working with Notion databases. This enables you to add, query for, and manage pages to a data source.

You're ready to help users take advantage of Notion's flexible and extensible data source interface to work with more kinds of data. There's more to learn and do with data sources in the resources below.

### **Next steps**

- This guide explains working with page properties. Take a look at [__working with page content__](https://developers.notion.com/docs/working-with-page-content).
- Explore the [__database object__](https://developers.notion.com/reference/database) and [__data source object__](https://developers.notion.com/reference/data-source) to see their other attributes available in the API.
- Learn about the other [__page property value__](https://developers.notion.com/reference/property-value-object) types. In particular, try to do more with [__rich text__](https://developers.notion.com/reference/rich-text).
- Learn more about [__pagination__](https://developers.notion.com/reference/intro#pagination).

# **Uploading larger files**

Learn how to send files larger than 20 MB in multiple parts.

[Suggest Edits](https://developers.notion.com/edit/sending-larger-files)

API bots in paid workspaces can use File Uploads in multi-part mode to upload files up to 5 GB. To do so, follow the steps below.

## **Step 1: Split the file into parts**

To send files larger than 20 MB, split them up into segments of 5-20 MB each. On Linux systems, one tool to do this is the `split`[__ command__](https://phoenixnap.com/kb/linux-split). In other toolchains, there are libraries such as `split-file`[__ for TypeScript__](https://github.com/tomvlk/node-split-file) to generate file parts.

ShellTypeScript

```
# Split `largefile.txt` into 10MB chunks, named as follows:
# split_part_aa, split_part_ab, etc.
split -b 10M ./largefile.txt split_part
```

> ## **📘Convention for sizes of file parts**
>
> When sending parts of a file to the Notion API, each file must be ≥ 5 and ≤ 20 (binary) megabytes in size, with the exception of the final part (the one with the highest part number), which can be less than 5 MB. The `split` command respects this convention, but the tools in your tech stack might vary.
>
> **To stay within the range, we recommend using a part size of 10 MB**.

## **Step 2: Start a file upload**

This is similar to [__Step 1 of uploading small files__](https://developers.notion.com/reference/uploading-small-files#step-1), but with a few additional required parameters.

Pass a `mode` of `"multi_part"` to the [__Create a file upload__](https://developers.notion.com/reference/create-a-file-upload) API, along with the `number_of_parts`, and a `filename` with a valid extension or a separate MIME `content_type` parameter that can be used to detect an extension.

cURL

```
curl --request POST \
  --url 'https://api.notion.com/v1/file_uploads' \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Content-Type: application/json' \
  -H  'Notion-Version: 2025-09-03' \
  --data '{
    "mode": "multi_part",
    "number_of_parts": 5,
    "filename": "image.png"
  }'
```

## **Step 3: Send all file parts**

Send each file part by using the [__Send File Upload API__](https://developers.notion.com/reference/send-a-file-upload) using the File Upload ID, or the `upload_url` in the response of the [__Create a file upload__](https://developers.notion.com/reference/create-a-file-upload) step.

This is similar to [__Step 2 of uploading small files__](https://developers.notion.com/reference/uploading-small-files#step-2). However, alongside the `file`, the form data in your request must include a field `part_number` that identifies which part you’re sending.

Your system can send file parts in parallel (up to standard Notion API [__rate limits__](https://developers.notion.com/reference/request-limits)). Parts can be uploaded in any order, as long as the entire sequence from {1, …, `number_of_parts`} is successfully sent before calling the [__Complete a file upload__](https://developers.notion.com/reference/complete-a-file-upload) API.

## **Step 4: Complete the file upload**

Call the [__Complete a file upload__](https://developers.notion.com/reference/complete-a-file-upload) API with the ID of the File Upload after all parts are sent.

## **Step 5: Attach the file upload**

After completing the File Upload, its status becomes `uploaded` and it can be attached to blocks and other objects the same way as file uploads created with a `mode` of `single_part` (the default setting).

Using its ID, attach the File Upload (for example, to a block, page, or database) within one hour of creating it to avoid expiry.

> ## **📘Error handling**
>
> The [__Send__](https://developers.notion.com/reference/send-a-file-upload) API validates the total file size against the [__workspace's limit__](https://developers.notion.com/docs/working-with-files-and-media#supported-file-types) at the time of uploading each part. However, because parts can be sent at the same time, the [__Complete__](https://developers.notion.com/reference/complete-a-file-upload) step re-validates the combined file size and can also return an HTTP 400 with a code of `validation_error`.
>
> We recommend checking the file's size before creating the File Upload when possible. Otherwise, make sure your integration can handle excessive file size errors returned from both the Send and Complete APIs.
>
> To manually test your integration, command-line tools like `head`, `dd`, and `split` can help generate file contents of a certain size and split them into 10 MB parts.

# **Parent**

Learn more about different parent objects that link together a workspace's entities in Notion's API.

[__Pages__](https://developers.notion.com/reference/page), [__databases__](https://developers.notion.com/reference/database), [__data sources__](https://developers.notion.com/reference/data-source), [__comments__](https://developers.notion.com/reference/comment-object) and [__blocks__](https://developers.notion.com/reference/block) are either located inside other pages, databases, data sources, and blocks, or are located at the top level of a workspace. This location is known as the "parent". Parent information is represented by a consistent `parent` object throughout the API.

General parenting rules:
- Pages can be parented by other pages, data sources, blocks, or by the whole workspace.
  - *Prior to [__API version 2025-09-03__](https://developers.notion.com/docs/upgrade-guide-2025-09-03), page parents were databases, not data sources.*
- Blocks can be parented by pages, data sources, or blocks.
- Databases can be parented by pages, blocks, or by the whole workspace.
  - *For wikis, databases can also have a data source parent.*
- Data sources are parented by databases.
  - *Linked or externally synced external data sources may have data source parents, but aren't thoroughly supported in Notion's API.*

> ## **🚧Exceptions apply**
>
> These parenting rules reflect the possible response you may receive when retrieving information about pages, databases, and blocks via Notion’s REST API in the latest APIversion.
>
> If you are creating new pages, databases, or blocks via Notion’s public REST API, the parenting rules may vary. For example, the parent of a database currently must be a page if it is [__created__](https://developers.notion.com/reference/create-a-database) via the API.
>
> Refer to the API reference documentation for creating [__pages__](https://developers.notion.com/reference/post-page), [__databases__](https://developers.notion.com/reference/database-create), [__data sources__](https://developers.notion.com/reference/create-a-data-source), and [__blocks__](https://developers.notion.com/reference/patch-block-children) for more information on current parenting rules.

### **Database parent**

Database parents most commonly show up for [__Data source__](https://developers.notion.com/reference/data-source) objects.

**PropertyTypeDescriptionExample values**`typestring`Always `"database_id"`.`"database_id"database_idstring` (UUIDv4)The ID of the [__database__](https://developers.notion.com/reference/database) that this page belongs to.`"b8595b75-abd1-4cad-8dfe-f935a8ef57cb"`

Database parent example

```
{
  "type": "database_id",
  "database_id": "d9824bdc-8445-4327-be8b-5b47500af6ce"
}
```

### **Data source parent**

Data source parents most commonly show up for [__Page__](https://developers.notion.com/reference/page) objects.

**PropertyTypeDescriptionExample values**`typestring`Always `"data_source_id"`.`"data_source_id"data_source_idstring` (UUIDv4)The ID of the [__data source__](https://developers.notion.com/reference/data-source) that this page belongs to.`"1a44be12-0953-4631-b498-9e5817518db8"database_idstring` (UUIDv4)The ID of the [__database__](https://developers.notion.com/reference/database) that the data source belongs to, provided in the API response for convenience.`"b8595b75-abd1-4cad-8dfe-f935a8ef57cb"`

Data source parent example

```
{
  "type": "data_source_id",
  "data_source_id": "1a44be12-0953-4631-b498-9e5817518db8",
  "database_id": "d9824bdc-8445-4327-be8b-5b47500af6ce"
}
```

### **Page parent**

**PropertyTypeDescriptionExample values**`typestring`Always `"page_id"`.`"page_id"page_idstring` (UUIDv4)The ID of the [__page__](https://developers.notion.com/reference/page) that this page belongs to.`"59833787-2cf9-4fdf-8782-e53db20768a5"`

Page parent example

```
{
  "type": "page_id",
  "page_id": "59833787-2cf9-4fdf-8782-e53db20768a5"
}
```

### **Workspace parent**

A page or database with a workspace parent is a top-level page within a Notion workspace. Team-level pages are also currently represented as having a workspace parent in the API.

The workspace `parent` object contains the following keys:

**PropertyTypeDescriptionExample values**`typetype`Always `"workspace"`.`"workspace"workspaceboolean`Always `true`.`true`

Workspace parent example

```
{
  "type": "workspace",
  "workspace": true
}
```

### **Block parent**

A page may have a block parent if it is created inline in a chunk of text, or is located beneath another block like a toggle or bullet block. The `parent` property is an object containing the following keys:

**PropertyTypeDescriptionExample values**`typetype`Always `"block_id"`.`"block_id"block_idstring` (UUIDv4)The ID of the [__page__](https://developers.notion.com/reference/page) that this page belongs to.`"ea29285f-7282-4b00-b80c-32bdbab50261"`

Block parent example

```
{
  "type": "block_id",
  "block_id": "7d50a184-5bbe-4d90-8f29-6bec57ed817b"
}
```

# **uthentication**

Requests use the HTTP `Authorization` header to both authenticate and authorize operations. The Notion API accepts bearer tokens in this header. Bearer tokens are provided to you when you create an integration. If you're creating a public OAuth integration, the integration also receives bearer tokens each time a user completes the OAuth flow.

cURL

```
curl 'https://api.notion.com/v1/users' \
  -H 'Authorization: Bearer '"$NOTION_ACCESS_TOKEN"'' \
  -H "Notion-Version: 2022-06-28"
```

Inside Notion, users will see updates made by integrations attributed to a bot. The bot's name and avatar are controlled in the integration settings.

Using a [__Notion SDK__](https://notionapi.readme.io/reference/intro#code-samples--sdks), a bearer token can be passed once to initialize a `Client` and the client can be used to send multiple authenticated requests.

Notion SDK for JS

```
const { Client } = require('@notionhq/client');

const client = new Client({ auth: process.env.NOTION_ACCESS_TOKEN });
```

Learn more in the [__Authorization guide__](https://developers.notion.com/docs/authorization) .

# **uthorization**

This guide describes the authorization flows for internal and public Notion integrations.

[Suggest Edits](https://developers.notion.com/edit/authorization)

## **What is authorization?**

Authorization is the process of granting an integration access to a user’s Notion data. That process varies depending on whether or not the integration is **public** or **internal**.

> ## **👍**
>
> [__Link Preview integrations__](https://developers.notion.com/docs/link-previews) — a subcategory of public integrations — use two-way OAuth, which differs from the authorization flow described in this guide.
>
> See the [__Build a Link Preview integration guide__](https://developers.notion.com/docs/build-a-link-preview-integration) to learn more about Link Preview authorization.

### **What is an internal integration?**

An internal integration allows Notion workspace members to interact with the workspace through the Notion REST API. Each internal integration is tied to a single, specific workspace and only members within the workspace can use the integration. After an internal integration is added to a workspace, members must manually [__give the integration access to the specific pages or databases__](https://www.notion.so/help/add-and-manage-connections-with-the-api#add-connections-to-pages) that they want it to use.

### **What is a public integration?**

Public integrations can be used by any Notion user in any workspace. They allow members to interact with their workspace using Notion’s REST API once the integration has been properly authorized.

Public integrations follow the [__OAuth 2.0__](https://oauth.net/2/) protocol. This allows workspace members to give access to Notion pages directly through the auth flow, without having to open each Notion workspace page directly and manually give permission to the integration. (More on this below.)

Public integrations can technically be used without permitting workspace pages access as long as the auth flow is completed and an [__access token is created__](https://developers.notion.com/reference/create-a-token) — a process which will be described in detail below. For example, if a public integration *only* needs to interact with the Notion [__User endpoints__](https://developers.notion.com/reference/get-users), it does not need to be given access to workspace pages.

For more details on the differences between public and internal integrations, refer to the [__getting started__](https://developers.notion.com/docs/getting-started#integration-types) page.

Read on to learn how to set up the auth flows for internal and public integrations.

## **Internal integration auth flow set-up**

To use an internal integration, start by creating your integration in the [__integration’s settings page__](https://www.notion.so/profile/integrations).

The internal integration will be associated with the workspace of your choice. You are required to be a workspace owner to create an integration.

Click the **New integration** button on the My integrations page to create a new integration.

Once the integration is created, you can update its settings as needed under the `Configuration` tab and retrieve the integration token in this tab.

The integration token will be used to authenticate REST API requests. The integration sends the same token in every API request.

Find the integration token in the integration's settings.

### **Integration permissions**

Before an integration can interact with your Notion workspace page(s), the page must be manually shared with the integration. To share a page with an integration, visit the page in your Notion workspace, click the ••• menu at the top right of a page, scroll down to `Add connections`, and use the search bar to find and select the integration from the dropdown list.

Once the integration is shared, you can start making API requests. If the page is not shared, any API requests made will respond with an error.

> ## **🚧Keep your token secret**
>
> Your integration token is a secret. To keep your integration secure, never store the token in your source code or commit it in version control. Instead, read the token from an environment variable. Use a secret manager or deployment system to set the token in the environment.
>
> [__Learn more: Best Practices for Handling API Keys__](https://developers.notion.com/docs/best-practices-for-handling-api-keys)

### **Making API requests with an internal integration**

Any time your integration is interacting with your workspace, you will need to include the integration token in the `Authorization` header with every API request. However, if you are using Notion’s [__SDK for JavaScript__](https://github.com/makenotion/notion-sdk-js) to interact with the REST API, the token is set once when a client is initialized.

HTTP

```
GET /v1/pages/b55c9c91-384d-452b-81db-d1ef79372b75 HTTP/1.1
Authorization: Bearer {INTEGRATION_TOKEN}
```

JavaScript

```
const { Client } = require("@notionhq/client")

// Initializing a client
const notion = new Client({
	auth: process.env.NOTION_TOKEN,
})

const getUsers = async () => {
	const listUsersResponse = await notion.users.list({})
}
```

> ## **📘**
>
> If you are not using the [__Notion SDK for JavaScript__](https://github.com/makenotion/notion-sdk-js), you will also need to set the `Notion-Version` and `Content-type` headers in all of in your requests, like so:
>
> JSON
>
> ```
> headers: {
>   Authorization: `Bearer ${process.env.NOTION_TOKEN}`,
>   "Notion-Version": "2022-06-28",
>   "Content-Type": "application/json",
> },
> 
> ```

If you receive an error response from the API, check if the integration has been properly [__added to the page__](https://www.notion.so/help/add-and-manage-connections-with-the-api#manage-connections-in-your-workspace). If this does not solve the problem, refer to our [__Status codes__](https://developers.notion.com/reference/status-codes) page for more information.

## **Public integration auth flow set-up**

When an integration is made public, any Notion user in any workspace can use it.

Since a public integration is not tied to a single workspace with a single integration token, public integrations instead follow the [__OAuth 2.0 protocol__](https://oauth.net/2/) to authorize an integration to interact with a workspace.

### **How to make a public integration**

Select `New Integration` in your integration dashboard and select `Public` in the integration *Type* during the creation flow. You may also edit an existing internal integration to convert to `Public`.

Public integration example.

You will need to fill out the form with additional information, including your company name, website, and redirect URI(s).

The redirect URI is the URI your users will be redirected to after authorizing the public integration. To learn more, read [__OAuth’s description of redirect URIs__](https://www.oauth.com/oauth2-servers/redirect-uris/).

### **Public integration authorization overview**

Once your integration has been made public, you can update your integration code to use the public auth flow.

As an overview, the authorization flow includes the following steps. Each step will be described in more detail below.
1. Navigate the user to the integration’s authorization URL. This URL is provided in the [__integration’s settings page__](https://www.notion.so/profile/integrations).
2. After the user selects which workspace pages to share, Notion redirects the user to the integration’s redirect URI and includes a `code` query parameter. The redirect URI is the one you specified in your [__integration’s settings page__](https://www.notion.so/profile/integrations).
3. You will make a `POST` request to [__create an access token__](https://developers.notion.com/reference/create-a-token) , which will exchange the temporary `code` for an access token.
4. The Notion API responds with an access token and some additional information.
5. You will store the access token for future API requests. View the [__API reference docs__](https://developers.notion.com/reference/intro) to learn about available endpoints.

### **Step 1: Navigate the user to the integration’s authorization URL**

After your integration has been successfully made public in your [__integration’s settings page__](https://www.notion.so/profile/integrations), you will be able to access the integration’s secrets in the **Configuration** tab. Similarly to the internal integrations, these values should be protected and should never be included in source code or version control.

The Authorization URL field populates after a public integration is submitted

As an example, your `.env` file using these secrets could look like this:

Shell

```
#.env

OAUTH_CLIENT_ID=<your-client-id>
OAUTH_CLIENT_SECRET=<your-client-secret>
NOTION_AUTH_URL=<your-auth-url>
```

To start the authorization flow for a public integration, you need to direct the prospective user to the authorization URL. To do this, it is common to include a hyperlink in the integration app that will be interacting with the Notion REST API. For example, if you have an app that will allow users to create new Notion pages for their workspace(s), you will first need them to first visit the authorization URL by clicking on the link.

The following example shows an authorization URL made available through a hyperlink:

HTML

```
<a href="https://api.notion.com/v1/oauth/authorize?owner=user&client_id=463558a3-725e-4f37-b6d3-0889894f68de&redirect_uri=https%3A%2F%2Fexample.com%2Fauth%2Fnotion%2Fcallback&response_type=code">Add to Notion</a>
```

The URL begins with `https://api.notion.com/v1/oauth/authorize` and has the following parameters:

**ParameterDescriptionRequired**`client_id`An identifier for your integration, found in the integration settings.✅`redirect_uri`The URL where the user should return after granting access.✅`response_type`Always use `code`.✅`owner`Always use `user`.✅`state`If the user was in the middle of an interaction or operation, then this parameter can be used to restore state after the user returns. It can also be used to prevent CSRF attacks.

Once the authorization URL is visited, the user will be shown a prompt that varies depending on whether or not the integration comes with a Notion template option.

**Prompt for a standard integration with no template option (Default)**

In the standard integration permissions flow, a prompt describes the integration [__capabilities__](https://developers.notion.com/reference/capabilities), presented to the user as what the integration would like to be able to do in the workspace. A user can either select pages to grant the integration access to, or cancel the request.

Prompt for authorizing a standard integration (no template option)

If the user presses **Cancel**, they will be redirected to the redirect URI with and `error` query param added.

```
www.example.com/my-redirect-uri?error=access_denied&state=
```

You can use this `error`query parameter to conditionally update your app’s state as needed.

If the user opts to `Select pages`, then a page picker interface opens. A user can search for and select pages and databases to share with the integration from the page picker.

> ## **📘**
>
> The page picker only displays pages or databases to which a user has [__full access__](https://www.notion.so/help/sharing-and-permissions), because a user needs full access to a resource in order to be able to share it with an integration.

Page picker interface

Users can select which pages to give the integration access to, including both private and public pages available to them. Parent pages can be selected to quickly provide access to child pages, as giving access to a parent page will provide access to all available child pages. Users can return to this view at a later time to update access settings if circumstances change.

If the user clicks `Allow access`, they are then redirected to the `redirect_uri` with a temporary authorization `code`. If the user denies access, they are redirected to the `redirect_uri` with an `error` query parameter.

If the user clicks `Allow access` and the rest of the auth flow is not completed, the integration will *not* have access to the pages that were selected.

**Prompt for an integration with a Notion template option**

Public integrations offer the option of providing a public Notion page to use as a template during the auth flow.

To add a template to your workspace, complete the following steps:
- Choose a public page in your workspace that you want users to be able to duplicate.
- Navigate to your [__integration’s settings__](https://www.notion.so/profile/integrations) and go to the **Basic Information** tab.
- Scroll to the bottom of your distribution settings and add the URL of the Notion page you selected to the **Notion URL for optional template** input.

Notion URL for optional template input in integration settings.

Once this URL is added, your auth flow prompt appearance will be updated.

Going back to your prompt view, if the integration offers a Notion template option, the first step in the permissions flow will describe the integration [__capabilities__](https://developers.notion.com/reference/capabilities). This is presented to the user as what the integration would be able to do in the workspace, and it prompts the user to click `Next`.

Prompt for an integration with a Notion template option

In the next step, a user can either choose to duplicate the template that you provided or to select existing pages to share with the integration.

A user can select to duplicate a template or to share existing pages with the integration

If the user chooses to duplicate the template, then the following happens automatically:
- The integration is added to the user’s workspace.
- The template is duplicated as a new page in the workspace.
- The new page is shared with the integration.

If the user chooses to select pages to share with the integration, then they continue to the page picker interface that’s part of the [__prompt for a standard integration__](https://developers.notion.com/docs/authorization#prompt-for-a-standard-integration-with-no-template-option-default).

> ## **📘**
>
> After a user installs a public integration, only that user is able to interact or share pages and databases with the integration. Unlike internal integrations, if multiple members in a workspace want to use a public integration, each prospective user needs to individually follow the auth flow for the integration.

**User authorization failures**

User authorization failures can happen. If a user chooses to `Cancel` the request, then a failure is triggered. Build your integration to handle these cases gracefully, as needed.

In some cases, Notion redirects the user to the `redirect_uri` that you set up when you created the public integration, along with an `error` query parameter. Notion uses the common [__error codes in the OAuth specification__](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.1). Use the `error` code to create a helpful prompt for the user when they’re redirected here.

### **Step 2: Notion redirects the user to the integration’s redirect URI and includes a **`code`** parameter**

When you first created the public integration, you specified a redirect URI. If the user follows the prompt to `Allow access` for the integration, then Notion generates a temporary `code` and sends a request to the redirect URI with the following information in the query string:

**ParameterDescriptionRequired**`code`A temporary authorization code.✅`state`The value provided by the integration when the user was [__prompted for access__](https://developers.notion.com/docs/authorization#prompt-for-a-standard-integration-with-no-template-option-default).

To complete the next set, you will need to retrieve the `code` query parameter provided in the redirect. How you retrieve this value will vary depending on your app’s tech stack.

In a React component, for example, the query parameters are made available through the `useRouter()` hook:

JavaScript

```
export default function AuthRedirectPage() {
  const router = useRouter();
  const { code } = router.query;
  ...
}
```

### **Step 3: Send the **`code`** in a **`POST`** request to the Notion API**

The integration needs to exchange the temporary `code` for an `access_token`.

To set up this step, retrieve the `code` from the redirect URI.

Next, you will need to send the `code` as part of a `POST` request to Notion’s token endpoint: [__https://api.notion.com/v1/oauth/token__](https://api.notion.com/v1/oauth/token).

This endpoint is described in more detail in the API reference docs for [__creating a token__](https://developers.notion.com/reference/create-a-token).

The request is authorized using HTTP Basic Authentication. The credential is a colon-delimited combination of the integration’s `CLIENT_ID` and `CLIENT_SECRET`, like so:

```
CLIENT_ID:CLIENT_SECRET
```

You can find both of these values in the [__integration’s settings__](https://www.notion.so/profile/integrations).

Note that in [__HTTP Basic Authentication__](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication), credentials are `base64` encoded before being added to the `Authorization` header.

The body of the request contains the following JSON-encoded fields:

**FieldTypeDescriptionRequired**`"grant_type"string`Always use `"authorization_code"`.✅`"code"string`The temporary authorization code received in the incoming request to the `"redirect_uri"`.✅`"redirect_uri"string`The `"redirect_uri"` that was provided in the Authorization step.✅/❌*

* If the redirect URI was supplied as a query param in the Authorization URL, this field is required. If there are more than one redirect URIs included in your integration settings, this field is required. Otherwise, it is not allowed. Learn more in the [__Create a token page__](https://developers.notion.com/reference/create-a-token).

The following is an example request to exchange the authorization code for an access token:

HTTP

```
POST /v1/oauth/token HTTP/1.1
Authorization: Basic "$CLIENT_ID:$CLIENT_SECRET" 
Content-Type: application/json

{"grant_type":"authorization_code","code":"e202e8c9-0990-40af-855f-ff8f872b1ec6", "redirect_uri":"https://example.com/auth/notion/callback"}
```

The Node-equivalent of this example would look something like this:

JavaScript

```
...
const clientId = process.env.OAUTH_CLIENT_ID;
const clientSecret = process.env.OAUTH_CLIENT_SECRET;
const redirectUri = process.env.OAUTH_REDIRECT_URI;

// encode in base 64
const encoded = btoa(`${clientId}:${clientSecret}`);

const response = await fetch("https://api.notion.com/v1/oauth/token", {
	method: "POST",
	headers: {
	Accept: "application/json",
	"Content-Type": "application/json",
	Authorization: `Basic ${encoded}`,
},
	body: JSON.stringify({
		grant_type: "authorization_code",
		code: "your-temporary-code",
		redirect_uri: redirectUri,
	}),
});
...
```

### **Step 4: Notion responds with an **`access_token`** , **`refresh_token`**, and additional information**

Notion responds to the request with an `access_token`, `refresh_token`, and additional information. The `access_token` will be used to authenticate subsequent Notion REST API requests. The `refresh_token` will be used to refresh the access token, which generates a new `access_token`.

The response contains the following JSON-encoded fields:

**FieldTypeDescriptionNot null**`"access_token"string`An access token used to authorize requests to the Notion API.✅`"refresh_token"string`A refresh token used to generate a new access token✅`"bot_id"string`An identifier for this authorization.✅`"duplicated_template_id"string`The ID of the new page created in the user’s workspace. The new page is a duplicate of the template that the developer provided with the integration. If the developer didn’t provide a template for the integration, then the value is `null`.`"owner"object`An object containing information about who can view and share this integration. `{ "workspace": true }` is returned for installations of workspace-level tokens. For user level tokens, a [__user object__](https://developers.notion.com/reference/user) is returned.✅`"workspace_icon"string`A URL to an image that can be used to display this authorization in the UI.`"workspace_id"string`The ID of the workspace where this authorization took place.✅`"workspace_name"string`A human-readable name that can be used to display this authorization in the UI.

**Token request failures**

If something goes wrong when the integration attempts to exchange the `code` for an `access_token`, then the response contains a JSON-encoded body with an `"error"` field. Notion uses the common [__error codes from the OAuth specification__](https://datatracker.ietf.org/doc/html/rfc6749#section-5.2).

### **Step 5: The integration stores the **`access_token`** and **`refresh_token`** for future requests**

You need to set up a way for your integration to store both the `access_token` and `refresh_token` that it receives. The `access_token` is used to make authorized requests to the Notion API, and the `refresh_token` is used to generate a new `access_token`.

**Tips for storing and using token access**
- Setting up a database is a typical solution for storing access tokens. If you’re using a database, then build relations between an `access_token`, `refresh_token`, and the corresponding Notion resources that your integration accesses with that token. For example, if you store a Notion database or page ID, relate those records with the correct `access_token` that you use to authorize requests to read or write to that database or page, and the `refresh_token` for ongoing token lifecycle support..
- Store all of the information that your integration receives with the `access_token` and `refresh_token`. You never know when your UI or product requirements might change and you’ll need this data. It's really hard (or impossible) to send users to repeat the authorization flow to generate the information again.
- The `bot_id` returned along with your tokens should act as your primary key when storing information.

### **Step 6: Refreshing an access token**

Refreshing an access token will generate a new access token and a new refresh token.

You will need to send the `refresh_token` provided from [__Step 4__](https://developers.notion.com/docs/authorization-asisd03rii#step-4-notion-responds-with-an-access_token--refresh_token-and-additional-information) as part of a `POST` request to Notion’s token endpoint: [__https://api.notion.com/v1/oauth/token__](https://api.notion.com/v1/oauth/token).

This endpoint is described in more detail in the API reference docs for [__refreshing a token__](https://developers.notion.com/reference/refresh-a-token).

The request is authorized using HTTP Basic Authentication. The credential is a colon-delimited combination of the integration’s `CLIENT_ID` and `CLIENT_SECRET`, like so:

```
CLIENT_ID:CLIENT_SECRET
```

You can find both of these values in the [__integration’s settings__](https://www.notion.so/profile/integrations).

Note that in [__HTTP Basic Authentication__](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication), credentials are `base64` encoded before being added to the `Authorization` header.

The body of the request contains the following JSON-encoded fields:

**FieldTypeDescriptionRequired**`"grant_type"string`Always use `"refresh_token"`.✅`"refresh_token"string`The `"refresh_token"` returned in the Authorization step.✅

The following is an example request to exchange the `refresh_token` for a new access token and new refresh token

HTTP

```
POST /v1/oauth/token HTTP/1.1
Authorization: Basic "$CLIENT_ID:$CLIENT_SECRET" 
Content-Type: application/json

{"grant_type":"refresh_token","refresh_token":"nrt_4991090011501Ejc6Xn4sHguI7jZIN449mKe9PRhpMfNK"}
```

The Node-equivalent of this example would look something like this:

JavaScript

```
...
const clientId = process.env.OAUTH_CLIENT_ID;
const clientSecret = process.env.OAUTH_CLIENT_SECRET;

// encode in base 64
const encoded = btoa(`${clientId}:${clientSecret}`);

const response = await fetch("https://api.notion.com/v1/oauth/token", {
	method: "POST",
	headers: {
	Accept: "application/json",
	"Content-Type": "application/json",
	Authorization: `Basic ${encoded}`,
},
	body: JSON.stringify({
		grant_type: "refresh_token",
		refresh_token: "your-refresh-token",
	}),
});
...
```