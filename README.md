# PythonRecipe

レシピ構造化・生成システム

## Components

### Recipe

1. `recipe_parser`
   * Collecting recipe data from recipe websites
   * Target : pro recipes
     * chef gohan
     * TODO: lettuce club
     * TODO: orange page
     * TODO: kurashiru

2. `recipe_db_constructor`
   * Reading recipe data
   * Extracting recipe features
     * `extract_abstract_instruction`

   * Constructing `RecipeDB`

3. `RecipeDBAccesor`
   * `__init__` : Reading path to import `RecipeDB`
   * `get_random` : Randomly Selecting a recipe
   * `filter` : Filtering recipes


### Ingredient

1. `ingredient_db_constructor`
   * Reading food data
   * Extracting food feature
   * Constructing `IngredientDB`

2. `IngredientDBAccesor`
   * `__init__` : Reading path to import `IngredientDB`
   * `get_similar` : Getting similar ingredient for substitution
     * `random` : Getting a ingredient from top-10 similar ingredients


### Generator

1. `RecipeGenerator`
   * `__init__` : Initializing `RecipeDBAccesor` and `IngredientDBAccesor`
   * TODO: `get_userdata`
   * `substitute` : Suggesting substitution for chosen ingredient
   * TODO: `arrange` : Arranging recipe


### TODO: Personalization

1. `user_interface` : Prividing user interface
   * `get_user_data` : Registering `UserData`
   * `add_log` : Adding log to a `UserData`

2. `UserDataAccesor`
   * `__init__` : Reading `UserData`
   * `get_userdata` : providing


## Plan

- [ ] テキストによる紐づけ
  * 日本語の類似度計算
  * ハイブリッドな紐づけシステム：候補表示・選択UIと紐づけキーの登録

- [ ] 風味データ統合
  * `IngredientDB`にFooDB統合
  * 料理の風味計算

- [ ] 食材分析
  * 代替食材提案
  * 食材クラスタリング　→複数食材代替

- [ ] 複数食材による代替（例：鶏むね肉→鶏もも肉＋豆腐）
  * サブグラフマッチング

- [ ] レシピデータ抽出
  * アプリオリ抽出

