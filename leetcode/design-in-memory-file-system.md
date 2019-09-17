# 588. Design In-Memory File System

* *Difficulty: Hard*

* *Topics: Design*

* *Similar Questions:*

  * [LRU Cache](lru-cache.md)

  * [LFU Cache](lfu-cache.md)

  * [Design Log Storage System](design-log-storage-system.md)

## Problem:

<p>Design an in-memory file system to simulate the following functions:</p>

<p><code>ls</code>: Given a path in string format. If it is a file path, return a list that only contains this file&#39;s name. If it is a directory path, return the list of file and directory names <b>in this directory</b>. Your output (file and directory names together) should in <b>lexicographic order</b>.</p>

<p><code>mkdir</code>: Given a <b>directory path</b> that does not exist, you should make a new directory according to the path. If the middle directories in the path don&#39;t exist either, you should create them as well. This function has void return type.</p>

<p><code>addContentToFile</code>: Given a <b>file path</b> and <b>file content</b> in string format. If the file doesn&#39;t exist, you need to create that file containing given content. If the file already exists, you need to <b>append</b> given content to original content. This function has void return type.</p>

<p><code>readContentFromFile</code>: Given a <b>file path</b>, return its <b>content</b> in string format.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> 
[&quot;FileSystem&quot;,&quot;ls&quot;,&quot;mkdir&quot;,&quot;addContentToFile&quot;,&quot;ls&quot;,&quot;readContentFromFile&quot;]
[[],[&quot;/&quot;],[&quot;/a/b/c&quot;],[&quot;/a/b/c/d&quot;,&quot;hello&quot;],[&quot;/&quot;],[&quot;/a/b/c/d&quot;]]

<b>Output:</b>
[null,[],null,null,[&quot;a&quot;],&quot;hello&quot;]

<b>Explanation:</b>
<img alt="filesystem" src="https://assets.leetcode.com/uploads/2018/10/12/filesystem.png" style="width: 640px;" />
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>You can assume all file or directory paths are absolute paths which begin with <code>/</code> and do not end with <code>/</code> except that the path is just <code>&quot;/&quot;</code>.</li>
	<li>You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.</li>
	<li>You can assume that all directory names and file names only contain lower-case letters, and same names won&#39;t exist in the same directory.</li>
</ol>

## Solutions:

```c++
class FileSystem {
public:
    FileSystem() {
        root = new Directory("");
    }
    
    vector<string> ls(string path) {
        vector<string> tokens = tokenize(path);
        Node* cur = root;
        for (auto& token : tokens) {
            cur = cur->next[token];
        }
        
        return cur->ls();
    }
    
    void mkdir(string path) {
        vector<string> tokens = tokenize(path);
        Node* cur = root;
        for (auto& token : tokens) {
            if (cur->next.count(token) == 0) {
                cur->next[token] = new Directory(token);
            }
            cur = cur->next[token];
        }
    }
    
    void addContentToFile(string filePath, string content) {
        vector<string> tokens = tokenize(filePath);
        Node* cur = root;
        for (auto& token : tokens) {
            if (cur->next.count(token) == 0) {
                cur->next[token] = new File(token);
            }
            cur = cur->next[token];
        }
        
        ((File*) cur)->append(content);
    }
    
    string readContentFromFile(string filePath) {
        vector<string> tokens = tokenize(filePath);
        Node* cur = root;
        for (auto& token : tokens) {
            cur = cur->next[token];
        }
        
        return ((File*) cur)->read();
    }
    
private:
    class Node {
    public:
        Node(const string& name) {
            this->name = name;
        }
        
        string getName() {
            return name;
        }
        
        virtual bool isDirectory() = 0;
        virtual vector<string> ls() = 0; 
        
        map<string, Node*> next;
    protected:
        string name;
    };
    
    class File : public Node {
    public:
        File(const string& name): Node(name) {}
        
        bool isDirectory() override{
            return false;
        }
        
        vector<string> ls() override {
            return {name};
        }
        
        void append(const string& str) {
            data.append(str);
        }
        
        string read() {
            return data;
        }
    private:
        string data;
    };
    
    class Directory : public Node {
    public:
        Directory(const string& name): Node(name) {}
        
        bool isDirectory() override {
            return true;
        }
        
        vector<string> ls() override {
            vector<string> ret;
            for (auto it = next.begin(); it != next.end(); ++it) {
                ret.push_back(it->first);
            }
            
            return ret;
        }
    private:
        
    };
    
    vector<string> tokenize(const string& path) {
        vector<string> ret;
        int pos = 1;
        string token;
        while (pos < path.length()) {
            if (path[pos] == '/') {
                ret.push_back(token);
                token.clear();
            } else {
                token.push_back(path[pos]);
            }
            ++pos;
        }
        
        if (token.length() > 0) {
            ret.push_back(token);
        }
        
        return ret;
    }
    
    Node* root;
};

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem* obj = new FileSystem();
 * vector<string> param_1 = obj->ls(path);
 * obj->mkdir(path);
 * obj->addContentToFile(filePath,content);
 * string param_4 = obj->readContentFromFile(filePath);
 */
```
