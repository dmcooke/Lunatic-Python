
define lua_print_tvalue
    if $arg0->tt == 0
        echo nil
    else
    if $arg0->tt == 1
        if $arg0->value.b == 0
            echo boolean false\n
        else
            printf "boolean true (%x)\n", $arg0->value.b
        end
    else
    if $arg0->tt == 2
        printf "lightuserdata %p\n", $arg0->value.p
    else
    if $arg0->tt == 3
        printf "number %g\n", $arg0->value.n
    else
    if $arg0->tt == 4
        set $_tsv = $arg0->value.gc->ts.tsv
        printf "string len=%d hash=%d \"%s\"\n", $_tsv.len, $_tsv.hash, (char *)(&($arg0->value.gc->ts)+1)
    else
    if $arg0->tt == 5
        printf "table @ %p\n", $arg0->value.gc->h
    else
    if $arg0->tt == 6
        printf "function @ %p\n", $arg0->value.gc->cl
    else
    if $arg0->tt == 7
        set $_uv = $arg0->value.gc->u.uv
        printf "userdata (%d bytes) @ %p, metatable @ %p\n", $_uv.len, $_uv.env, $_uv.metatable
    else
    if $arg0->tt == 8
        printf "thread @ %p\n", $arg0->value.gc->th
    end
    end
    end
    end
    end
    end
    end
    end
    end
end
