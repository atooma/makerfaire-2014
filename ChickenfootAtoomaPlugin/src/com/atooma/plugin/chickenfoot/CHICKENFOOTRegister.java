
package com.atooma.plugin.chickenfoot;

import com.atooma.plugin.Module;
import com.atooma.sdk.RegisterService;

public class CHICKENFOOTRegister extends RegisterService {
    @Override
    public Module getModuleInstance() {
        return new CHICKENFOOT(this, CHICKENFOOT.MODULE_ID, CHICKENFOOT.MODULE_VERSION);
    }
}
