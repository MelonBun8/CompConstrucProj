# Symbol Table Data & Verification Chart

## 1. Sample Code Program (`scope_test.calc`)

```javascript
/* 1  */ // 1. Global Scope
/* 2  */ g_a = 10; g_c = g_a + 4;
/* 3  */ g_b = 3.5; g_c = g_c + 1; print(g_c);
/* 4  */ if (g_a > 5) { // 2. If Block Scope
/* 5  */     if_var = 1;
/* 6  */     g_a = 20;  // Creates local g_a (shadows global g_a) 
/* 7  */     // 3. Nested Block Scope
/* 8  */     {
/* 9  */         block_var = 99;
/* 10 */         if_var = 2; // Creates local if_var (shadows Scope 1 if_var)
/* 11 */     } 
/* 12 */ // Scope 2 END
/* 13 */ } 
/* 14 */ // Scope 1 END
/* 15 */ // Loop Scope
/* 16 */ counter = 10;
/* 17 */ while (counter > 0) {
/* 18 */     loop_var = 50; print(loop_var);
/* 19 */     counter = 0;
/* 20 */     g_a = 77; // Shadows Global g_a
/* 21 */ }
/* 22 */ // Loop Scope END
/* 23 */ print(counter); // Should be 10 (global)
/* 24 */ //print(loop_var);
```

---

## 2. Symbol Table Stack (Snapshot at Line 10)

This snapshot represents the state of the symbol tables when execution is at the deepest point of nesting (inside the nested block).

### **Scope 2 (Nested Block)**

| Name | Kind | Type | Decl Line | Scope | Offset | Size | Mangled Name |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `block_var` | Var | `int` | 9 | 2 | 0 | 4 | `block_var_6` |
| `if_var` | Var | `int` | 10 | 2 | 4 | 4 | `if_var_7` |

### **Scope 1 (If-Block)**

| Name | Kind | Type | Decl Line | Scope | Offset | Size | Mangled Name |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `if_var` | Var | `int` | 5 | 1 | 0 | 4 | `if_var_4` |
| `g_a` | Var | `int` | 6 | 1 | 4 | 4 | `g_a_5` |

### **Scope 0 (Global)**

| Name | Kind | Type | Decl Line | Scope | Offset | Size | Mangled Name |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `g_a` | Var | `int` | 2 | 0 | 0 | 4 | `g_a_1` |
| `g_c` | Var | `int` | 2 | 0 | 4 | 4 | `g_c_3` |
| `g_b` | Var | `float` | 3 | 0 | 8 | 8 | `g_b_2` |
| `counter` | Var | `int` | 16 | 0 | 16 | 4 | `counter_8` |

*(Note: `counter` is defined later at Line 16, but shown here for completeness of the Global Scope)*

---

## 3. Symbol Table Stack (Snapshot at Line 18)

This snapshot represents the state inside the `while` loop, demonstrating variable hoisting.

### **Scope 3 (While Loop)**

| Name | Kind | Type | Decl Line | Scope | Offset | Size | Mangled Name |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `counter` | Var | `int` | 17 (Hoist) | 3 | 0 | 4 | `counter_9` |
| `loop_var` | Var | `int` | 18 | 3 | 4 | 4 | `loop_var_10` |
| `g_a` | Var | `int` | 20 | 3 | 8 | 4 | `g_a_11` |

*(Note: `counter` uses the reused symbol `counter_9` for subsequent assignments in this scope)*

### **Scope 0 (Global)**

*(Same as above)*

---

## 4. Symbol Table Operations Trace

This table lists the create/delete/insert/lookup operations performed during the semantic analysis pass.

| Line | Operation | Name | Kind | Type | Decl | Scope | Offset | Size | Details |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2 | **Insert** | `g_a` | Var | `int` | 2 | 0 | 0 | 4 | Defined global `g_a` |
| 2 | **Lookup** | `g_a` | Var | `int` | 2 | 0 | 0 | 4 | RHS of `g_c = ...` |
| 2 | **Insert** | `g_c` | Var | `int` | 2 | 0 | 4 | 4 | Defined global `g_c` |
| 3 | **Insert** | `g_b` | Var | `float` | 3 | 0 | 8 | 8 | Defined global `g_b` |
| 3 | **Lookup** | `g_c` | Var | `int` | 2 | 0 | 4 | 4 | RHS increment |
| 3 | **Insert** | `g_c` | Var | `int` | 2 | 0 | 4 | 4 | Re-assignment (updates symbol) |
| 4 | **Lookup** | `g_a` | Var | `int` | 2 | 0 | 0 | 4 | If condition |
| 4 | **Enter Scope** | - | - | - | - | 1 | - | - | **Start If-Block Scope** |
| 5 | **Insert** | `if_var` | Var | `int` | 5 | 1 | 0 | 4 | Local variable |
| 6 | **Insert** | `g_a` | Var | `int` | 6 | 1 | 4 | 4 | **Shadows** Global `g_a` |
| 8 | **Enter Scope** | - | - | - | - | 2 | - | - | **Start Nested Block Scope** |
| 9 | **Insert** | `block_var` | Var | `int` | 9 | 2 | 0 | 4 | Local variable |
| 10 | **Insert** | `if_var` | Var | `int` | 10 | 2 | 4 | 4 | **Shadows** Scope 1 `if_var` |
| 11 | **Exit Scope** | - | - | - | - | 1 | - | - | End Nested Block Scope |
| 13 | **Exit Scope** | - | - | - | - | 0 | - | - | End If-Block Scope |
| 16 | **Insert** | `counter` | Var | `int` | 16 | 0 | 16 | 4 | Defined global `counter` |
| 17 | **Enter Scope** | - | - | - | - | 3 | - | - | **Start While Loop Scope** |
| 17 | **Hoist** | `counter` | Var | `int` | 17 | 3 | 0 | 4 | **Copy-on-Entry** from Global |
| 17 | **Lookup** | `counter` | Var | `int` | 17 | 3 | 0 | 4 | Condition Check (Pre-Loop) |
| 18 | **Insert** | `loop_var` | Var | `int` | 18 | 3 | 4 | 4 | Local variable |
| 19 | **Lookup** | `counter` | Var | `int` | 17 | 3 | 0 | 4 | Assignment LHS (Resovles Local) |
| 20 | **Insert** | `g_a` | Var | `int` | 20 | 3 | 8 | 4 | **Shadows** Global `g_a` |
| 17 | **Lookup** | `counter` | Var | `int` | 17 | 3 | 0 | 4 | Condition Check (Post-Loop) |
| 21 | **Exit Scope** | - | - | - | - | 0 | - | - | End While Loop Scope |
| 23 | **Lookup** | `counter` | Var | `int` | 16 | 0 | 16 | 4 | Print Global `counter` (10) |
